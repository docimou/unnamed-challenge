#!/usr/bin/env bash

python ./src/words_tweeted.py -i tweet_input/tweets.txt -o tweet_output/ft1.txt -q
python ./src/median_unique.py -i tweet_input/tweets.txt -o tweet_output/ft2.txt -q
