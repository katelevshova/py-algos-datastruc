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
        self.dir_nodes_dict[dir_name] = RouteTrieNode()

    def __str__(self) -> str:
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
            print("     ->insert: dir_name= " + dir_name)
            node.insert(dir_name)
            print("     root node= " + str(node))
            node = node.dir_nodes_dict[dir_name]
        if handler_str is not '':
            node.handler = handler_str
        print("     handler= " + str(node.handler) + "\n")

    def find(self, dir_list) -> str:
        """
        Finds the handler for the path represented as dir_list
        :param dir_list: - list created based on the lookup path
        :return: string value of the handler
        """
        print("->find: dir_list=" + str(dir_list))
        node = self.root

        for dir_name in dir_list:
            # print("dir_name=" + str(dir_name))

            if not node.dir_nodes_dict.get(dir_name):
                print("not found!")
                return "not found handler"
            node = node.dir_nodes_dict[dir_name]
            # print("node=" + str(node))
        return self.get_handler_value(node.handler)

    def get_handler_value(self, handler_str) -> str:
        """
        Returns string handler value. If the handler value is None or "", returns "not found handler"
        :param handler_str: string
        :return: string
        """

        if handler_str is None or handler_str is "":
            return "not found handler"
        else:
            return handler_str


class Router:
    def __init__(self, path_str='', handler_str=''):
        self.route_trie = RouteTrie()
        self.add_handler(path_str, handler_str)

    def dir_name_checker(self, path_str) -> str:
        """
        Converts path to a proper format using "Root/" prefix.
        Example_1: "", "/", "Root", "Root/" are converted to "Root/"
        Example_2: "/Home" converts to "Root/Home"
        Example_3: "Home" converts to "Root/Home"
        :param path_str:
        :return: str - converted string value
        """
        if path_str == "" or path_str == "/" or path_str == "Root" or path_str == "Root/":
            return "Root/"
        elif path_str[0] == "/":
            return "Root" + path_str
        else:
            return "Root/" + path_str

    def add_handler(self, path_str='', handler_str=''):
        print("->add_handler: path_str= " + str(path_str) + ", handler_str= " + str(handler_str))

        if path_str is not None:
            checked_path = self.dir_name_checker(path_str)
            self.route_trie.insert(self.split_path(checked_path), handler_str)
        else:
            print("     path_str must be initialized! currently it's value is None.")

    def lookup(self, path_str) -> str:
        """
        Searches the path an returns the associated handler
        :param path_str: lookup path, /about and /about/ both return the /about handler
        :return handler: string
        """
        print("->lookup: path_str= " + str(path_str))
        checked_path = self.dir_name_checker(path_str)
        split_path_list = self.split_path(checked_path)
        print("root= " + str(self.route_trie.root))

        result_handler = self.route_trie.find(split_path_list)
        print("->lookup: result_handler= " + str(result_handler) + "\n")
        return result_handler

    def split_path(self, path_str) -> list:
        split_path_list = [y for y in path_str.split("/") if y]
        # print("->split_path: path_str= " + str(path_str) + ", split_path_list=" + str(split_path_list))
        return split_path_list


def test_root_1():
    print("------------------------------------")
    print("->test_root_1: START")
    router = Router("Root", "root handler")
    # case1
    print("\ncase1:")
    assert router.lookup("Root") == "root handler"
    assert router.lookup("Root/") == "root handler"
    assert router.lookup("/") == "root handler"
    assert router.lookup("") == "root handler"

    # case2
    print("\ncase2:")
    # "/Root" must create path "Root/Root" because first "/" is considered also Root
    assert router.lookup("/Root") == "not found handler"
    print("->test_root_1: END")


def test_root_2():
    print("\n------------------------------------")
    print("->test_root_2: START")
    router = Router("/")
    # case1
    print("\ncase1:")
    assert router.lookup("/") == "not found handler"
    router.add_handler("", "root handler")
    assert router.lookup("") == "root handler"

    # case2
    print("\ncase2:")
    router.add_handler("Home", "root handler")
    assert router.lookup("Home") == "root handler"

    print("->test_root_2: END")


def test_insert_to_root_1():
    print("\n------------------------------------")
    print("->test_insert_to_root_1: START")
    router = Router()
    router.add_handler("/home/about", "about handler")

    # case1
    print("\ncase1:")
    actual_result = router.lookup("/home")
    expected_result = "not found handler"
    assert actual_result == expected_result, "{}, actual= '{}', expected= {}".format("case1", actual_result,
                                                                                     expected_result)

    # case2
    print("\ncase2:")
    actual_result = router.lookup("/home/about")
    expected_result = "about handler"
    assert actual_result == expected_result, "{}, actual= '{}', expected= {}".format("case2", actual_result,
                                                                                     expected_result)

    # case3
    print("\ncase3:")
    assert router.lookup("/home/about/") == "about handler"
    assert router.lookup("/home /about /") == "not found handler"
    assert router.lookup("/home/about/me") == "not found handler"

    print("->test_insert_to_root_1: END")


def test_insert_to_root_2():
    print("\n------------------------------------")
    print("->test_insert_to_root_2: START")
    router = Router()

    # case1
    print("\ncase1:")
    router.add_handler("/home/about", "about handler")
    assert router.lookup("/home/username/group/about") == "not found handler"

    # case2
    print("\ncase2:")
    router.add_handler("/home/about/test_none_handler", None)
    assert router.lookup("/home/about/test_none_handler") == "not found handler"

    # case3
    print("\ncase3:")
    router.add_handler("/home/about/test_empty_handler", "")
    assert router.lookup("/home/about/test_empty_handler") == "not found handler"

    # case4
    print("\ncase4:")
    router.add_handler(None, None)
    assert router.lookup("/None") == "not found handler"

    print("->test_insert_to_root_2: END")


def test():
    test_root_1()
    test_root_2()
    test_insert_to_root_1()
    test_insert_to_root_2()
    print("\n======================================")
    print("ALL TESTS FINISHED SUCCESSFULLY!")


test()
