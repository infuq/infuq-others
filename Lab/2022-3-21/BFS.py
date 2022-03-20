#! /usr/bin/env python


"""
功能: 图的广度优先遍历 == 树的层序遍历

辅助: 需要借助队列
"""

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

	while (len(queue) > 0):
		vertex = queue.pop(0)
		nodes = graph[vertex] # 找出vertex节点的所有相邻节点
		for node in nodes:
			if node not in seen:
				queue.append(node) # 相邻节点放入队列中
				seen.add(node)
		print(vertex)


if __name__ == "__main__":
	do_bfs(graph, "B")


