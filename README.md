Insight Data Engineering Coding Challenge
===

Design Decisions
---
I chose Python as my programming language of choice, as it is clean, well-documented, and most importantly, scalable.

I used a sysargv for command line file I/O, as I expected the program to be an internal tool that warrants straightforward usage.  Because of this, I had to import the `sys` and `getopt` libraries.

I also checked for the existence of an input file and output file, using the `os` library.

Incorrect usage of the script causes a help prompt to be presented, directing the user on how this program is meant to be run.  When the command-line-level usage is correct, the respective function is called.

### words_tweeted.py

Within `words_tweeted.py`, I chose a 2d list as the primary data structure.  A word and a count are grouped as two elements in a list, and these are put into another list.  I chose not to use a class structure, as the additional overhead was not worth implementing.

Each line is iteratively processed, and the count for a word is incremented after each word.  After the end of the file is reached, the 2d list is sorted by its first element, therefore alphabetically by word.  Each word and its corresponding count is written to the output file, with the count left aligned as in the example.

### median_unique.py

Similarly, `median_unique.py` does not use any classes, and goes through the same word-counting procedure as `words_tweeted.py`.  In fact, I could have combined the word-counting portion but since the two files were separated in the starter code, my assumption was that they needed to be separated in the code.  Regardless, this could be trivially combined later on.

Once the lists of words are calculated, the number of elements in each list (aka the unique words in the tweet) are put in another list, `unique`.  This is then iterated through, and for each item in `unique` a new list `seen` is made.  It is comprised of all previous elements as well as the current one.  It is sorted and the median is then found, with the middle two elements being averaged if the total count of is even.

Other
---

This was developed primarily on an Mac, partially through Linux Mint, and the last-minute tests were done on a Windows 64-bit machine.
