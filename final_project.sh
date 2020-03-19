#!/bin/bash

# because of the great file size of each of the articles, we will analyze only the csv file with 

cat articles3.csv | grep -o 'Trump' | wc -l
