#include <stdio.h>

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

	int mid = left + (right - left) /2;
	build(2 * index + 1, left, mid);
	build(2 * index + 2, mid + 1, right);

	tree[index] = tree[2 * index + 1] + tree[2 * index + 2];

}

int main(int argc, char *argv[])
{

	build(0, 0, sizeof(data) / sizeof(int));

	for ( int i = 0; i < sizeof(tree) / sizeof(int); i++ )
	{
		printf("%d ", tree[i]);
	}

	printf("\n%ld\n", sizeof(tree) / sizeof(int));

	return 0;

}

