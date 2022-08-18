# Predicting Delays for US Flights
by David Schneemann

## About the Project
### Project Goals

My goal with this project is to identify key drivers of flight delays and to provide insight into why and how these factors influence flight delays. With this information and the following recommendations, we can have a better understanding of how to avoid booking flights in the future that have a strong likelihood of producing delays. 


### Project Description

In the US, there are over 45,000 flights happening each and every day. At any given time, there are over 5000 flights in the sky at once. These vast quantities underline the importance of maintaining flights that have minimal issues and delays. However, delays do happen on a regular basis. The question is, can we predict when, where, and for how long those delays will be in the future?

In order to more accurately predict flight delays, we will analyze the attributes (features) of flights within a predetermined set of data. This dataset includes all US flights conducted during the year 2007. 
We will then develop models for predicting flight delays based on these attributes and provide recommendations and predictions for improving prediction of delays moving forward.


### Executive Summary

This report performs exploration, analysis, and modeling to predict future flight delays. \
I ask 5 initial questions of the data, creating visuals and performing statistical analysis. \
I conclude with a comparison of 3 separate regression models that analyze flight data and corresponding delays from a sample of the data. 

I then perform predictions on data not seen by these models. \
The results from my top model indicate that it will perform over 9% better than our baseline prediction on future data it has not seen. \
My conclusory summary at the end of the report highlights potential recommendations and next steps. 


### Initial Questions

#### 1. Do flights in August have higher average flight delays than than the annual average? 

#### 2. Do flights on Thursdays have higher average flight delays than the weekly average?

#### 3. Does JetBlue Airways have greater flight delays than the carrier national average?

#### 4. Does Detroit airport have greater flight delays than the overall average airport delay?

#### 5. Does total_time_diff have a relationship to flight delay?



### Data Dictionary

|Index| Variable         | Variable descriptions                                                |
|---:|:------------------|:---------------------------------------------------------------------|
|  1 | Name              | Description                                                          |
|  2 | Year              | 2007                                                                 |
|  3 | Month             | Month of the year                                                    |
|  4 | dayofmonth        | 31-Jan                                                               |
|  5 | dayofweek         | 1 (Monday) - 7 (Sunday)                                              |
|  6 | depart            | Actual departure time (local, hhmm)                                  |
|  7 | scheduled_depart  | Scheduled departure time (local, hhmm)                               |
|  8 | arrive            | Actual arrival time (local, hhmm)                                    |
|  9 | scheduled_arrive  | Scheduled arrival time (local, hhmm)                                 |
| 10 | UniqueCarrier     | Unique carrier code                                                  |
| 11 | FlightNum         | Flight number                                                        |
| 12 | TailNum           | Plane tail number                                                    |
| 13 | total_time        | Total actual time from departure to arrival (in minutes)             |
| 14 | scheduled_total_time    | Total scheduled time from departure to arrival (in minutes)    |
| 15 | AirTime           | Total time in air (in minutes)                                                           |
| 16 | ArrDelay          | Arrival delay, in minutes                                            |
| 17 | DepDelay          | Departure delay, in minutes                                          |
| 18 | Origin            | Origin IATA airport code                                             |
| 19 | Dest              | Destination IATA airport code                                        |
| 20 | Distance          | in miles                                                             |
| 21 | TaxiIn            | Taxi in time, in minutes                                             |
| 22 | TaxiOut           | Taxi out time in minutes                                             |
| 23 | Cancelled         | Was the flight cancelled?                                            |
| 25 | Diverted          | 1 = yes, 0 = no                                                      |
| 26 | CarrierDelay      | in minutes                                                           |
| 27 | WeatherDelay      | in minutes                                                           |
| 28 | NASDelay          | National Aviation System (in minutes)                                |
| 29 | SecurityDelay     | in minutes                                                           |
| 30 | LateAircraftDelay | in minutes                                                           |
| 31 | total_delay       | Total Delay (Arrival + Departure delays)                             |
| 32 | total_time_diff   | Difference between actual total time and scheduled total time        |



### Steps to Reproduce

1. You will need to visit the Harvard Dataverse website (https://dataverse.harvard.edu/)
2. Download and unzip the appropriate file for the year 2007
2. Clone my repo (including the flight_delay_acquire.py, flight_delay_prepare.py, explore.py, & scale.py) 
3. Libraries used are pandas, matplotlib, seaborn, numpy, sklearn, scipy, and model. A full list of modules with specific tools are provided in my Full Report.
4. Following these steps, you should return the exact dataset I used to in my report.


### The Plan
Below, I walk through all stages of my pipeline and process.

#### Wrangle
##### Modules (acquire.py + prepare.py)

1. Test acquire function
2. Add to acquire.py module
3. Write and test function to clean data
4. Add to prepare.py module
5. Write and test function to split data
6. Add to prepare.py module

#### Explore 
##### Modules (explore.py)

1. Ask 5 distinct questions of our data \
  a. Do flights in August have higher average flight delays than than the annual average?  \
  b. Do flights on Thursdays have higher average flight delays than the weekly average? \
  c. Does JetBlue Airways have greater flight delays than the carrier national average? \
  d. Does Detroit airport have greater flight delays than the overall average airport delay? \
  e. Does total_time_diff have a relationship to flight delay? \
2. Explore these questions through visualizations, calling explore.py as needed \
  a. Barplots are used primarily due to our features being categorical variables \
  b. For our continuous variable, lmplots with line of best fit is used \
  c. These plots illustrate a potential relationship of our chosen features with total flight delay \
3. Statistical Testing is conducted on all relevant features to determine statistical significance \
4. Summary includes key takeaways from all features explored \

#### Modeling and Evaluate
##### Modules (model.py)

1. Select Evaluation Metric: Correlation, namely RMSE
2. Scale the data utilizing our model.py scaling function
3. Evaluate a Baseline: 74 minutes (root mean square error)
4. Develop 3 distinct models
    a. Linear Regression
    b. Lasso Lars
    c. TweedieRegressor
5. Evaluate on Train and then on Validate (for promising feature sets)
6. Once a top performing model is selected, evaluate on test dataset



### Conclusion

#### Summary

In seeking solutions to more accurately predict total flight delay, we have explored a multiplicity of factors in the dataset that affect flight delays. We have shown that some potential primary drivers of flight delays are :

- The month out of the year 
- The day of the week 
- The carrier flown
- The airport one departs from
- The difference between actual total time versus scheduled total time

The correlation of these features with flight delays, combined within our analysis and models, expresses confidence in the validity of our findings. We have created robust models that perform significantly better than our baseline estimated error of 74 minutes.

Having fit the best performing model to our train, validate, and test datasets, we expect this model to perform 9.11% better than our baseline in the future on data it has not seen, given no major changes to our data source.

#### Recommendations

There are a number of recommendations that can be offered based on the above analysis. These suggestions are tied to the findings within our primary drivers of total flight delay:

1. Keep in mind the month in which a flight occurs. Certain peak travel months like August and December will almost inevitably have longer and more frequent delays than other months. 
2. The day of the week influences the potential for delay. Thursdays in particular were potentially shown to have more delays than other days of the week. 
3. The carrier chosen to fly with has particular importance for avoiding delays. For example, my statistical testing expressed confidence that Southwest Airlines have as many of fewer delays than the national carrier average despite being the biggest carrier in 2007 by a sizable margin. Inversely, JetBlue Airways has more and longer delays than the national carrier average despite being a smaller carrier with less overall flights flown.
4. The airport one flies out of does play a role in potential delays. Although this isn't necessarily a varaiable choice for most, it can inform a customer of increased potential for delays and allow them to plan accordingly.

#### Next Steps

Despite the overall effectiveness of our best-performing model, there is always room for improvement and optimization. \
If given more time to pursue a better results, I would begin by conducting further exploration and analysis of other features within our dataset. These features could include:
- The difference in actual departure time vs scheduled departure time
- A deeper analysis of delay by carrier, further extrapolating on different key carriers
- An analysis of whether the week of the month influences flight delays

In addition to exploring other features, I would look into methods for more appropriately separating our data into additional delay categories. For example:
- Breaking down total flight delay by delay segments (i.e. short, medium, and long delays)
- Analysis drawn from additional minor datasets provided
    - Namely, types and models of aircraft utilized by different carriers and their overall performance and consistency

By optimizing our dataset to include the above categories, I believe we could increase the strength of relationship of our feature set with total flight delay and improve model prediction accuracy.

