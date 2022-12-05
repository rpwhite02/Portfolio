import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
sns.set()


def compare_bachelors_1980(data):
    """
    The compare_bachelors function takes the dataset as a parameter and returns
    the percentages of men and women who ahcieved a minimum degree of a
    bachelor's in the year 1980. This is done in the form of a 2-by-2 dataframe
    with rows corresponding to men and women and the columns corresponding to
    sex and total.
    """
    is_male = data['Sex'] == 'M'
    is_female = data['Sex'] == 'F'
    is_bachelors = data['Min degree'] == "bachelor's"
    is_1980 = data['Year'] == 1980
    filtered_data = data[(is_male | is_female) & is_bachelors & is_1980]
    return filtered_data[['Sex', 'Total']]
  
  
def top_2_2000s(data, sex='A'):
    """
    The top_2_2000s function takes a dataset and a default parameter for the
    sex column as 'A'. The function should then return a 2-element series
    showing the degrees and their respective average percentages for the years
    2000-2010(inclusive).
    """
    is_sex = data['Sex'] == sex
    in_range = (data['Year'] >= 2000) & (data['Year'] <= 2010)
    filtered_data = data[is_sex & in_range]
    group = filtered_data.groupby('Min degree')['Total'].mean()
    result = group.nlargest(2)
    return result


def line_plot_bachelors(data):
    """
    The line_plot_bachelors function takes a dataset as a parameter and
    then plots a line chart with the x axis as years and the y axis as the
    total percentages. Filtered data includes sex column = 'A' and min degree =
    'bachelor's'.
    """
    is_a = data['Sex'] == 'A'
    is_bachelors = data['Min degree'] == "bachelor's"
    filtered_data = data[is_a & is_bachelors]
    sns.relplot(x='Year', y='Total', data=filtered_data, kind='line')
    plt.title("Percentage Earning Bachelor's over Time")
    plt.xlabel('Year')
    plt.ylabel('Percentage')
    plt.savefig('line_plot_bachelors.png', bbox_inches='tight')


def bar_chart_high_school(data):
    """
    The bar_chart_high_school function takes a dataset as a parameter and plots
    a bar chart with the x axis as sex and the y axis as percentage of people.
    This is done using the catplot function from seaborn and titles and labels
    using matplotlib.
    """
    is_high_school = data['Min degree'] == 'high school'
    is_2009 = data['Year'] == 2009
    filtered_data = data[is_2009 & is_high_school]
    sns.catplot(x='Sex', y='Total', data=filtered_data, kind='bar')
    plt.title('Percentage Completed High School by Sex')
    plt.ylabel('Percentage')
    plt.savefig('bar_chart_high_school.png', bbox_inches='tight')


def plot_hispanic_min_degree(data):
    """
    The plot_hispanic_min_degree function takes a dataset as a parameter and
    returns a chart type of choice for this plot. Label the axis and title the
    plot accordingly.
    """
    is_date = (data['Year'] >= 1990) & (data['Year'] <= 2010)
    is_bachelors = data['Min degree'] == "bachelor's"
    is_high_school = data['Min degree'] == 'high school'
    all_sexes = data['Sex'] == 'A'
    filtered_data = data[(is_bachelors | is_high_school) & is_date & all_sexes]
    sns.catplot(x='Year', y='Hispanic', data=filtered_data, kind='bar',
                hue='Min degree')
    plt.title("How Minimum Degrees Hispanic People Obtain Change Over Time")
    plt.ylabel('Percentage of Hispanics')
    plt.savefig('plot_hispanic_min_degree.png', bbox_inches='tight')


def fit_and_predict_degrees(data):
    """
    The fit_and_predict_degrees function takes a dataset as a parameter and
    filters it according to the columns we want to use as features, then choose
    the labels as the 'total' column because that's what we want to predict.
    THis function uses many features from the scikit learn library such as
    train and test split, decition tree regressor model, and the mean mean
    squared error method.
    """
    filtered_data = data.filter(['Year', 'Min degree', 'Sex', 'Total'])
    filtered_data = filtered_data.dropna()
    features = filtered_data.loc[:, filtered_data.columns != 'Total']
    features = pd.get_dummies(features)
    labels = filtered_data['Total']
    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.2)
    model = DecisionTreeRegressor()
    model.fit(features_train, labels_train)
    test_pred = model.predict(features_test)
    test_acc = mean_squared_error(labels_test, test_pred)
    return test_acc


def main():
    data = pd.read_csv('nces-ed-attainment.csv', na_values=['---'])
    compare_bachelors_1980(data)
    top_2_2000s(data)
    line_plot_bachelors(data)
    bar_chart_high_school(data)
    plot_hispanic_min_degree(data)
    fit_and_predict_degrees(data)


if __name__ == '__main__':
    main()
