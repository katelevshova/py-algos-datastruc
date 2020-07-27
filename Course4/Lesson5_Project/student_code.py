import math
from queue import PriorityQueue

'''
class Node:
    def __init__(self, _parent=None, _index=None):
        self.parent = _parent
        self.index = _index
        self.path_cost_g = 0
        self.est_dist_h = 0
        self.total_path_f = 0
        self.x_y = [None, None]

    def __eq__(self, other):
        return other.total_path_f == self.total_path_f

    def __lt__(self, other):
        return other.total_path_f < self.total_path_f

    def __gt__(self, other):
        return other.total_path_f > self.total_path_f

    def __str__(self):
        return "Node: i= " + str(self.index) + ", g= " + str(self.path_cost_g) + ", h= " + str(
            self.est_dist_h) + ", f= " + str(self.total_path_f) + ", x_y= " + str(self.x_y)
'''


def shortest_path(graph_map, start_index, target_index):
    print("INPUT: start==============================================================================")
    print("->shortest_path: graph_map={}, start_index={}, target={}".format(str(graph_map), str(start_index),
                                                                            str(target_index)))
    print("intersections=\n" + str(graph_map.intersections))
    print("roads= ")
    print(*graph_map.roads, sep="\n")
    print("INPUT: end==============================================================================\n")

    if start_index == target_index:
        print("Already there")
        return [start_index]

    # Create start and target nodes
    # start_node = Node(None, start_index)
    # start_node.x_y = graph_map.intersections[start_index]
    # target_node = Node(None, target_index)
    # target_node.x_y = graph_map.intersections[target_index]

    result_list = perform_a_star(graph_map, start_index, target_index)
    print("\n")
    return result_list


def perform_a_star(graph_map, start_node_index: int, target_node_index: int) -> list:
    print("\n->perform_a_star:")

    # The Python priority queue is built on the heapq module, which is basically a binary heap.
    # Entries are typically tuples of the form:  (priority number, data).
    path_priority_queue = PriorityQueue()
    path_priority_queue.put(start_node_index, 0)  # total_f is 0 for start

    prev_total_f_dict = dict()
    prev_total_f_dict[start_node_index] = None
    total_f_dict = dict()
    total_f_dict[start_node_index] = 0

    print("start_node_index={}, target_node_index={}".format(start_node_index, target_node_index))
    result_path = []

    print("===================================")

    while not path_priority_queue.empty():
        current_node_index = path_priority_queue.get()  # returns and deletes the smallest item
        print("CURRENT NODE index:" + str(current_node_index))
        current_node_x_y = graph_map.intersections[current_node_index]

        connected_nodes_list = graph_map.roads[current_node_index]
        print("connected_nodes_list=" + str(connected_nodes_list))

        for node_index in connected_nodes_list:
            print("-------------node_index:= " + str(node_index))

            if current_node_index == target_node_index:
                print("     >>>>>>REACHED TARGET>>>>>>")
                result_path = create_path(prev_total_f_dict, start_node_index, target_node_index)

            # f = g + h, where g = path cost, h = estimated distance and f = total path

            connected_node_x_y = graph_map.intersections[node_index]
            print("connected_node_x_y " + str(connected_node_x_y))

            distance_curr_to_connected = get_euclidean_distance(current_node_x_y, connected_node_x_y)
            print("distance_curr_to_connected=" + str(distance_curr_to_connected))

            print("total_f_dict["+str(current_node_index)+"]= " + str(total_f_dict[current_node_index]))
            updated_path_cost_g = total_f_dict[current_node_index] + distance_curr_to_connected
            prev_path_cost_g = total_f_dict[current_node_index]
            print("updated_path_cost_g=" + str(updated_path_cost_g), ", prev_path_cost_g=" + str(prev_path_cost_g))

            print("total_f_dict="+str(total_f_dict))

            is_not_visited = (node_index not in total_f_dict)
            print("is_not_visited=" + str(is_not_visited))
            is_lesser_distance = (updated_path_cost_g < prev_path_cost_g)
            print("is_lesser_distance=" + str(is_lesser_distance))

            # if not visited yet OR
            # the node is visited but the distance from the starting node is less
            # than the distance stored previously for this node
            if is_not_visited or is_lesser_distance:
                print("UPDATE")
                total_f_dict[node_index] = updated_path_cost_g

                target_node_x_y = graph_map.intersections[target_node_index]
                est_dist_h = get_euclidean_distance(connected_node_x_y, target_node_x_y)
                total_path_f = updated_path_cost_g + est_dist_h
                path_priority_queue.put(node_index, total_path_f)

                prev_total_f_dict[node_index] = current_node_index
            else:
                print("Do nothing...")
    return result_path


def search_queue(index: int, _queue: PriorityQueue) -> bool:
    while not _queue.empty():
        val_tuple = _queue.get()
        print("val_tuple= " + str(val_tuple) + ", index=" + str(index))
        if val_tuple[0] == index:
            return True
    return False


def print_queue(_queue):
    print("->print_queue:")
    for item in _queue.queue:
        print(item)


def get_euclidean_distance(current_x_y: list, target_x_y: list):
    distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(current_x_y, target_x_y)]))
    # print("->get_euclidean_distance: distance= "+str(distance))
    return distance


def create_path(prev, start, target) -> list:
    print("->create_path: ")
    curr = target
    path = [curr]
    while curr != start:
        curr = prev[curr]
        path.append(curr)
    path.reverse()
    print("path=" + str(path))
    return path


# -----------------TESTING-------------------------------------------------------------------------------------------

class graph_map:
    intersections = {0: [0.7801603911549438, 0.49474860768712914], 1: [0.5249831588690298, 0.14953665513987202],
                     2: [0.8085335344099086, 0.7696330846542071], 3: [0.2599134798656856, 0.14485659826020547],
                     4: [0.7353838928272886, 0.8089961609345658], 5: [0.09088671576431506, 0.7222846879290787],
                     6: [0.313999018186756, 0.01876171413125327], 7: [0.6824813442515916, 0.8016111783687677],
                     8: [0.20128789391122526, 0.43196344222361227], 9: [0.8551947714242674, 0.9011339078096633],
                     10: [0.7581736589784409, 0.24026772497187532], 11: [0.25311953895059136, 0.10321622277398101],
                     12: [0.4813859169876731, 0.5006237737207431], 13: [0.9112422509614865, 0.1839028760606296],
                     14: [0.04580558670435442, 0.5886703168399895], 15: [0.4582523173083307, 0.1735506267461867],
                     16: [0.12939557977525573, 0.690016328140396], 17: [0.607698913404794, 0.362322730884702],
                     18: [0.719569201584275, 0.13985272363426526], 19: [0.8860336256842246, 0.891868301175821],
                     20: [0.4238357358399233, 0.026771817842421997], 21: [0.8252497121120052, 0.9532681441921305],
                     22: [0.47415009287034726, 0.7353428557575755], 23: [0.26253385360950576, 0.9768234503830939],
                     24: [0.9363713903322148, 0.13022993020357043], 25: [0.6243437191127235, 0.21665962402659544],
                     26: [0.5572917679006295, 0.2083567880838434], 27: [0.7482655725962591, 0.12631654071213483],
                     28: [0.6435799740880603, 0.5488515965193208], 29: [0.34509802713919313, 0.8800306496459869],
                     30: [0.021423673670808885, 0.4666482714834408], 31: [0.640952694324525, 0.3232711412508066],
                     32: [0.17440205342790494, 0.9528527425842739], 33: [0.1332965908314021, 0.3996510641743197],
                     34: [0.583993110207876, 0.42704536740474663], 35: [0.3073865727705063, 0.09186645974288632],
                     36: [0.740625863119245, 0.68128520136847], 37: [0.3345284735051981, 0.6569436279895382],
                     38: [0.17972981733780147, 0.999395685828547], 39: [0.6315322816286787, 0.7311657634689946]}
    roads = [[36, 34, 31, 28, 17], [35, 31, 27, 26, 25, 20, 18, 17, 15, 6], [39, 36, 21, 19, 9, 7, 4],
             [35, 20, 15, 11, 6], [39, 36, 21, 19, 9, 7, 2], [32, 16, 14], [35, 20, 15, 11, 1, 3],
             [39, 36, 22, 21, 19, 9, 2, 4], [33, 30, 14], [36, 21, 19, 2, 4, 7], [31, 27, 26, 25, 24, 18, 17, 13],
             [35, 20, 15, 3, 6], [37, 34, 31, 28, 22, 17], [27, 24, 18, 10], [33, 30, 16, 5, 8],
             [35, 31, 26, 25, 20, 17, 1, 3, 6, 11], [37, 30, 5, 14], [34, 31, 28, 26, 25, 18, 0, 1, 10, 12, 15],
             [31, 27, 26, 25, 24, 1, 10, 13, 17], [21, 2, 4, 7, 9], [35, 26, 1, 3, 6, 11, 15], [2, 4, 7, 9, 19],
             [39, 37, 29, 7, 12], [38, 32, 29], [27, 10, 13, 18], [34, 31, 27, 26, 1, 10, 15, 17, 18],
             [34, 31, 27, 1, 10, 15, 17, 18, 20, 25], [31, 1, 10, 13, 18, 24, 25, 26], [39, 36, 34, 31, 0, 12, 17],
             [38, 37, 32, 22, 23], [33, 8, 14, 16], [34, 0, 1, 10, 12, 15, 17, 18, 25, 26, 27, 28], [38, 5, 23, 29],
             [8, 14, 30], [0, 12, 17, 25, 26, 28, 31], [1, 3, 6, 11, 15, 20], [39, 0, 2, 4, 7, 9, 28], [12, 16, 22, 29],
             [23, 29, 32], [2, 4, 7, 22, 28, 36]]


def test_1():
    print("->test_1: start-------------------------------")
    actual_path = shortest_path(graph_map, 5, 34)
    expected_path = [5, 16, 37, 12, 34]
    print("actual_path=   {} \nexpected_path= {}".format(actual_path, expected_path))
    assert actual_path == expected_path
    print("->test_1: end-------------------------------")


def test_2():
    print("->test_2: start-------------------------------")
    actual_path = shortest_path(graph_map, 5, 16)
    expected_path = [5, 16]
    print("actual_path=   {} \nexpected_path= {}".format(actual_path, expected_path))
    assert actual_path == expected_path
    print("->test_2: end-------------------------------")


def test_3():
    print("->test_3: start-------------------------------")
    actual_path = shortest_path(graph_map, 5, 37)
    expected_path = [5, 16, 37]
    print("actual_path=   {} \nexpected_path= {}".format(actual_path, expected_path))
    assert actual_path == expected_path
    print("->test_3: end-------------------------------")


def test_4():
    print("->test_4: start-------------------------------")
    actual_path = shortest_path(graph_map, 5, 12)
    expected_path = [5, 16, 37, 12]
    print("actual_path=   {} \nexpected_path= {}".format(actual_path, expected_path))
    assert actual_path == expected_path
    print("->test_4: end-------------------------------")


def test():
    # test_1()
    # test_2()
    # test_3()
    test_4()


test()
