#include <stdio.h>

// 线段树


int data[] = {1,3,5,7,9,2,4,6,8,10};
int tree[4 * sizeof(data)/sizeof(int)];

// 构建index节点的值
void build(int index, int left, int right)
{

	if (left == right)
	{
		tree[index] = data[left];
		return;
	}

	int mid = left + (right - left) / 2;
	build(2 * index + 1, left, mid);
	build(2 * index + 2, mid + 1, right);

	tree[index] = tree[2 * index + 1] + tree[2 * index + 2];

}

// 更新
void update(int index, int left, int right, int idx, int v)
{

	if (left == right)
	{
		tree[index] = v;
		return;
	}

	int mid = left + (right - left) / 2;
	if (idx <= mid)
		update(2 * index + 1, left, mid, idx, v);
	else
		update(2 * index + 2, mid + 1, right, idx, v);


	tree[index] = tree[2 * index + 1] + tree[2 * index + 2];


}

// 查询
int query(int index, int left, int right, int lq, int rq)
{

	// 第一种情况
	if (left == lq && right == rq)
		return tree[index];


	int mid = left + (right - left) / 2;

	// 第二种情况
	if (rq <= mid)
		return query(2 * index + 1, left, mid, lq, rq);
	// 第三种情况
	else if (mid + 1 <= lq)
		return query(2 * index + 2, mid + 1, right, lq, rq);

	// 第四种情况
	return query(2 * index + 1, left, mid, lq, mid) + query(2 * index + 2, mid + 1, right, mid + 1, rq);

}



int main(int argc, char *argv[])
{

	// 将data[]中下标[0, len-1]的数据构造成一颗线段树
	build(0, 0, sizeof(data) / sizeof(int) - 1);

	for ( int i = 0; i < sizeof(tree) / sizeof(int); i++ )
	{
		printf("%d ", tree[i]);
	}

	printf("\n%ld\n", sizeof(tree) / sizeof(int));


#if 0
	// 更新data[]中下标=4(idx=4)的值为40
	update(0, 0, sizeof(data) / sizeof(int) - 1, 4, 40);
	for ( int i = 0; i < sizeof(tree) / sizeof(int); i++ )
	{
		printf("%d ", tree[i]);
	}
#endif


	
	int res = query(0, 0, sizeof(data) / sizeof(int) - 1, 4, 6);
	printf("query = %d\n", res);

	return 0;

}

