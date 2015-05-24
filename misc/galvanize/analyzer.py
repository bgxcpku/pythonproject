import string
from sys import argv
from collections import Counter

fname = argv[1]
with open(fname) as f:
    text = f.read()

# Convert everything to lowercase so that case
# doesn't affect word count
text = text.lower()
#word_counter = Counter()
sentences = text.split(". ")

# Set up some data structures that will
# contain information about the length 
# of sentences and the number of words in sentences.

sentence_lengths = [] # A list of numbers where `sentence_lengths[i]` 
                      # is the number of words in the i-th sentence

word_counter = dict() # A dictionary where `word_counter["the"]` is the 
                      # number of appearances of the word, "the". 

print "Sentences Detected:", len(sentences)
for i, sentence in enumerate(sentences):
    print "Analyzing sentence #", i
    print "\tSentence:", sentence
    words = sentence.split()
    n_words = len(words)
    print "\tNumber of words:", n_words
    sentence_lengths.append(n_words)
    for word in words:
        # Strip all punctuation from the words
        w = word.translate(None, string.punctuation).strip() 
        # If the word already has an entry in our our word_counter, 
        # add 1 to the running count. Otherwise, make a new 
        # entry and set the count to 1
        if w != "":
            if w in word_counter:
                word_counter[w] += 1
            else: 
                word_counter[w] = 1

total_words = sum(sentence_lengths)
total_unique_words = len(word_counter)
sentence_count = len(sentences)

print "Total words:", total_words
print "Unique words:", total_unique_words
print "Sentences:", sentence_count

# Brownie Points
avg_sentence_len = float(total_words) / sentence_count
top_words = sorted(word_counter.items(), key=lambda x: x[1], reverse=True)
print "Average sentence length:", avg_sentence_len
print "Top words:"
for word, count in top_words[:10]:
    print word, ":", count, "appearances."

