package main

import "fmt"

func min(a int, b int) int {
    if a < b {
        return a
    } else {
        return b
    }
}


func findKth(nums1 []int, nums2 []int, pos int) int {
    if len(nums1) > len(nums2) {
        nums1, nums2 = nums2, nums1
    }

    if len(nums1) == 0 {
        return nums2[pos-1]
    }

    if pos == 1 {
        return min(nums1[0], nums2[0]) 
    }

    m := min(pos/2, len(nums1))
    if nums1[m-1] < nums2[pos-m-1] {
        return findKth(nums1[m:], nums2, pos-m)
    } else {
        return findKth(nums1, nums2[pos-m:], m)
    }
}


func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
    len1 := len(nums1);
    len2 := len(nums2);
    if (len1 + len2) % 2 == 0 {
        return ((float64)(findKth(nums1, nums2, (len1 + len2)/2) + findKth(nums1, nums2, (len1+len2)/2 + 1)))/2
    } else {
        return (float64)(findKth(nums1, nums2, (len1 + len2)/2 + 1))
    }
}

func main() {
    nums1 := [1]int{6}
    nums2 := [5]int{1, 2, 3, 4, 5}
    fmt.Println(findMedianSortedArrays(nums1[:], nums2[:]))
}