"""Generate Markov text from text files."""

from random import choice
import sys



def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file_string = open(file_path).read()

    return file_string


# def make_key(i, gram_num,words):
#     return tuple([words[j] for j in range(i, i + gram_num)])

def make_chains(text_string, gram_num):
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

    #dict_variable = {key:value for (key,value) in dictonary.items()}
    # your code goes here
    words = text_string.split()


    # chains = { make_key(i, gram_num,words):
    #    (chains[make_key(i, gram_num,words)].append(words[i+gram_num])
    #     if make_key(i, gram_num,words) in list(chains.keys())
    #     else [words[i+gram_num]])
    #     for i in range(len(words)- gram_num)}

    #word_list_comp = [words[j] for j in range(i, i + gram_num)]


    

    for i in range(len(words)-gram_num):
       # print("i = ", i)
        #j = i
        word_list = []
        for j in range(i, i + gram_num):
            #print("j = ", j)
            word_list.append(words[j])
        word_tuple = tuple(word_list)

        if(word_tuple in list(chains.keys())):
            chains[word_tuple].append(words[i+gram_num])
        else:
            chains[word_tuple] = [words[i+gram_num]]


    # for i in range(len(words)-2):
    #     word_tuple = ((words[i], words[i+1]))

    #     if(word_tuple in list(chains.keys())):
    #         chains[word_tuple].append(words[i+2])
    #     else:
    #         chains[word_tuple] = [words[i+2]]


    return chains


def make_text(chains, gram_num):
    """Return text from chains."""

    words = []

    # your code goes here
    current_key = choice(list(chains.keys()))
    
    while not current_key[0][0].isupper():
        current_key = choice(list(chains.keys()))

    while current_key in list(chains.keys()):
        words.append(current_key[0])

        new_key_list = []
        for i in range(1, gram_num):
           # print("i = ", i)
            new_key_list.append(current_key[i])
        new_key_list.append(choice(chains[current_key]))

        current_key = tuple(new_key_list)



    # print(current_key)

    # while current_key in list(chains.keys()):
    #     words.append(current_key[0])

    #     new_key = (current_key[1], choice(chains[current_key]))
    #     current_key = new_key

    # words.append(current_key[0])
    # words.append(current_key[1])

    #     words.append(word)
    for j in range(0, gram_num):
        words.append(current_key[j])

    return " ".join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

gram_num = 2

# Get a Markov chain
chains = make_chains(input_text, gram_num)

print(chains)

# Produce random text
random_text = make_text(chains, gram_num)

print(random_text)
