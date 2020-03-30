#!/bin/bash
# S.P.C.A. van Loon / 3515710
# 30-02-2020
# final_project.sh

# Instructions: Make sure that this bash script is run in the same
# directory as 'all-the-news.zip', 'NRC-Emotion-Lexicon.zip' and 'extract_articles.py'.
# Start the script like this: $: bash final_project.sh

unzip all-the-news.zip -x
unzip NRC-Emotion-Lexicon.zip -x
mv NRC-Emotion-Lexicon-v0.92/NRC-Emotion-Lexicon-Wordlevel-v0.92.txt
grep -P 'positive\t1' NRC-Emotion-Lexicon-Wordlevel-v0.92.txt | cut -f1 > positive_words.txt # select al words with a positive score of 1
grep -P 'negative\t1' NRC-Emotion-Lexicon-Wordlevel-v0.92.txt | cut -f1 > negative_words.txt # select al words with a negative score of 1
grep -vf negative_words.txt positive_words.txt > unique_pos_words.txt # select all the lines from positive_words.txt that are not included in the negative word list. 
grep -vf positive_words.txt negative_words.txt > unique_neg_words.txt # select all the lines from negative_words.txt that are not included in the positive word list. 

python3 extract_articles.py
