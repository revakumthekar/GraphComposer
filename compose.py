import string
import random
import re
import os

from graph import Graph, Vertex

# returns a list of words from the file


def get_words_from_text(text_path):
    with open(text_path, 'r') as f:
        text = f.read()  # returns a string

        # remove [text in here] for the song files
        text = re.sub(r'\[(.+)\]', ' ', text)

        # this is saying turn whitespace into just spaces
        text = ' '.join(text.split())

        # make everything lowercase to compare stuff
        text = text.lower()

        # remove all punctuation to make things easier
        text = text.translate(str.maketrans('', '', string.punctuation))

    # split on spaces
    words = text.split()
    return words

# creates the graph based on the words from the file


def make_graph(words):
    g = Graph()

    previous_word = None

    for word in words:

        # check that word is in the graph, and if it is not, then we add it
        word_vertex = g.get_vertex(word)

        # if there was a previous word, then add an edge if it does not already exist in the graph
        #   else increment the weight of the existing edge by 1
        if previous_word:
            previous_word.increment_edge(word_vertex)

        # set our current word to the previous word, and iterate
        previous_word = word_vertex

    # generate the probability mappings before composing it all together
    g.generate_probability_mappings()
    return g

# puts a composition of the graph based on one random word to begin with
# default of 50 words


def compose(g, words, length=50):
    composition = []

    # pick a random word to start
    word = g.get_vertex(random.choice(words))
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition


def main(artist):

    # for a book text file
    # words = get_words_from_text('texts/hp_sorcerer_stone.txt')

    # for song lyrics
    words = []
    for song_file in os.listdir(f'songs/{artist}'):
        if song_file == '.DS_Store':
            continue
        song_words = get_words_from_text(f'songs/{artist}/{song_file}')
        words.extend(song_words)

    g = make_graph(words)

    composition = compose(g, words, 100)

    # returns a string, where all the words are separated by a space
    return ' '.join(composition)


if __name__ == '__main__':
    print(main('queen'))
