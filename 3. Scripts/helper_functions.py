from IPython.display import Markdown, display
import matplotlib.pyplot as plt
import plotnine as p9
from plotnine.stats.stat_boxplot import weighted_percentile
from onstove import RasterLayer, VectorLayer
import pandas as pd
import numpy as np
import os
#from tkinter import filedialog as fd


# def select_file():
#     file = fd.askopenfile()
#     print(file.name)

# def select_directory():
#     dir = fd.askdirectory(initialdir = "/", title = "Select output directory")
#     print(dir)

def get_tariff(row, energy, tariffs, exchange_rate):
    breaker = (tariffs['Breaker size (Amp)'] == row['variable'])
    demand = energy / (3.6 * 12)
    demand_level = tariffs.loc[tariffs['kWh (Monthly)'] >= demand, 'kWh (Monthly)'].min()
    demand_rows = (tariffs['kWh (Monthly)'] == demand_level)
    dff = tariffs.loc[breaker & demand_rows]
    return (float(dff['Monthly Minimum Charge (Nrs.)'].iloc[0]) / demand + float(dff['Energy Charge (Nrs./kWh)'].iloc[0])) / exchange_rate

def swatches(colors, sep=' ', width=1):
    display(Markdown(sep.join(
        f'<span style="color: {color}">{chr(9607)*width} <span style="font-family: monospace">{color} - <span style="font-family: monospace">{label} </span></span><br>'
        for label, color in colors.items()
    )))  

def plot_baseline_split(model, labels):
    df = pd.DataFrame()
    for tech in model.techs.values():
        dff = pd.DataFrame({'tech': [tech.name], 
                            'Population': [tech.current_share_urban * model.specs['population_start_year'] * model.specs['urban_start']], 
                            'region': 'Urban'})
        df = pd.concat([df, dff], ignore_index=True)
        dff = pd.DataFrame({'tech': [tech.name], 
                            'Population': [tech.current_share_rural * model.specs['population_start_year'] * (1 - model.specs['urban_start'])], 
                            'region': 'Rural'})
        df = pd.concat([df, dff], ignore_index=True)
    
    model._re_name(df, labels, 'tech')
    df = df.loc[df['Population']>0]
    df['Population'] /= 1000000
    df['Share'] = df['Population'] / df['Population'].sum()
    shares = df.loc[df['Share']>0.005].copy()
    shares['label_position'] = shares.groupby('tech')['Population'].transform('cumsum')
    
    tech_list = df.groupby('tech')[['Population']].sum().sort_values('Population').index.tolist()
    colors = {'Urban': '#009fc3', 'Rural': '#b30437'}
    # colors = {'Urban': '#9bd5e7', 'Rural': '#e1a4a0'}
    
    p = (p9.ggplot(df)
        + p9.geom_col(p9.aes(x='tech', y='Population', fill='region'))#, position='dodge')
        + p9.geom_label(shares,
                        p9.aes(x='tech', y='label_position', label='Share*100'),
                        format_string='{:.0f}%',
                        size=6,
                        color='#231f20'
                        )
        + p9.scale_x_discrete(limits=tech_list)
        + p9.ylim(0, shares['label_position'].max() * 1.02)
        + p9.scale_fill_manual(colors)
        + p9.coord_flip()
        + p9.theme_minimal()
        + p9.theme(text=p9.element_text(size=6, color='#231f20'), legend_position=(0.82, 0.2), legend_direction='horizontal', 
                   legend_background=p9.element_rect(color='white', size=0.5, fill='#f9f9f9'), legend_box_margin=2
                  )
        + p9.labs(x='', y='Population (Millions)', fill='Municipalities'))
    
    p.save(os.path.join(model.output_directory, 'current_share.pdf'), height=70/24.5, width=90/24.5)
    p.save(os.path.join(model.output_directory, 'current_share.png'), height=70/24.5, width=90/24.5, dpi=300)
    return p

def available_layers(d, indent=0):
    for key, values in d.items():
        print(' ' * 4 * indent + '\033[1m' + str(key) + ':\033[0m' )
        for name in values.keys():
            print(' ' * 4 * (indent+1)+ str(name))

def histogram(model, index: RasterLayer, name: str, labels: dict, cmap: dict, output_folder: str):
    dff = model.gdf[['Households', 'max_benefit_tech']].copy()
    x = model.raster_to_dataframe(index, method='read')
    xf = pd.Series(x)

    dff[name] = xf
    dff = model._re_name(dff, labels, 'max_benefit_tech')
    dff = dff.loc[dff['max_benefit_tech']==name]

    dff['Households'] /= 1000

    max_val = dff[name].max()
    min_val = dff[name].min()
    binwidth = (max_val - min_val) * 0.05

    p = model._histogram(dff, cat='max_benefit_tech', x=name, 
                         cmap = cmap, x_title = f'{name} priority index (-)', y_title = 'Households (k)',
                         font_args=dict(color='black', size=11),
                         kwargs=dict(binwidth=binwidth, alpha=0.8, size=0.2)) + p9.theme(legend_position="none")
    
    # Add quantile lines
    q1, q3 = weighted_percentile(a=dff[name].values, q=(25, 75), weights=dff['Households'].values)
    line1 = p9.geom_vline(xintercept=q1, color="#4D4D4D", size=0.8, linetype="dashed")
    line3 = p9.geom_vline(xintercept=q3, color="#4D4D4D", size=0.8, linetype="dashed")

    hist = p + line1 + line3

    # get figure to annotate
    fig = hist.draw() # get the matplotlib figure object
    ax = fig.axes[0] # get the matplotlib axis (may be more than one if faceted)

    # annotate quantiles
    trans = ax.get_xaxis_transform()
    ax.annotate('Q1', xy=(q1, 1.05), xycoords=trans,
                horizontalalignment='center',
                color='#4D4D4D', weight="bold")
    ax.annotate('Q3', xy=(q3, 1.05), xycoords=trans,
                horizontalalignment='center',
                color='#4D4D4D', weight="bold")
    
    fig.set_size_inches(4, 2.5)
    fig.savefig(os.path.join(output_folder, f'{name.replace(" ", "_")}_index.pdf'), bbox_inches='tight', transparent=True)
    return fig

def set_weights(model, index):
    w = model.raster_to_dataframe(index, method='read')
    indices = np.where(~np.isnan(w))
    return model.gdf.index.map(pd.Series(w, index=[x for x in range(len(w))]))

def prioritize_households(model, index, technology, goal):
    if 'Prioritized_hh' not in model.gdf.columns:
        model.gdf['Prioritized_hh'] = 'None'
        
    model.gdf['weights'] = 0
    model.gdf['weights'] = set_weights(model, index)

    households = 0
    step = 0.01
    i = 1
    
    if isinstance(technology, list):
        tech = technology[0]
    else:
        tech = technology
        technology = [technology]

    while households < goal:
        bool_vec = (model.gdf['weights'] >= i) & (model.gdf['max_benefit_tech'].isin(technology))
        _households = model.gdf.loc[bool_vec, "Households"].sum()

        if _households <= (goal * 1.01):
            households = _households
            model.gdf.loc[bool_vec, 'Prioritized_hh'] = tech
        else:
            i += step
            step *= 0.1

        if i == 0:
            break
        i -= step
        if i < 0:
            i = 0
    if households >= goal:
        print(f'Households using {" or ".join(technology)}:', f'{households:.0f}', 'Goal:', f'{goal:.0f}')
    else:
        print(f'Goal not reached for {" or ".join(technology)}, households:', f'{households:.0f}', 'Goal:', f'{goal:.0f}')

    model.gdf.drop('weights', axis=1, inplace=True)
    
def prioritize_households_2(model, index, technology, goal):
    households =  model.gdf.loc[model.gdf['Prioritized_hh']==technology, 'Households'].sum()

    model.gdf['weights'] = 0
    model.gdf['weights'] = set_weights(model, index)

    step = 0.01
    i = 1
    # goal -= households
    # households = 0
    
    while households < goal:
        bool_vec = (model.gdf['weights'] >= i) & ((model.gdf['Prioritized_hh']=='None'))
        _households = model.gdf.loc[bool_vec | (model.gdf['Prioritized_hh']==technology), "Households"].sum()

        if _households <= (goal * 1.01):
            households = _households
            model.gdf.loc[bool_vec, 'Prioritized_hh'] = technology
        else:
            i += step
            step *= 0.1

        if i == 0:
            break
        i -= step
        if i < 0:
            i = 0
            
    if households >= goal:
        print(f'Households using {technology}:', f'{households:.0f}', 'Goal:', f'{goal:.0f}')
    else:
        print(f'Goal not reached for {technology}, households:', f'{households:.0f}', 'Goal:', f'{goal:.0f}')  