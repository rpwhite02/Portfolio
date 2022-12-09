import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd


def load_in_data(shp_file_name, csv_file_name):
    """
    The load_in_data function takes the shp file the geographic data and the
    csv file that contains census tract data and returns the two datasets
    merged together. Result should be a GeoDataFrame.
    """
    census_data = gpd.read_file(shp_file_name)
    food_access_data = pd.read_csv(csv_file_name)
    filtered_data = census_data.merge(food_access_data,
                                      right_on='CensusTract',
                                      left_on='CTIDFP00', how='left')
    return filtered_data


def percentage_food_data(state_data):
    """
    The percentage_food_data takes the merged data and returns the percentage
    of census tracts in Washington for which there is food access data present
    in the files we were given. Result is not rounded.
    """
    filtered_state = state_data['CensusTract'].dropna()
    total = len(state_data['CensusTract'])
    filtered = len(filtered_state)
    percentage = filtered / total * 100
    return percentage


def plot_map(state_data):
    """
    The plot_map function takes the merged data and plots a map of Washington
    with all of the census tracts.
    """
    state_data.plot()
    plt.title('Washington State')
    plt.savefig('map.png')


def plot_population_map(state_data):
    """
    The plot_population_map function takes the merged data and plots the
    shapes of all the census tracts in Washington where each census tract is
    colored from a legend according to its population. Under the population
    plot, all of Washington's census tracts will be the background.
    """
    fig, ax = plt.subplots(1)
    state_data.plot(color='#EEEEEE', ax=ax)
    state_data.plot(column='POP2010', legend=True, ax=ax)
    plt.title('Washington Census Tract Populations')
    plt.savefig('population_map.png')


def plot_population_county_map(state_data):
    """
    The plot_population_county_map takes the merged data and plots the shapes
    of all the census tracts in Washington where each Washington state county
    is colored from a legend according to its population. Under the population
    plot, all of Washington's census tracts will be the background.
    """
    fig, ax = plt.subplots(1)
    county_data = state_data[['POP2010', 'County', 'geometry']]
    by_county = county_data.dissolve(by='County', aggfunc='sum')
    state_data.plot(color='#EEEEEE', ax=ax)
    by_county.plot(column='POP2010', ax=ax, legend=True)
    plt.title('Washington County Populations')
    plt.savefig('county_population_map.png')


def plot_food_access_by_county(state_data):
    """
    The plot_food_access_by_county function takes the merged data and produces
    4 plots showing information we have from the data files across different
    income levels. Compute the ratio and create new columns for (1) number of
    people in the census tract having low access in a half mile radius,
    (2) number of people in the census tract having low access in a 10 mile
    radius, (3) number of people in the census tract having low access in a
    half mile radius and are also low income, and (4) number of people in the
    census tract having low access in a 10 mile radius and are also low
    income.
    """
    filtered_data = state_data[['County', 'geometry', 'POP2010', 'lapophalf',
                               'lapop10', 'lalowihalf', 'lalowi10']]
    filtered_data = filtered_data.dissolve(by='County', aggfunc='sum')
    filtered_data['lapophalf_ratio'] = filtered_data['lapophalf']\
        / filtered_data['POP2010']
    filtered_data['lapop10_ratio'] = filtered_data['lapop10']\
        / filtered_data['POP2010']
    filtered_data['lalowihalf_ratio'] = filtered_data['lalowihalf']\
        / filtered_data['POP2010']
    filtered_data['lalowi10_ratio'] = filtered_data['lalowi10']\
        / filtered_data['POP2010']
    fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2, 2, figsize=(20, 10))
    state_data.plot(color='#EEEEEE', ax=ax1)
    filtered_data.plot(column='lapophalf_ratio', legend=True, ax=ax1, vmin=0,
                       vmax=1)
    ax1.set_title('Low Access: Half')
    state_data.plot(color='#EEEEEE', ax=ax2)
    filtered_data.plot(column='lalowihalf_ratio', legend=True, ax=ax2, vmin=0,
                       vmax=1)
    ax2.set_title('Low Access + Low Income: Half')
    state_data.plot(color='#EEEEEE', ax=ax3)
    filtered_data.plot(column='lapop10_ratio', legend=True, ax=ax3, vmin=0,
                       vmax=1)
    ax3.set_title('Low Access: 10')
    state_data.plot(color='#EEEEEE', ax=ax4)
    filtered_data.plot(column='lalowi10_ratio', legend=True, ax=ax4, vmin=0,
                       vmax=1)
    ax4.set_title('Low Access + Low Income: 10')
    plt.savefig('county_food_access.png')


def plot_low_access_tracts(state_data):
    """
    The plot_low_access_tracts function takes the merged data and computes and
    plots all census tracts that are considered low access. Under the low
    access plot, there will be a plot for which we have food access data, and
    under that plot all of Washington's census tracts will be the main
    background.
    """
    state_no_na = state_data.dropna()
    if_urban = (state_data['Urban'] == 1.0)
    if_rural = (state_data['Rural'] == 1.0)
    if_urban = state_data[if_urban]
    if_rural = state_data[if_rural]
    is_half_mile = (if_urban['lapophalf'] >= 500) | (if_urban['lapophalf'] >=
                                                     if_urban['POP2010'] *
                                                     0.33)
    is_10_miles = (if_rural['lapop10'] >= 500) | (if_rural['lapop10'] >=
                                                  if_rural['POP2010'] * 0.33)
    is_half_mile = if_urban[is_half_mile]
    is_10_miles = if_rural[is_10_miles]
    fig, ax = plt.subplots(1)
    state_data.plot(color='#EEEEEE', ax=ax)
    state_no_na.plot(color='#AAAAAA', ax=ax)
    is_half_mile.plot(ax=ax)
    is_10_miles.plot(ax=ax)
    plt.title('Low Access Census Tracts')
    plt.savefig('low_access.png')


def main():
    state_data = load_in_data(
        '/course/food_access/tl_2010_53_tract00/tl_2010_53_tract00.shp',
        '/course/food_access/food_access.csv'
    )
    print(percentage_food_data(state_data))
    plot_map(state_data)
    plot_population_map(state_data)
    plot_population_county_map(state_data)
    plot_food_access_by_county(state_data)
    plot_low_access_tracts(state_data)


if __name__ == '__main__':
    main()
