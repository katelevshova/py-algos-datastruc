"""
TASK7:
HTTPRouter using a Trie

For this exercise we are going to implement an HTTPRouter like you would find in
a typical web server using the Trie data structure we learned previously.

There are many different implementations of HTTP Routers such as regular expressions
or simple string matching, but the Trie is an excellent and very efficient data structure for this purpose.

The purpose of an HTTP Router is to take a
URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what
content to return. In a dynamic web server, the content will often come from a block of code called a handler.

A Trie with a single path entry of: "/about/me" would look like:
(root, None) -> ("about", None) -> ("me", "About Me handler")
"""


class RouteTrieNode:
    def __init__(self):
        self.dir_nodes_dict = {}
        self.handler = None

    def insert(self, dir_name):
        if not self.dir_nodes_dict.get(dir_name):
            self.dir_nodes_dict[dir_name] = RouteTrieNode()

    def __str__(self):
        result = ""
        for key, value in self.dir_nodes_dict.items():
            result += "{" + str(key) + ":{" + str(value) + "}}"
        return result


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()

    def insert(self, dir_list):
        node = self.root

        for dir_name in dir_list:
            print("dir_name= " + dir_name)
            node.insert(dir_name)
            print("2. root node= " + str(node))
            node = node.dir_nodes_dict[dir_name]

    def find(self, dir_name):
        if self.root.dir_nodes_dict.get(dir_name):
            return self.root.dir_nodes_dict[dir_name].handler
        else:
            return "not found handler"


class Router:
    def __init__(self, path, handler):
        self.route_trie = RouteTrie()

    # Create a new RouteTrie for holding our routes
    # You could also add a handler for 404 page not found responses as well!
    def add_handler(self, path_str, handler_str):
        print("->add_handler: path_str= "+path_str+", handler_str= "+handler_str)
        self.route_trie.insert(self.split_path(path_str))

    # Add a handler for a path
    # You will need to split the path and pass the pass parts
    # as a list to the RouteTrie

    def lookup(self, path_str):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        result_handler = self.route_trie.find(self.split_path(path_str)[-1])
        print("result_handler= "+result_handler)
        return result_handler


    def split_path(self, path_str) -> list:
        split_path_list = [y for y in path_str.split("/") if y]
        print("split_path_list=" + str(split_path_list))
        return split_path_list


def test_1():
    print("------------------------------------")
    print("->test_1: start")
    router = Router()
    assert router.lookup("/") == "not found handler"

    print("->test_1: end")


def test():
    test_1()


test()
