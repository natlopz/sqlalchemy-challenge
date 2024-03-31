# sqlalchemy-challenge
Module 10 Challenge

## Climate Starter
1. Import dependencies
2. Create a reference to the file
3. Create .engine to hawaii.sqlite
4. Reflect an existing database into a new
5. Reflect the tables
6. View all of the classes that automap found
7. Save references to each table
8. Create our session (link) from Python to the DB
9. Find the most recent date in the data set.
10. Find the start date in the data set for FLASK APP
11. Design a query to retrieve the last 12 months of precipitation data and plot the results. Starting from the most recent data point in the database.
12. Calculate the date one year from the last date in data set.
13. Perform a query to retrieve the data and precipitation scores
14. Save the query results as a Pandas DataFrame. Explicitly set the column names
15. Sort the dataframe by date
16. Use Pandas Plotting with Matplotlib to plot the data
17. Use Pandas to calculate the summary statistics for the precipitation dat
18. Design a query to calculate the total number of stations in the dataset
19. Design a query to find the most active stations (i.e. which stations have the most rows?). List the stations and their counts in descending order.
20. Which station id has the greatest number of observations? The station ID that has the greatest number of observations is "'USC00519281' with a total of 2772 stations.
21. Using the most active station id from the previous query, calculate the lowest, highest, and average temperature.
22. Using the most active station id. Query the last 12 months of temperature observation data for this station and plot the results as a histogram
23. Converting the last date to a "datetime" object
24. Calculating the exact date 12 months ago before the last date
25. Querying the last 12 months of temp observation data for the most active station id
26. Extracting temperature observations from the query results
27. Plot!
28. Close the session

## Flask App
1. Import the dependencies.
2. Database Setup
3. Create a reference to the file
4. Create engine to hawaii.sqlite
5. Reflect an existing database into a new model
6. Reflect the tables
7. Save references to each table
8. Create our session (link) from Python to the DB
9. Flask Setup
10. def welcome():
11. def precipitation():
12. def stations():
13. def tobs():
14. def start(start):
15. def start_end(start, end):
16. Run flask app from command line
