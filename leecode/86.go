package main

import "fmt"

type ListNode struct {
    Val int
    Next *ListNode
}

func print(head *ListNode) {
	cur := head
	for cur != nil {
		fmt.Print(cur.Val, " ")
		cur = cur.Next
	}
}

func convertArrayToList(array []int) *ListNode {
	sentinel := new(ListNode)
	cur := sentinel
	for _, value := range array {
		cur.Next = new(ListNode)
		cur = cur.Next
		cur.Val = value
	}
	return sentinel.Next
}

func isEqual(head1 *ListNode, head2 *ListNode) bool {
	cur1, cur2 := head1, head2
	for cur1 != nil && cur2 != nil {
		if cur1.Val != cur2.Val {
			return false
			cur1, cur2 = cur1.Next, cur2.Next
		}
	}
	if cur1 != nil || cur2 != nil {
		return false
	}
	return true
}

func partition(head *ListNode, x int) *ListNode {
    sentinel1 := new(ListNode)
    sentinel2 := new(ListNode)
    cur, cur1, cur2 := head, sentinel1, sentinel2
    for cur != nil {
    	if cur1.Val < x {
    		cur1.Next = cur
    		cur = cur.Next
    		cur1 = cur1.Next
    	} else {
    		cur2.Next = cur
    		cur = cur.Next
    		cur2 = cur2.Next
    	}
    }
    cur2.Next = nil
    cur1.Next = sentinel2.Next
    return sentinel1.Next
}

func assert(cond bool) {
    if (!cond) {
        panic("not equal")
    }
}

func main() {
    array := [...]int{1, 4, 3, 2, 5, 2}
    head := convertArrayToList(array[:])
    arrayout := [...]int{1, 2, 2, 4, 3, 5}
    headout := convertArrayToList(arrayout[:])
    assert(isEqual(partition(head, 3), headout))
}
