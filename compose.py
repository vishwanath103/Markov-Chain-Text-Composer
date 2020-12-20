import string
import random
from graph import Graph, Vertex

def get_words_from_text(text_path):
    with open(text_path, 'r') as f:
        text = f.read()
        text = ' '.join(text.split())
        text = text.lower()
        text = text.translate(str.maketrans('','',string.punctuation))
    words = text.split()
    return words

def make_graph(words):
    g = Graph()

    previous_word = None

    for word in words:
        # check and add the word to the graph
        word_vertex = g.get_vertex(word)

        if previous_word:
            previous_word.increment_edge(word_vertex)

        previous_word = word_vertex

    g.generate_probability_mappings()
    return g

def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words))
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)
    return composition

def main():
    # step 1: get words from text
    words = get_words_from_text('texts/hp_sorcerer_stone.txt')
    # step 2: make a graph using those words
    g = make_graph(words)
    # step 3: get the next word for x number of words
    # step 4: show it to the user
    composition = compose(g, words, 100)
    return ' '.join(composition)

if __name__ == '__main__':
    print(main())
