# [Ronan White](https://www.linkedin.com/in/ronanwhite)

# This is my portfolio to showcase some of my data analysis/science and GIS projects, hosted on Github Pages.

## [Project 1: Basic Data Visualizations and Predictions](https://github.com/rpwhite02/Portfolio/tree/main/Project%201)
* Use python libraries pandas, matplotlib, seaborn, and scikit-learn.
* Created lineplots and barplots using matplotlib and seaborn, as well as a decision tree regression model using scikit-learn.
* Based on a dataset from the National Center for Education Statistics called "Percentage of persons 25 to 29 years old with
selected levels of educational attainment, by race/ethnicity and sex: Selected years, 1920 through 2018."
* Answered questions regarding the types of degrees that percentages of people of different races and genders acquire and predicted
degree types using a decision tree regression model.
* Created and immplemented a function that creates a decision tree regressor model and predicts the total/percentage of degrees
(label) attained for a given sex, mminimum degree, and year (features). Function returns mean squared error as a basic value
to measure the model's accuracy.

![](/images/lineplot.png)
<figcaption align = "center">
  <b> Plot showing percentage of all people obtaining minimum of Bachelor's degree over time</b>
</figcaption>


![](/images/hispanicplot.png)
<figcaption align = "center">
  <b>Plot of two bars next to each other comparing the minimum degrees Hispanic people obtain</b>
</figcaption>


## [Project 2: Python Search Engine](https://github.com/rpwhite02/Portfolio/tree/main/Project%202)
* Assignment from my Data Programming class which utilized classes and objects in Python.
* Code to setup a server to host the search engine was given to the class, as well as HTML and CSS
code that set up the presentation and functionality of the search engine website.
* The document file contains the document class which represents all the data and words in a
single web page (document) and computes the term frequency for a given term in a document.
* The search engine file contains the search engine class which represents a directory of document
objects and computes the TFIDF (term frequency-inverse document frequency) score for a given
search query in each document object. In other words, this class computes how important a word
in a search query is to what the user is searching for.
* The included python code for this project is just to look through web pages and scan them for all words, as
well as calculate the importance of a word in a search query and present web pages (documents) that
correlate with the search query. Code to set up the server and website isn't included.

![](/images/searchbar.png)
<figcaption align = "center">
  <b>The search bar before entering search query</b>
</figcaption>


![](/images/searchresults.png)
<figcaption align = "center">
  <b>Suggested results after typing "computer" into the search bar</b>
</figcaption>


## [Project 3: Analyzing Ridge and LASSO Regression using scikit-learn and matplotlib](https://github.com/rpwhite02/Portfolio/tree/main/Project%203)
* Given a dataset with features such as # bedroomms, # bathrooms, square footage, year built, zip code, and more,
predict price (the label).
* Used pandas to do some feature engineering and to select features from the dataset.
* Regularized and standardized the features used so that we can meet the assumptions of the Ridge and LASSO models.
* First fit a linear regression model and obtain the root mean squared error as a baseline to compare with Ridge and
LASSO models.
* Then, move on to Ridge regression where we create a new pandas dataframe to store certain l2 penalties for our Ridge models,
the model with its alpha value (l2 penalty), the model's train root mean squared error, and the model's validation root mean squared error
using that specific l2 penalty. Below is the resulting pandas dataframe.


![](/images/ridge_data.png)
<figcaption align = "center">
  <b>The ridge data used to visualize our RMSE's as the l2 penalty changes</b>
</figcaption>


* Next, we do the same thing but for LASSO regression but with different hyperparameter choices for the l1 penalty.
Below is the resulting pandas dataframe.


![](/images/lasso_data.png)
<figcaption align = "center">
  <b>The lasso data used to visualize our RMSE's as the l1 penalty changes</b>
</figcaption>

* After we have these dataframes, we can display the observations on a plot and see how the RMSE values 
change as the l1 and l2 penalties change. Below are the plots for Ridge and LASSO.

![](/images/ridge_error_visual.png)
<figcaption align = "center">
  <b>The visual for Ridge regression</b>
</figcaption>

![](/images/lasso_error_visual.png)
<figcaption align = "center">
  <b>The visual for LASSO regression</b>
</figcaption>


## [Project 4: Web Mapping Covid Cases and Rates using HTML, CSS, and JavaScript](https://github.com/rpwhite02/Portfolio/tree/main/Project%204)
* Given shapefile (.shp) data for both case totals and rates, transform into geojson so that we can read
the data in using JavaScript
* Obtained a MapBox token so that we can have a basemap for both of our web maps, no need to create our own basemap.

![](/images/choropleth.png)

* [Map 1](https://rpwhite02.github.io/Portfolio/Project%204/map1.html) is a choropleth map that shows each U.S. county and
their COVID rates for 2020. When you hover over a specific county, their COVID rate for 2020 will come up. The population
data used for calculating each county's rate were taken from the 2018 ACS 5 year estimates.

![](/images/propsymbol.png)

* [Map 2](https://rpwhite02.github.io/Portfolio/Project%204/map2.html) is a proportional symbol map that is a good visualization
for a general overview of the distribution of COVID cases throughout the United States. The data used for this map was from The
New York Times.
