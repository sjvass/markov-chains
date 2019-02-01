"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file_string = open(file_path).read()

    return file_string


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    words = text_string.split()

    for i in range(len(words)-2):
        word_tuple = ((words[i], words[i+1]))

        if(word_tuple in list(chains.keys())):
            chains[word_tuple].append(words[i+2])
        else:
            chains[word_tuple] = [words[i+2]]

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    current_key = choice(list(chains.keys()))
    #print(current_key)

    while current_key in list(chains.keys()):
        words.append(current_key[0])
    
        new_key = (current_key[1], choice(chains[current_key]))
        current_key = new_key

    words.append(current_key[0])
    words.append(current_key[1])

    return " ".join(words)


input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)


# Get a Markov chain
chains = make_chains(input_text)

#print(chains)

# Produce random text
random_text = make_text(chains)

print(random_text)
