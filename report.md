## Report

This report will only cover the top level details and analysis. Please reference the main analysis notebook below for specific details

## Table of Contents
1. [Thesis](#thesis)
2. [Analysis Notebook](#analysis-notebook-link)
3. [Data Cleaning](#data-cleaning)
4. [Analysis Overview](#analysis)
5. [Graphs](#graphs)
6. [Conlusion](#future-research)
7. [Future Research](#future-research)

### Thesis

1) Does the first baron, first inhibitor, first dragon correlate to who wins the game? 

### Analysis Notebook Link

Most of the detailed analysis was done within the workbook including details on why things were complete.
[Main Python Notebook](.\main.ipynb)

### Data Cleaning

Data was gathered from the games.csv and champion_info.json and combined for easier reading

Null values were removed from the json file

Zero values were removed from the analysis dataset due to being vague on their meaning

## Analysis
Since most of these data is categorical Chi-Square and Cramer's-V was used to check correlation. 

Additional Metrics are being shown here as part of some additional analysis and correlations

Chi-Square Value Test
![Chi-Square](.\images\chi.png)

Cramer's-V Value
![cramers](.\images\cramers.png)

Hgh Chi values and low P v-values point to a clear correlation

### Graphs

To show just the percentage and chance of someone winning the game on these metrics here a is a graph on the percentage of times someone won based on the metrics measured

Chance
![chance](.\images\win-chance.png)

Correlation heat map

Correlation
![correlation](.\images\metric-correlation-map.png)

This shows the correlation between the metrics themselves, such that if you also have 

![cramers-V](.\images\cramers-graph.png)

Cramers-V values for all the metrics, you can see first inhibitor, baron, and dragon are all very highly correlated based on the metric shown. 

## Conclusion

From the graphs above there is a clear correlation between the 3 methods, first baron, first dragon, and first inhibitor. The null hypothesis is dispproven that there is no correlation between the metrics measure and winning the game.

### Future Research

I am looking to use Riot's API to grab some more recent game info and look at additional data and stats to see what indicators at the start of the game might influence the win chances between them. Hopefully also looking at some continuous data as well to track.

Here's some additional exploration from this project as well.

![additional exploration](.\images\additional-eda.png)