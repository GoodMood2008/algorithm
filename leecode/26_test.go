package main

import (
	"fmt"
	"testing"
)

// Given a sorted array nums, remove the duplicates 
// in-place such that each element appear only once and return the new length.
// Do not allocate extra space for another array, 
// you must do this by modifying the input array in-place with O(1) extra memory.

func removeDuplicates(nums []int) int {
    length := len(nums)
    if length <= 1 {
        return length
    }
    pos := 1
    v := nums[0]
    for i := 1; i < length; i++ {
        if v != nums[i] {
            nums[pos] = nums[i]
            pos++
            v = nums[i]
        }
    }
    return pos
}

func removeDuplicates_v1(nums []int) int {
    i := 0
    for _, n := range nums {
        if i == 0 || n > nums[i-1] {
            nums[i] = n
            i++
        }
    }
    return i
}

func assertEqual(t *testing.T, a bool) {
	if !a {
		t.Errorf("Not Equal. ")
	}
}

func print(array []int) {
    fmt.Print("[")
    for i := 0; i < len(array); i++ {
        fmt.Print(array[i], " ")
    }
    fmt.Println("]")
}

func do_assert(t *testing.T, length int, targetLength int, array []int) {
    assertEqual(t, length == targetLength)
    for i := 0; i < length; i++ {
        assertEqual(t, array[i] == i)
    }
}

func TestRemoveDuplicates(t *testing.T) {
    array := []int{0,0,1,1,1,2,2,3,3,4}
    length := removeDuplicates(array)
    do_assert(t, length, 5, array)

    array = []int{0,0,1,1,1,2,2,3,3,4}
    length = removeDuplicates_v1(array)
    do_assert(t, length, 5, array)
}
