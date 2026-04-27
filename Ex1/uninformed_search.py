from collections import deque
import heapq as h
class Graph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []
            print(f"Node '{node}' added.")
        else:
            print(f"Node '{node}' already exists.")
    def add_edge(self, u, v, cost=0):
        if u in self.graph and v in self.graph:
            if any(neighbor == v for neighbor, _ in self.graph[u]):
                print(f"Edge from '{u}' to '{v}' already exists.")
            else:
                self.graph[u].append((v, cost))
                if not self.directed:
                    self.graph[v].append((u, cost))
                print(f"Edge added from '{u}' to '{v}' with cost {cost}.")
        else:
            print("Add nodes first for edge creation.")
    def delete_node(self, node):
        if node in self.graph:
            del self.graph[node]
            for n in self.graph:
                self.graph[n] = [(x, c) for x, c in self.graph[n] if x != node]
            print(f"Node '{node}' deleted.")
        else:
            print(f"Node '{node}' not found.")
    def delete_edge(self, u, v):
        edge_deleted = False
        if u in self.graph:
            initial_len = len(self.graph[u])
            self.graph[u] = [(x, c) for x, c in self.graph[u] if x != v]
            if len(self.graph[u]) < initial_len:
                edge_deleted = True
        if not self.directed and v in self.graph:
            initial_len = len(self.graph[v])
            self.graph[v] = [(x, c) for x, c in self.graph[v] if x != u]
            if len(self.graph[v]) < initial_len:
                edge_deleted = True
        if edge_deleted:
            print(f"Edge between '{u}' and '{v}' deleted.")
        else:
            print(f"Edge between '{u}' and '{v}' not found.")
    def display(self):
        print("\nGraph Adjacency List:")
        if not self.graph:
            print("Graph is empty.")
            return
        for node in sorted(self.graph.keys()):
            print(f"{node}: {self.graph[node]}")
    def display_adj_list(self, node):
        if node in self.graph:
            print(f"Adjacency list for '{node}': {self.graph[node]}")
        else:
            print(f"Node '{node}' not found.")
    def _print_table_row(self, iteration, fringe, explored, current_node):
        fringe_str = ', '.join([n for n, _ in fringe])
        explored_str = ', '.join(explored)
        print(f"{iteration:<10} | {fringe_str:<30} | {explored_str:<20}")
    def bfs_lr(self, start, goal=None):
        if start not in self.graph:
            print("Start node not found")
            return
        explored = []
        print(f"{'Iteration':<10} | {'Fringe (Nodes)'} | {'Explored (Nodes)'}")
        fringe = deque([start])
        i = 0
        while fringe:
            i += 1
            node = fringe.popleft()
            explored.append(node)
            if node == goal:
                print("Goal is reached")
                print("Path is:", explored)
                return
            for neigh, _ in self.graph[node]:
                if neigh not in fringe and neigh not in explored:
                    fringe.append(neigh)
            print(i, list(fringe), explored)
        print("Goal not reached")
    def bfs_rl(self, start, goal=None):
        if start not in self.graph:
            print("Start node not found")
            return
        explored = []
        print(f"{'Iteration':<10} | {'Fringe (Nodes)'} | {'Explored (Nodes)'}")
        fringe = deque([start])
        i = 0
        while fringe:
            i += 1
            node = fringe.popleft()
            explored.append(node)
            if node == goal:
                print("Goal is reached")
                print("Path is:", explored)
                return
            for neigh, _ in reversed(self.graph[node]):
                if neigh not in fringe and neigh not in explored:
                    fringe.append(neigh)
            print(i, list(fringe), explored)
        print("Goal not reached")
    def dfs_lr(self, start, goal=None):
        if start not in self.graph:
            print("Start node not found")
            return
        explored = []
        print(f"{'Iteration':<10} | {'Fringe (Nodes)'} | {'Explored (Nodes)'}")
        fringe = [start]
        i = 0
        while fringe:
            i += 1
            node = fringe.pop()
            explored.append(node)
            if node == goal:
                print("Goal is reached")
                print("Path is:", explored)
                return
            for neigh, _ in self.graph[node]:
                if neigh not in fringe and neigh not in explored:
                    fringe.append(neigh)
            print(i, fringe, explored)
        print("Goal not reached")
    def dfs_rl(self, start, goal=None):
        if start not in self.graph:
            print("Start node not found")
            return
        explored = []
        print(f"{'Iteration':<10} | {'Fringe (Nodes)'} | {'Explored (Nodes)'}")
        fringe = [(start)]
        i = 0
        while fringe:
            i += 1
            node = fringe.pop()
            explored.append(node)
            if node == goal:
                print("Goal is reached")
                print("Path is:", explored)
                return
            for neigh, _ in reversed(self.graph[node]):
                if neigh not in fringe and neigh not in explored:
                    fringe.append(neigh)
            print(i, fringe, explored)
        print("Goal not reached")
    def ucs(self,start,goal):
        frontier=[]
        h.heappush(frontier,(0,start,[start]))
        explored=set()
        i=1
        print("Iteration\tFringe\tExplored\n")
        print("---------------------------------------\n")
        while frontier:
            fringe=[(p,c) for (c,n,p) in frontier]
            print(f"{i}  {fringe}\t\n{list(explored)}")
            cost,node,path=h.heappop(frontier)
            if node==goal:
                print("Goal reached")
                print("Total cost: ",cost)
                print("Path: ",path)
                return
            explored.add(node)
            for child,e_cost in self.graph[node]:
                if child not in explored:
                    new_cost=cost+e_cost
                    in_front=False
                    for j,(c,n,p) in enumerate(frontier):
                        if n==child:
                            in_front=True;
                            if new_cost<c:
                                frontier.pop(j)
                                h.heappush(frontier,(new_cost,child,path+[child]))
                            break
                    if not in_front:
                        h.heappush(frontier,(new_cost,child,path+[child]))
            i+=1
        print("Goal not found")
def get_graph_input_initial(graph_obj):
    num_nodes = int(input("Enter the number of nodes: "))
    print("Enter ",num_nodes,"nodes :")
    for i in range(num_nodes):
        node_name = input()
        graph_obj.add_node(node_name)
    num_edges = int(input("Enter the number of edges: "))
    for i in range(num_edges):
        u,v,cost_str = input(f"Enter 'from','to' and cost of node for Edge {i+1}: ").split()
        cost = int(cost_str) if cost_str else 0
        graph_obj.add_edge(u, v, cost)
    print("\nInitial graph setup complete!")
def run_menu(graph_obj):
    print("\nMENU")
    print("1  Add Node")
    print("2  Add Edge")
    print("3  Delete Node")
    print("4  Delete Edge")
    print("5  Display Graph")
    print("6  Display Adjacency List")
    print("7  BFS Left to Right ")
    print("8  BFS Right to Left ")
    print("9  DFS Left to Right ")
    print("10 DFS Right to Left ")
    print("11 UCS")
    print("12 Exit")
    while True:
        ch = input("Enter choice: ")
        if not ch.isdigit():
            print("Invalid input. Please enter a number between 1 and 11.")
            continue
        ch = int(ch)
        if ch == 1:
            graph_obj.add_node(input("Node: "))
        elif ch == 2:
            u = input("From: ")
            v = input("To: ")
            cost_str = input("Cost (press Enter for 0): ")
            cost = int(cost_str) if cost_str else 0
            graph_obj.add_edge(u, v, cost)
        elif ch == 3:
            node_to_delete = input("Node: ")
            graph_obj.delete_node(node_to_delete)
        elif ch == 4:
            u = input("From: ")
            v = input("To: ")
            graph_obj.delete_edge(u, v)
        elif ch == 5:
            graph_obj.display()
        elif ch == 6:
            graph_obj.display_adj_list(input("Node: "))
        elif ch in [7, 8, 9, 10]:
            start_node = input("Enter start node: ")
            goal_input = input("Enter goal node : ")
            goal_node = goal_input if goal_input else None
            if ch == 7:
                graph_obj.bfs_lr(start_node, goal_node)
            elif ch == 8:
                graph_obj.bfs_rl(start_node, goal_node)
            elif ch == 9:
                graph_obj.dfs_lr(start_node, goal_node)
            elif ch == 10:
                graph_obj.dfs_rl(start_node, goal_node)
        elif ch==11:
            start = input("Enter start node: ")
            goal = input("Enter goal node : ")
            graph_obj.ucs(start,goal)
        elif ch == 12:
            print("Program terminated.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 11.")
graph_type = input("Enter graph type (D for Directed / U for Undirected): ").strip().upper()
is_directed = True if graph_type == 'D' else False
g = Graph(directed=is_directed)
get_graph_input_initial(g)
run_menu(g)
