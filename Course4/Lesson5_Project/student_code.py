import math
from queue import PriorityQueue


def shortest_path(graph_map, start, goal):
    print("INPUT: start==============================================================================")
    print("->shortest_path: graph_map={}, start={}, target={}".format(str(graph_map), str(start), str(goal)))
    print("intersections=\n" + str(graph_map.intersections))
    print("roads=\n" + str(graph_map.roads))
    print("INPUT: end==============================================================================\n")

    if start == goal:
        pritn("Already there")
        return [start]

    create_visitation_priority_queue(graph_map, start, goal)

    print("\n")
    return [6, 7]


def create_visitation_priority_queue(graph_map, start_index: int, goal_index: int):
    print("\n->create_visitation_priority_queue:")

    # The Python priority queue is built on the heapq module, which is basically a binary heap.
    path_priority_queue = PriorityQueue()
    path_priority_queue.put(start_index, 0)

    current_intersection_node = graph_map.intersections[start_index]
    print("Current start_index={}, node={}".format(str(start_index), str(current_intersection_node)))

    connected_nodes_list = graph_map.roads[start_index]
    print("connected_nodes_list=" + str(connected_nodes_list))

    print("\n_________")

    while True:

        for node_index in connected_nodes_list:
            print("node_index= " + str(node_index))

            # f = g + h, where g = path cost, h = esimated distance and f = total path

            path_cost_g = 0  # calculate this

            current_node_x_y = graph_map.intersections[node_index]
            print("current_node_x_y=" + str(current_node_x_y))

            # est_dist_h = get_euclidean_distance(, )

            # if path_priority_queue.get()

    print("path_priority_queue= " + str(path_priority_queue.queue))


def get_euclidean_distance(current_x_y: list, target_x_y: list):
    distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(current_x_y, target_x_y)]))
    print("->get_euclidean_distance: distance= " + str(distance))
    return distance
