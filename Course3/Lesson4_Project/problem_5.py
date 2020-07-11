"""
TASK5:
Building a Trie in Python

Before we start let us reiterate the key components of a Trie or Prefix Tree.
A trie is a tree-like data structure that stores a dynamic set of strings.
Tries are commonly used to facilitate operations like predictive text or autocomplete features
on mobile phones or web search.

Before we move into the autocomplete function we need to create a working trie for storing strings.
We will create two classes:
    A Trie class that contains the root node (empty string)
    A TrieNode class that exposes the general functionality of the Trie,
    like inserting a word or finding the node which represents a prefix.


"""


# Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        self.char_nodes_dict = {}
        self.last = False

    def __str__(self):
        result = ""
        for key, value in self.char_nodes_dict.items():
            result += "{" + str(key) + ":{" + str(value) + "}}"
        return result

    def insert(self, char):
        if not self.char_nodes_dict.get(char):
            # print("1. [TrieNode]-> insert: char= " + char)
            self.char_nodes_dict[char] = TrieNode()

    '''
    Function that collects the suffix for 
    all complete words below this point.
    For example, if our Trie contains the words ["fun", "function", "factory"] and
    we ask for suffixes from the f node, we would expect 
    to receive ["un", "unction", "actory"] back.
    '''

    def suffixes(self) -> list:
        # print("[TrieNode]->suffixes: ")
        result_list = []
        tmp_suffix = ""

        for char_key, value_node in self.char_nodes_dict.items():
            self.suffixes_rec(result_list, value_node, tmp_suffix + char_key)

        return result_list

    def suffixes_rec(self, result_list, node, tmp_suffix):

        if node.last:
            result_list.append(tmp_suffix)

        for char_key, value_node in node.char_nodes_dict.items():
            tmp_suffix += char_key
            self.suffixes_rec(result_list, value_node, tmp_suffix)


# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()
        # self.words_set = set()

    def insert(self, word):
        # Add a word to the Trie
        # print("-----------------------------")
        # print("[Trie]->insert: word= " + word)
        node = self.root
        # self.words_set.add(word)

        for char_key in list(word):
            # print("char_key= " + char_key)
            node.insert(char_key)
            # print("2. root node= " + str(node))
            node = node.char_nodes_dict[char_key]
            # print("3. child node= " + str(node))
        node.last = True

    # Find the Trie node that represents this prefix
    def find(self, prefix):
        print("[TrieNode]->find: prefix= " + str(prefix))
        node = self.root
        found = True

        for char in list(prefix):
            # print("char="+char)
            if not node.char_nodes_dict.get(char):
                found = False
                print("not found!")
                break

            node = node.char_nodes_dict[char]
            # print("node= "+str(node))

        return node, found


def test_suffixes_1():
    print("--------------------------------------------")
    print("->test_suffixes_1: start")
    trie = Trie()
    word_list = [
        "ant", "anthology", "antagonist", "antonym",
        "fun", "function", "factory",
        "trie", "trigger", "trigonometry", "tripod"
    ]
    for word in word_list:
        trie.insert(word)

    prefixNode, isFound = trie.find('ant')
    print("prefixNode= " + str(prefixNode))

    assert isFound

    suffixes = prefixNode.suffixes()
    print("suffixes= " + str(suffixes))
    assert suffixes == ['hology', 'agonist', 'onym']
    print("->test_suffixes_1: end")


def test_suffixes_2():
    print("--------------------------------------------")
    print("->test_suffixes_2: start")
    trie = Trie()
    word_list = [
        "ant", "anthology", "antagonist", "antonym",
        "fun", "function", "factory",
        "trie", "trigger", "trigonometry", "tripod"
    ]
    for word in word_list:
        trie.insert(word)

    prefixNode, isFound = trie.find('f')
    print("prefixNode= " + str(prefixNode))

    assert isFound

    suffixes = prefixNode.suffixes()
    print("suffixes= " + str(suffixes))
    assert suffixes == ['un', 'unction', 'actory']
    print("->test_suffixes_2: end")


def test_find_3():
    print("--------------------------------------------")
    print("->test_find_3: start")
    trie = Trie()
    word_list = [
        "ant", "anthology", "antagonist", "antonym",
        "fun", "function", "factory",
        "trie", "trigger", "trigonometry", "tripod"
    ]
    for word in word_list:
        trie.insert(word)

    prefixNode, isFound = trie.find('g')
    assert isFound == False
    print("->test_find_3: end")


def test():
    test_suffixes_1()
    test_suffixes_2()
    test_find_3()


test()
