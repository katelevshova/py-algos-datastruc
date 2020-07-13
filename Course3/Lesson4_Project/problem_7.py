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

    def insert(self, dir_list, handler_str=''):
        node = self.root

        for dir_name in dir_list:
            print("->insert: dir_name= " + dir_name)
            node.insert(dir_name)
            print("root node= " + str(node))
            node = node.dir_nodes_dict[dir_name]
        if handler_str is not '':
            node.handler = handler_str
        print("handler= " + str(node.handler))

    def find(self, dir_list: list):
        print("->find: dir_name="+str(dir_list))
        node = self.root

        for dir_name in dir_list:
            if not node.dir_nodes_dict.get(dir_name):
                print("not found!")
                break
            node = node.dir_nodes_dict[dir_name]
            print("Found node="+str(node))
            print("handler= "+str(node.handler))

        if node.handler is None or node.handler is "":
            return "not found handler"
        else:
            return node.handler


class Router:
    def __init__(self, path_str='', handler_str=''):
        self.route_trie = RouteTrie()
        checked_path = self.dir_name_checker(path_str)
        self.route_trie.insert(self.split_path(checked_path), handler_str)

    def dir_name_checker(self, path_str):
        if path_str == "" or path_str == "/":
            return "Root"
        else:
            return path_str

    # Create a new RouteTrie for holding our routes
    # You could also add a handler for 404 page not found responses as well!
    def add_handler(self, path_str, handler_str):
        print("->add_handler: path_str= " + path_str + ", handler_str= " + handler_str)
        checked_path = self.dir_name_checker(path_str)
        self.route_trie.insert(self.split_path(checked_path), handler_str)

    # Add a handler for a path
    # You will need to split the path and pass the pass parts
    # as a list to the RouteTrie

    def lookup(self, path_str):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        checked_path = self.dir_name_checker(path_str)
        split_path_list = self.split_path(checked_path)

        '''
        if len(split_path_list) > 0:
            dir_name = split_path_list[-1]
        else:
            dir_name = split_path_list[0]

        print("root= "+str(self.route_trie.root))'''

        result_handler = self.route_trie.find(split_path_list)
        print("->lookup: result_handler= " + result_handler)
        return result_handler

    def split_path(self, path_str) -> list:
        split_path_list = [y for y in path_str.split("/") if y]
        print("split_path_list=" + str(split_path_list))
        return split_path_list


def test_root_1():
    print("------------------------------------")
    print("->test_root_1: start")
    router = Router("Root", "root handler")
    assert router.lookup("Root") == "root handler"
    assert router.lookup("Root/") == "root handler"
    assert router.lookup("/Root") == "root handler"
    assert router.lookup("/") == "root handler"
    assert router.lookup("") == "root handler"
    print("->test_root_1: end")


def test_root_2():
    print("------------------------------------")
    print("->test_root_2: start")
    router = Router("/")
    assert router.lookup("/") == "not found handler"
    router.add_handler("", "root handler")
    assert router.lookup("") == "root handler"
    print("->test_root_2: end")


def test_root_3():
    print("------------------------------------")
    print("->test_root_3: start")
    router = Router()
    router.add_handler("/home/about", "about handler")
    # case1
    print("case1:")
    actual_result = router.lookup("/home")
    expected_result = "not found handler"
    assert actual_result == expected_result, "{}, actual= '{}', expected= {}".format("case1", actual_result,
                                                                                     expected_result)
    # case2
    print("case2:")
    actual_result = router.lookup("/home/about")
    expected_result = "about handler"
    assert actual_result == expected_result, "{}, actual= '{}', expected= {}".format("case2", actual_result,
                                                                                     expected_result)
    # case3
    print("case3:")
    assert router.lookup("/home/about/") == "about handler"
    assert router.lookup("/home /about /") == "not found handler"
    assert router.lookup("/home/about/me") == "not found handler"
    print("->test_root_3: end")


def test_root_4():
    print("------------------------------------")
    print("->test_root_4: start")
    router = Router()
    router.add_handler("/home/about", "about handler")
    assert router.lookup("/home/username/group/about") == "not found handler"

    router.add_handler("/home/about/test_none_handler")
    assert router.lookup("/home/about/test_none_handler") == "not found handler"

    router.add_handler("/home/about/test_empty_handler", "")
    assert router.lookup("/home/about/test_empty_handler") == "1"

    print("->test_root_4: end")


def test():
    test_root_1()
    test_root_2()
    test_root_3()
    # test_root_4()


test()
