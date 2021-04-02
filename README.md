# nhl_stats_analysis [WIP]
This is still a work in progress. I have a lot of clean up and resiliency to add  
(robust unit testing, typing, getting rid of redundant lines of code, general optimization)

Summary
Scrapes NHL websites to save player stats, log matchups for the day, find injuries and starting goalies
Uses the stats to calculate a value based on a formula to represent all stats in a single number
Goalies and skaters each have different formulas

The stats and values are then used as input and output to create a scatter plot
I use linear regression to calculate a line of best fit and determine the outcome of future matches
