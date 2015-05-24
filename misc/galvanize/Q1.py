"""
From the Galvanize problem set: 

The challenge is to create a text content analyzer. This is a tool used by writers to find statistics such as word and sentence count on essays or articles they are writing.
Write a Python program that analyzes input from a file and compiles statistics on it.
The program should output:
    1. The total word count
    2. The count of unique words
    3. The number of sentences
    Example output:

    Total word count: 468
    Unique words: 223
    Sentences: 38
    Brownie points will be awarded for the following extras:
    1. The ability to calculate the average sentence length in words
    2. The ability to find often used phrases (a phrase of 3 or more words used over 3 times)
    3. A list of words used, in order of descending frequency
    4. The ability to accept input from STDIN, or from a file specified on the command line.

I broke this up into an unnecessary amount of (somewhat useless) functions, 
which may or may not be useful for you to get an idea of we can use functions
to break up functionality into small, useful pieces (functions) that we can 
re-use. 
"""

def read_file_str(fname):
    """
    Reads the contents of the file at path `fname` and returns
    contents as string
    """
    with open(fname) as f:
        return f.read()

def sentences(text, sep=". "):
    """
    Splits text into sentences according to `sep`. The default 
    separator will be ". ". So if you don't give a second argument
    to this function, we assume that sentences are separated by 
    a period followed by a space. 
    """
    return text.split(sep)

def words(sentence, sep=" "):
    """
    Splits the string, `sentence` into words.
    """
    return sentence.split(sep)

def word_count(sentence, sep=" "):
    """
    Returns the number of words in the given sentence
    """
    word_list = words(sentence, sep=sep)
    return len(word_list)

def unique_words(sentence, sep=" "):
    """
    Gets a set of unique words from sentence
    """
    word_list = words(sentence, sep=sep)
    return set(word_list)

def n_unique_words(sentence, sep=" "):
    """
    Returns the number of unique words in the sentence
    """
    return len(unique_words(sentence, sep=sep))

def sentence_count(text, sep=". "):
    """
    Returns the number of sentenes in the text
    """
    return len(sentences(text, sep=sep))

def analyze(text, sentence_sep=". ", word_sep=" "):
    """
    Returns the word count, unique word count, and number of sentences
    in text
    """

    wc = word_count(text, sep=word_sep)
    sc = sentence_count(text, sep=sentence_sep) 
    unique_wc = n_unique_words(text)
    return wc, sc, unique_wc

if __name__ == "__main__":
    
    # sys.argv is builtin Python module (part of the standard Python library)
    # which allows you to read in arguments from the commad line as a list.
    # If we run `python Q1.py somefile.txt` from the command line, argv
    # wil be the list ["Q1.py", "somefile.txt"]
    from sys import argv
    fname = argv[1]
    wc, sc, uwc = analyze(read_file_str(fname))
    print "Word Count:", wc
    print "Sentence Count:", sc
    print "Unique Word Count:", uwc
    
