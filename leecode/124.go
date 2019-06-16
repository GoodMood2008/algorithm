package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxPathSum(root *TreeNode) int {
	maxVal := ^int(^uint(0) >> 1)
	backtrack(root, &maxVal)
	return maxVal
}

func backtrack(root *TreeNode, maxVal *int) int {
	if nil == root {
		return 0
	}
	left := max2(0, backtrack(root.Left, maxVal))
	right := max2(0, backtrack(root.Right, maxVal))
	*maxVal = max2(*maxVal, root.Val+left+right)
	return root.Val + max2(left, right)

}

func max2(left int, right int) int {
	if left > right {
		return left
	} else {
		return right
	}
}

func assert(cond bool) {
	if !cond {
		panic("not equal")
	}
}

func newTreeNode(val int) *TreeNode {
	node := new(TreeNode)
	node.Val = val
	return node
}

func main() {
	root := newTreeNode(-10)
	root.Left = newTreeNode(9)

	right := newTreeNode(20)
	root.Right = right

	right.Left = newTreeNode(15)
	right.Right = newTreeNode(7)

	maxPath := maxPathSum(root)
	assert(42 == maxPath)

	root = newTreeNode(-3)
	maxPath = maxPathSum(root)
	assert(-3 == maxPath)
}
