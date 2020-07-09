"""
TASK5:

"""


# Represents a single node in the Trie
class TrieNode:
    def __init__(self):
       # print("Create new TrieNode")
        self.char_nodes_dict = {}
        self.last = False

    def __str__(self):
        result = "TrieNode :  "
        for child in self.char_nodes_dict:
            result += child + "->"
        return result[:-2]

    def insert(self, char):
        # print("[TrieNode]-> insert: char= "+char)
        if not self.char_nodes_dict.get(char):
            self.char_nodes_dict[char] = TrieNode()


# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        print("[Trie]->insert: word= " + word)
        node = self.root

        for char_key in list(word):
            node.insert(char_key)
            node = node.char_nodes_dict[char_key]
            print("char_key= "+char_key+", "+str(node))
        node.last = True


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)
