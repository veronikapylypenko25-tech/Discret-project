import random
import time

class RandomGraph:
   def __init__(self, n: int, d: float):
       self.n = n
       self.d = d
       self.adjacency_list = [[] for s in range(n)]
       self.adjacency_matrix = [[0]*n for s in range(n)]
       self.generate_directed_acyclic_graph()


   def generate_directed_acyclic_graph(self):
       for i in range(self.n):
           for j in range(i + 1, self.n):
               if random.random() < self.d:
                   self.adjacency_list[i].append(j)
                   self.adjacency_matrix[i][j] = 1


       self.edge_count = sum(sum(row) for row in self.adjacency_matrix)


   def print_graph(self):
       print("Список суміжності:")
       for idx, neighbors in enumerate(self.adjacency_list):
           print(idx, ":", neighbors)


       print("Матриця суміжності:")
       for row in self.adjacency_matrix:
           print(row)

   def topological_sorting(self):
       visited = [0] * self.n
       sorted_v = []

       def move(u):
           visited[u] = 1
           for w in self.adjacency_list[u]:
               if visited[w] == 1:
                   raise ValueError('Граф містить цикл!')
               if visited[w] == 0:
                   move(w)
           visited[u] = 2
           sorted_v.append(u)

       for v in range(self.n):
           if visited[v] == 0:
               move(v)
       return sorted_v[::-1]

   def wat_time_s(self):
       start_sort = time.perf_counter()
       res_2 = self.topological_sorting()
       start_sort_m = time.perf_counter()
       return start_sort_m - start_sort

   def wat_time_m(self):
       start_sort = time.perf_counter()
       res_2 = self.topological_sorting_matrix()
       start_sort_m = time.perf_counter()
       return start_sort_m - start_sort

   def topological_sorting_matrix(self):
       visited = [0] * self.n
       sorted_v = []

       def move(u):
           visited[u] = 1
           for w in range(self.n):
               if self.adjacency_matrix[u][w] == 1:
                   if visited[w] == 1:
                       raise ValueError('Граф містить цикл!')
                   if visited[w] == 0:
                       move(w)
           visited[u] = 2
           sorted_v.append(u)

       for v in range(self.n):
           if visited[v] == 0:
               move(v)
       return sorted_v[::-1]


g = RandomGraph(n=5, d=0.1)
g.print_graph()
print("Кількість ребер:", g.edge_count)
g.print_graph()
print("Кількість вершин:", g.n, ", кількість ребер:", g.edge_count)

def info_tab_sort_s():
    density = {
        0.001: {22: None,
                40:None, 67:None, 73:None, 104:None, 121:None, 146:None, 169:None, 182:None, 199:None},
        0.05: {22: None,
                40:None, 67:None, 73:None, 104:None, 121:None, 146:None, 169:None, 182:None, 199:None},
        0.1: {22: None,
                40:None, 67:None, 73:None, 104:None, 121:None, 146:None, 169:None, 182:None, 199:None},
        0.5: {22: None,
                40:None, 67:None, 73:None, 104:None, 121:None, 146:None, 169:None, 182:None, 199:None},
        0.9: {22: None,
                40:None, 67:None, 73:None, 104:None, 121:None, 146:None, 169:None, 182:None, 199:None}
    }
    for i in density:
        for t in density[i]:
            rr = []
            for k in range(20):
                rr.append(RandomGraph(t, i).wat_time_s())
            density[i][t] = sum(rr)/len(rr)
    return density
def info_tab_sort_m():
    density = {
        0.001: {22: None,
                40: None, 67: None, 73: None, 104: None, 121: None, 146: None, 169: None, 182: None, 199: None},
        0.05: {22: None,
               40: None, 67: None, 73: None, 104: None, 121: None, 146: None, 169: None, 182: None, 199: None},
        0.1: {22: None,
              40: None, 67: None, 73: None, 104: None, 121: None, 146: None, 169: None, 182: None, 199: None},
        0.5: {22: None,
              40: None, 67: None, 73: None, 104: None, 121: None, 146: None, 169: None, 182: None, 199: None},
        0.9: {22: None,
              40: None, 67: None, 73: None, 104: None, 121: None, 146: None, 169: None, 182: None, 199: None}
    }
    for i in density:
        for t in density[i]:
            rr = []
            for k in range(20):
                rr.append(RandomGraph(t, i).wat_time_m())
            density[i][t] = sum(rr) / len(rr)
    return density