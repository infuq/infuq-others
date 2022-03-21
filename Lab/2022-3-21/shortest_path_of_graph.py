#! /usr/bin/env python


"""
功能: 基于BFS, 计算图中两点最短路径, 无权重

"""

# https://gitee.com/infuq/infuq-img/blob/master/img/graph.jpg
graph = {	
	"A": ["B", "C"],
	"B": ["A", "C", "D"],
	"C": ["A", "B", "D", "E"],	
	"D": ["E", "C", "B", "F"],
	"E": ["C", "D"],
	"F": ["D"]
}

# 从起点begin开始, 打印图graph的广度优先遍历
def do_bfs(graph, begin):
	queue = []
	queue.append(begin)
	seen = set()
	seen.add(begin)
	parent = {
		begin: None # 表示begin的前一个点是None
	}

	while (len(queue) > 0):
		vertex = queue.pop(0)
		nodes = graph[vertex] # 找出vertex节点的所有相邻节点
		for node in nodes:
			if node not in seen:
				queue.append(node) # 相邻节点放入队列中
				seen.add(node)
				parent[node] = vertex	# 表示node的前一个点是vertex
		
	return parent


if __name__ == "__main__":
	parent = do_bfs(graph, "A")

	# E -> A最短路径
	v = 'E'
	while (v != None):
		print(v)
		prev = parent[v]
		v = prev

