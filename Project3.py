import pandas as pd
import plotly.express as px

#import csv file
rawdf = pd.read_csv('movies.csv')

#clean data
cleanedDF = rawdf.dropna()
 
#MAIN QUESTION: How do Score and Budget affect Revenue in the Movie industry 1980-2019? 

#FACTOR 1: SCORE
#Question: Does movies with higher score have higher revenue? 

fig1 = px.scatter(cleanedDF, x='score', y='gross', 
                    labels={
                        'score': 'Score',
                        'gross': 'Revenue'
                    },
                    title='Gross Revenue versus Score')
fig1.show()

#FACTOR 2: BUDGET
#Question: Does movies with higher budget have higher revenue? 

fig2 = px.scatter(cleanedDF, x='budget', y='gross', opacity=0.5,
                    labels={
                        'budget': 'Budget',
                        'gross': 'Revenue'
                    },
                    title='Gross Revenue versus Budget')
fig2.show()

#Findings with Country
#Ques_1: Which country generates highest revenue in movie industry?
#First, sum up revenue of each country:
sum = cleanedDF.groupby('country')['gross'].sum().reset_index()

#Use a bar chart for Country & Revenue then rank the results in ascending order:
fig3 = px.bar(sum, x='country', y='gross', color='country',
                labels={
                    'country': 'Countries',
                    'gross': 'Revenue'
                },
                title='Revenue of each Countries')
fig3.update_layout(barmode='stack', xaxis={'categoryorder':'total ascending'})
fig3.show()

#Ques_2: Is it because the US having the highest budget?
#First, find the average budget of each country:
average = cleanedDF.groupby('country').mean().reset_index()
average = cleanedDF.groupby('country')['budget'].mean().reset_index()

#Use a bar chart for Country & Budget then rank the results in ascending order:
fig4 = px.bar(average, x='country', y='budget', color='budget',
                labels={
                    'country': 'Countries',
                    'budget': 'Budget'
                },
                title='Average Budget in Countries')
fig4.update_layout(barmode='stack', xaxis={'categoryorder':'total ascending'})
fig4.show()

#Ques_3: Is it because the US produce the highest number of movies?
#Calculate the total number of movies produced in each countries:
countUS = cleanedDF.groupby('country')['year'].count().reset_index()
countUS = countUS.sort_values('year')
renamed_US = countUS.rename(columns={'year':'No of movies'})
print(renamed_US)

#Findings with Genre
#Ques_1: Gross revenue for each genre of movies?
#Use a histogram between Genre and Revenue:
fig5 = px.histogram(cleanedDF, x='genre', y='gross',
                    labels={
                    'genre': 'Genre',
                    'gross': 'Revenue'
                    },
                    title='Gross Revenue based on Genre of movies')
fig5.show()

#Ques_2: How does the revenue vary from time to time, based on Genre?
#As data is inadequate in 2020 and after:
cleanedDF = cleanedDF.query('year <= 2019')
cleanedDF['year'] = cleanedDF['year'].apply(str)

#Aggregate numbers (revenue, score, budget) based on release year and film genre:
cleanedDF = cleanedDF.groupby(['year', 'genre']).sum().reset_index()
print(cleanedDF)

#Use line chart to show the trend:
fig6 = px.line(cleanedDF, x="year", y="gross", color='genre')
fig6.show()

#Ques_3: How many movies produced in each kind of genres?
countGE = cleanedDF.groupby('genre')['year'].count().reset_index()
countGE = countGE.sort_values('year')
renamed_GE = countGE.rename(columns={'year':'count'})
print(renamed_GE)

