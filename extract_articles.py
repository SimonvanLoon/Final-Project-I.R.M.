#!/bin/python3

import pandas as pd
import re
import warnings
warnings.simplefilter(action='ignore', category=UserWarning)


def extract_articles():
    df = pd.read_csv('articles1.csv', sep=',', header=0)
    suitable_article_dates = df.loc[(
        "2016-04-20" <= df['date']) & (df['date'] <= "2016-11-07"), :]
    left_wing_papers = suitable_article_dates.loc[(
        df['publication'] == 'New York Times') | (df['publication'] == 'CNN'), :]
    right_wing_papers = suitable_article_dates.loc[df['publication']
                                                   == 'Breitbart', :]
    p = re.compile(r"\bTrump(\'s)*[\s\.]{1}")
    left_wing_trump = left_wing_papers.loc[left_wing_papers['title'].str.contains(
        r"\bTrump(\'s)*[\s\.]{1}", regex=True), :].sort_values(by='date')
    right_wing_trump = right_wing_papers.loc[right_wing_papers['title'].str.contains(
        r"\bTrump(\'s)*[\s\.]{1}", regex=True), :].sort_values(by='date')
    return [left_wing_trump, right_wing_trump]


def count_sentiment_words(dataframe):
    pos_words = open("unique_pos_words.txt", "r").read()
    neg_words = open("unique_neg_words.txt", "r").read()
    punctuation_marks = ".,?!:;\'\"“”’‘—()@#[]"
    pos_word_count = 0
    neg_word_count = 0
    total_word_count = 0
    for article in dataframe['content'].tolist():
        for mark in punctuation_marks:
            article = article.replace(mark, "")
        for word in article.split():
            total_word_count += 1
            word = word.lower()
            if word in pos_words:
                pos_word_count += 1
            if word in neg_words:
                neg_word_count += 1
            total_word_count += 1
            if total_word_count == 537134:
                return [total_word_count, pos_word_count, neg_word_count]


def main():
    extracted_articles = extract_articles()
    left_wing_sentiments = count_sentiment_words(extracted_articles[0])
    right_wing_sentiments = count_sentiment_words(extracted_articles[1])
    print()
    print(
        "Total amount of words in left-wing articles: {0}\n\
Amount of words with positive sentiment: {1}\n\
Amount of words with negative sentiment: {2}\n\
There are {3} more negative words than positive words \
in the left-wing articles." .format(
            left_wing_sentiments[0],
            left_wing_sentiments[1],
            left_wing_sentiments[2],
            left_wing_sentiments[2] -
            left_wing_sentiments[1]))
    print("\n----------------------------------------------------------------------\n")
    print(
        "Total amount of words in right-wing articles: {0}\n\
Amount of words with positive sentiment: {1}\n\
Amount of words with negative sentiment: {2}\n\
There are {3} more negative words than positive words \
in the right-wing articles.".format(
            right_wing_sentiments[0],
            right_wing_sentiments[1],
            right_wing_sentiments[2],
            right_wing_sentiments[2] -
            right_wing_sentiments[1]))


main()
