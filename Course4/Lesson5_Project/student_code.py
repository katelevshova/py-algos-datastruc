from queue import PriorityQueue
import math


def shortest_path(graph_map, start, goal):
    print("INPUT: start==============================================================================")
    print("->shortest_path: graph_map={}, start={}, target={}".format(str(graph_map), str(start), str(goal)))
    print("intersections=\n" + str(graph_map.intersections))
    print("roads=\n" + str(graph_map.roads))
    print("INPUT: end==============================================================================\n")

    if start == goal:
        pritn("Already there")
        return [start]

    perform_a_star(graph_map, start, goal)

    print("\n")
    return [6, 7]


def perform_a_star(graph_map, start_index: int, goal_index: int):
    print("\n->perform_a_star:")

    # The Python priority queue is built on the heapq module, which is basically a binary heap.
    path_priority_queue = PriorityQueue()
    path_priority_queue.put(start_index, 0)

    print("start_index=" + str(start_index) + ", goal_index=" + str(goal_index))

    print("____________________________________________")

    while not path_priority_queue.empty():
        current_node_index = path_priority_queue.get()  # path_priority_queue.queue[0]
        print("current_node_index=" + str(current_node_index))

        if current_node_index == goal_index:
            create_path()

        connected_nodes_list = graph_map.roads[current_node_index]
        print("connected_nodes_list=" + str(connected_nodes_list))

        print("\n")

        # f = g + h, where g = path cost, h = esimated distance and f = total path
        current_node_x_y = graph_map.intersections[current_node_index]
        target_node_x_y = graph_map.intersections[goal_index]
        # print("target_node_x_y="+str(target_node_x_y))
        est_dist_h = get_euclidean_distance(current_node_x_y, target_node_x_y)

        for node_index in connected_nodes_list:
            print("-------------")
            print("node_index= " + str(node_index))

            connected_node_x_y = graph_map.intersections[node_index]
            path_cost_g = get_euclidean_distance(current_node_x_y, connected_node_x_y)
            print("path_cost_g=" + str(path_cost_g))
            print("est_dist_h=" + str(est_dist_h))
            total_path_f = path_cost_g + est_dist_h
            print("total_path_f=" + str(total_path_f))

    print("path_priority_queue= " + str(path_priority_queue.queue))


def get_euclidean_distance(current_x_y: list, target_x_y: list):
    distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(current_x_y, target_x_y)]))
    # print("->get_euclidean_distance: distance= "+str(distance))
    return distance







