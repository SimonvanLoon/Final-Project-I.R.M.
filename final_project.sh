#!/bin/bash

# because of the great file size of each of the articles, we will analyze only the csv file with 

#echo "There are `grep -P 'positive\t1' NRC-Emotion-Lexicon-Wordlevel-v0.92.txt | wc -l` words with a positive connotation,
#and `grep -P 'negative\t1' NRC-Emotion-Lexicon-Wordlevel-v0.92.txt | wc -l` words with a negative connotation."

#grep -P '[(posi)(nega)]tive\t1' NRC-Emotion-Lexicon-Wordlevel-v0.92.txt > short_lexicon.txt

grep -P 'positive\t1' NRC-Emotion-Lexicon-Wordlevel-v0.92.txt | cut -f1 > positive_words.txt

grep -P 'negative\t1' NRC-Emotion-Lexicon-Wordlevel-v0.92.txt | cut -f1 > negative_words.txt

grep -vf negative_words.txt positive_words.txt > unique_pos_words.txt # select all the lines from positive_words.txt that are not included in the negative word list. 
grep -vf positive_words.txt negative_words.txt > unique_neg_words.txt # select all the lines from negative_words.txt that are not included in the positive word list. 
