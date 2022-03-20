#! /usr/bin/env python


"""
功能: 图的深度优先遍历 == 树的先序遍历

辅助: 需要借助栈
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

# 从起点begin开始, 打印图graph的深度优先遍历
def do_bfs(graph, begin):
	stack = []
	stack.append(begin)
	seen = set()
	seen.add(begin)

	while (len(stack) > 0):
		vertex = stack.pop()
		nodes = graph[vertex] # 找出vertex节点的所有相邻节点
		for node in nodes:
			if node not in seen:
				stack.append(node) # 相邻节点放入队列中
				seen.add(node)
		print(vertex)


if __name__ == "__main__":
	do_bfs(graph, "B")


