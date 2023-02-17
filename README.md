# Ronan White

# [Project 1: Data Visualizations and Predictions](https://github.com/rpwhite02/Portfolio/tree/main/Project%201)
* Use python libraries pandas, matplotlib, seaborn, and scikit-learn.
* Created lineplots and barplots using matplotlib and seaborn, as well as a decision tree regression model using scikit-learn.
* Based on a dataset from the National Center for Education Statistics called "Percentage of persons 25 to 29 years old with
selected levels of educational attainment, by race/ethnicity and sex: Selected years, 1920 through 2018."
* Answered questions regarding the types of degrees that percentages of people of different races and genders acquire and predicted
degree types using a decision tree regression model.

![](/images/lineplot.png)
<figcaption align = "center">
  <b> Plot showing percentage of all people obtaining minimum of Bachelor's degree over time</b>
</figcaption>


![](/images/hispanicplot.png)
<figcaption align = "center">
  <b>Plot of two bars next to each other comparing the minimum degrees Hispanic people obtain</b>
</figcaption>


# [Project 2: Python Search Engine](https://github.com/rpwhite02/Portfolio/tree/main/Project%202)
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


# [Project 3: Analyzing Ridge and LASSO Regression using scikit-learn and matplotlib](https://github.com/rpwhite02/Portfolio/tree/main/Project%203)
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


* Next, we do the same thing but for LASSO regression. Below is the resulting pandas dataframe.


![](/images/lasso_data.png)
<figcaption align = "center">
  <b>The lasso data used to visualize our RMSE's as the l1 penalty changes</b>
</figcaption>

* After we have these dataframes, we can plot how the RMSE values change as the l1 and l2 penalties
change. Below are the plots for Ridge and LASSO.

![](/images/ridge_error_visual.png)
<figcaption align = "center">
  <b>The visual for Ridge regression</b>
</figcaption>


![](/images/lasso_error_visual.png)
<figcaption align = "center">
  <b>The visual for LASSO regression</b>
</figcaption>
