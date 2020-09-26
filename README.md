# NBA Stats and Salary Analysis

## Objective
<strong>Use machine learning to predict the next big NBA star</strong>

Data analysis of NBA salaries and player stats, such as player position, minutes played per game, All Star status, biometrics, and injuries to train machine learning models to learn important factors of the most successful players to predict who the next big players will be and evaluation of players' value.

## Tools and Libraries
* Python
* Pandas, Numpy
* Sci-kit Learn
* Plotly
* JSON, CSV
* HTML, CSS
* Javascript
* Flask
* Tableau

## Datasets
* https://github.com/swar/nba_api
* https://sportsdata.io/developers/data-dictionary/nba
* http://www.espn.com/nba/salaries


## Presentation Site
https://xxxxxxxxx

***

## Analysis Details

### All-Star Achievement 
Analysis of All-Star and non All-Star players ranging from 1996 to 2018 to find correlation between All-Star achievements and player salary. Using Plotly scatter graphs confirmed that all the highest salaries were also All-Stars. We used this insight to use All-Star status as a benchmark to train and test machine learning models to predict player's success and identify which stats were most important. We ran 2 classification models from Sci-kit Learn to train and test our dataset using All-Star achievement as the target against player stats, such as games played, wins, rebounds, blocks and steals.

Decision Tree Classifier scored a 96% on test data:
<br>
![index](group_files/images/readme1.png)

Random Forest Classifier scored 97% on test data. We used Sci-Kit Learn's `feature_importances_` function to highlight which stats were the most important in predicting player's path to the All-Stars:
<br>
![index](group_files/images/readme2.png)

Link to All-Star analysis: https://xxxxxxxxx

### Health and Biometrics
xxxxx

https://xxxxxxxxx

### Injuries
xxxxx

https://xxxxxxxxx

### Salary Analysis
xxxxx

https://xxxxxxxxx
