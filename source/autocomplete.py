# Assume the file is txt
# Preprocess the file: split and store the data into array
import string
import time

# Solution 1 w/ small data to test
database = ["abracadara", "al", "alice", "alicia",
            "allen", "alter", "altercation", "bob",
            "eve", "evening", "event", "eventually", "mallory"]

def sol_1(char, word_list):
    check_str = [d for d in word_list if d.startswith(char)]
    # print(check_str)

class Trie_Node(object):

    def __init__(self, data, ended=False):
        self.data = (data, ended)
        self.children = {}


class Trie(object):

    def __init__(self):
        self.root = Trie_Node("")

    # def find_parent(self, word, parent=None):
    #     parent = self.root
    #     next_child = None
    #     # children = self.children
    #
    #     if next_child is None:
    #         return parent
    #     else:
    #         for w in range(len(word)):
    #             for child in parent.children:
    #                 print(child)
    #                 if word[w] == parent.children:
    #                     parent = parent.children[word[w]]
    #                     next_child = word[w+1]
    #                     find_parent(word, parent, next_child)


    def insert(self, word):
        parent = self.root
        characters = parent.data[0]
        for i in range(len(word)):
            if word[i] in parent.children:
                parent = parent.children[word[i]]
                characters += word[i]
            else:
                characters += word[i]
                ended = False
                if i == len(word) - 1:
                    ended = True
                parent.children[word[i]] = Trie_Node(characters, ended)



def find_prefix(trie, prefix):
    node = trie.root
    for p in prefix:
        node = node.children[p]
    return node.children

def find_words(nodes, words=[]):
    for char in nodes:
        if nodes[char].data[1]:
            words.append(nodes[char].data[0])
    return words

def find_all_words(trie, prefix):
    nodes = find_prefix(trie, prefix)
    all_words = find_words(nodes)
    return all_words

def get_words(filename):
    opened_file = open(filename)
    words = opened_file.read().split()
    return words

def store_word(words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    return trie

# def autocomplete_trie():


def benchmark(prefixes):
    start_time = time.time()
    filename = "/usr/share/dict/words"
    words = get_words(filename)
    # trie = Trie()
    # for word in all_words:
    #     trie.insert(word)
    # # return trie
    trie = store_word(words)
    for prefix in prefixes:
        find_all_words(trie, prefix)
    end_time = time.time()
    return end_time - start_time

# Benchmarks:
# 1) sol_1: 2663.87 sec ==  44 min



def main():
    all_words = get_words('/usr/share/dict/words')
    all_prefixes = set([word[:len(word)//2] for word in all_words])
    # # print(all_words)
    time = benchmark(all_prefixes)
    print('Took {} seconds to benchmark {} prefixes on {} words'.format(time, len(all_prefixes), len(all_words)))

if __name__ == '__main__':
    main()
