# words_tweeted.py
# author: @dmou
#
# This module takes a file as input, and creates a file as the output. The
# input file must exist, and the output file will be created if it does not
# exist, else overwritten if it does.
#
# ex.   python words_tweeted.py -i fileIn.txt -o fileOut.txt -q
#       python words_tweeted.py --help
#       python words_tweeted.py -i ../fileIn.txt -o ../fileOut.txt
#
# TODO: create justification for design decisions

import sys, getopt, os

""" The words_tweeted function takes a file name as input and modifies a named
    output file. It reads in each line as a tweet and parses them by word. Each
    word is associated with a count, and the output file lists a word and its
    associated count on each line, sorted alphabetically. """
def words_tweeted(fileIn, fileOut, quiet):

    if (fileIn == ""):
        sys.exit("Please specify an input file.")
    elif (not os.path.exists(fileIn)):
        sys.exit("Input file {0} does not exist.".format(fileIn))
    if (not os.path.exists(fileOut) and not quiet):
        print("Creating new file %s." % fileOut)

    # list of lists with first element as the word and second as the count
    words = []

    # open file and read in each line, counting as you go
    with open(fileIn, 'r') as tweets:
        if (not quiet):
            print("Now reading from file %s..." % fileIn)
        for line in tweets:
            wordList = line.split()
            # determine if word has been seen before and add 1 to count if so
            # otherwise create new entry for word with count set to 1
            for word in wordList:
                if word in [wordPair[0] for wordPair in words]:
                    for i in range(0, len(words)):
                        if (word == words[i][0]):
                            words[i][1] += 1
                else:
                    words.append([word, 1])

    # sort this list by word alphabetically
    words.sort(key = lambda x: x[0])

    if (not quiet):
        print("Finished reading from file %s." % fileIn)
        print("Now writing from file %s..." % fileOut)

    with open(fileOut, 'w') as tweeted:
        for j in words:
            tweeted.write("{0:28} {1}\n".format(j[0], j[1]))

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
