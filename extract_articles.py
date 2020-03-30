#!/bin/python3

import pandas as pd
import re
import warnings
warnings.simplefilter(action='ignore', category=UserWarning)


def extract_articles():
    df = pd.read_csv('articles1.csv', sep=',', header=0)
    suitable_article_dates = df.loc[(  # select suitable article dates
        "2016-05-10" <= df['date']) & (df['date'] <= "2016-11-07"), :]
    left_wing_papers = suitable_article_dates.loc[(  # select articles with either The New York Times or CNN as publisher
        df['publication'] == 'New York Times') | (df['publication'] == 'CNN'), :]
    right_wing_papers = suitable_article_dates.loc[df['publication']  # select articles with Breitbart as publisher
                                                   == 'Breitbart', :]
    p = re.compile(r"\bTrump(\'s)*[\s\.]{1}")
    left_wing_trump = left_wing_papers.loc[left_wing_papers['title'].str.contains(  # select articles with contain the regex in the title column
        r"\bTrump(\'s)*[\s\.]{1}", regex=True), :].sort_values(by='date').head(600)
    right_wing_trump = (right_wing_papers.loc[right_wing_papers['title'].str.contains(
        r"\bTrump(\'s)*[\s\.]{1}", regex=True), :].sort_values(by='date')).loc[::2, :].head(600)  # take every 2nd article of the Breitbart articles
    return [left_wing_trump, right_wing_trump]


def count_sentiment_articles(dataframe):
    pos_words = open("unique_pos_words.txt", "r").read()
    neg_words = open("unique_neg_words.txt", "r").read()
    punctuation_marks = ".,?!:;\'\"“”’‘—()@#[]"
    pos_article_count = 0
    neg_article_count = 0
    total_word_count = 0
    for article in dataframe['content'].tolist():
        pos_word_count = 0
        neg_word_count = 0
        for mark in punctuation_marks:
            article = article.replace(mark, "")
        for word in article.split():
            word = word.lower()
            if word in pos_words:
                pos_word_count += 1
            if word in neg_words:
                neg_word_count += 1
        if pos_word_count > neg_word_count:
            pos_article_count += 1
        if neg_word_count > pos_word_count:
            neg_article_count += 1
    return [pos_article_count, neg_article_count]


def main():
    extracted_articles_df = extract_articles()
    left_wing_sentiments = count_sentiment_articles(extracted_articles_df[0])
    right_wing_sentiments = count_sentiment_articles(extracted_articles_df[1])
    print()
    print(
        "Total amount of left-wing articles about Trump with an overall positive sentiment: {0}\n\
Total amount of right-wing articles about Trump with an overall positive sentiment: {1}\n\n\
Total amount of left-wing articles about Trump with an overall negative sentiment: {2}\n\
Total amount of right-wing articles about Trump with an overall negative sentiment: {3}".format(
            left_wing_sentiments[0],
            right_wing_sentiments[0],
            left_wing_sentiments[1],
            right_wing_sentiments[1]))


main()
