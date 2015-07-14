# median_unique.py
# author: @dmou
#
# This module takes a file as input, and creates a file as the output. The
# input file must exist, and the output file will be created if it does not
# exist, else overwritten if it does.
#
# ex.   python median_unique.py -i fileIn.txt -o fileOut.txt -q
#       python median_unique.py --help
#       python median_unique.py -i ../fileIn.txt -o ../fileOut.txt
#

import sys, getopt, os, decimal

""" The median_unique function takes a file name as input and modifies a named
    output file. It reads in each line as a tweet and parses them by word. Each
    unique word in a tweet is counted and the median number of unique words seen
    so far is then written on a new line to the output file. """
def words_tweeted(fileIn, fileOut, quiet):

    if (fileIn == ""):
        sys.exit("Please specify an input file.")
    elif (not os.path.exists(fileIn)):
        sys.exit("Input file {0} does not exist.".format(fileIn))
    if (not os.path.exists(fileOut) and not quiet):
        print("Creating new file %s." % fileOut)

    # list of number of unique words in a tweet seen so far
    unique = []

    # open file and read in each line, counting as you go
    with open(fileIn, 'r') as tweets:
        if (not quiet):
            print("Now reading from file %s..." % fileIn)
        for line in tweets:
            # determine if word has been seen before and add 1 to count if so
            # otherwise create new entry for word with count set to 1
            wordList = line.split()
            words = []
            for word in wordList:
                if word in [wordPair[0] for wordPair in words]:
                    for i in range(0, len(words)):
                        if (word == words[i][0]):
                            words[i][1] += 1
                else:
                    words.append([word, 1])

            unique.append(len(words))

    if (not quiet):
        print("Finished reading from file %s." % fileIn)
        print("Now writing from file %s..." % fileOut)

    # write running median into output file with each tweet
    with open(fileOut, 'w') as tweeted:
        # iterate through list of unique words in each tweet
        for j in range(0, len(unique)):
            total = 0
            k = 0
            # average all previous items inclusively
            while (k <= j):
                total += unique[k]
                k += 1
            average = float(total) / (j + 1)
            tweeted.write("{0:.1f}\n".format(average))

    if (not quiet):
        print("Finished writing to file %s." % fileOut)


""" Main function serving to facilitate command line parsing. """
def main():

    def usage():
        print("\
usage: words_tweeted.py -i file -o file [-h help] [-q quiet]\n\n\
Parse input file to calculate words tweeted and put results in output file.\n\n\
-i FILE      : specify FILE as input file being read from\n\
-o FILE      : specify FILE as output file being written to\n\
-q, --quiet  : suppress status updates\n\
-h, --help   : help")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hqi:o:", ["help", "quiet"])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    quiet = False
    fileIn = ""
    fileOut = ""
    for o, a in opts:
        if (o in ("-q", "--quiet")):
            quiet = True
        elif (o in ("-h", "--help")):
            usage()
            sys.exit()
        elif (o == "-i"):
            # input file
            fileIn = a
        elif (o == "-o"):
            # output file
            fileOut = a
        else:
            # unhandled case
            assert False

    words_tweeted(fileIn, fileOut, quiet)
    sys.exit(0)

if __name__ == "__main__":
    main()
