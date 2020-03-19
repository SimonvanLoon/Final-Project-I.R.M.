#!/bin/python3
import re
import pandas as pd

df = pd.read_csv('articles1.csv', sep=',', header=0)
news_sources = df['publication'].value_counts()
date_range = df['month'].value_counts()
print(df.shape) 
years_before_2017 = df.loc[df['year'] < 2017.0, :]
suitable_article_dates = years_before_2017.loc[df['month'] < 11.0, :]
suitable_article_dates = df.loc[("2015-06-18" <= df['date'] ) & (df['date'] <= "2016-11-07"), :] 
print(suitable_article_dates['date'].describe())
left_wing_papers = suitable_article_dates.loc[(df['publication'] == 'New York Times') | (df['publication'] == 'CNN'), :]
right_wing_papers = suitable_article_dates.loc[df['publication'] == 'Breitbart', :]
p = re.compile("\bTrump(\'s)*[\s\.]{1}")
left_wing_trump = left_wing_papers.loc[left_wing_papers['title'].str.contains(r"\bTrump(\'s)*[\s\.]{1}", regex=True), :]
right_wing_trump = right_wing_papers.loc[right_wing_papers['title'].str.contains(r"\bTrump(\'s)*[\s\.]{1}", regex=True), :]
print(left_wing_trump['date'].describe())
