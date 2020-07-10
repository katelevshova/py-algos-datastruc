"""
TASK5:

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
            print("1. [TrieNode]-> insert: char= " + char)
            self.char_nodes_dict[char] = TrieNode()

    #def find(self, char):


# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()
        self.words_set = set()

    def insert(self, word):
        # Add a word to the Trie
        print("-----------------------------")
        print("[Trie]->insert: word= " + word)
        node = self.root
        self.words_set.add(word)

        for char_key in list(word):
            print("char_key= " + char_key)
            node.insert(char_key)
            print("2. root node= " + str(node))
            node = node.char_nodes_dict[char_key]
            print("3. child node= " + str(node))
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
                break

            node = node.char_nodes_dict[char]
            # print("node= "+str(node))

        return node, found


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

prefixNode, isFound = MyTrie.find('ant')
print("prefixNode= " + str(prefixNode))
print("isFound= " + str(isFound))

