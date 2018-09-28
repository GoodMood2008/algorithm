package main

func max(a int, b int) int {
    if a > b {
        return a
    } else {
        return b
    }
}

func min(a int, b int) int {
    if a < b {
        return a
    } else {
        return b
    }
}


func maxArea(height []int) int {
    area := 0
    length := len(height)
    i := 0
    j := length - 1
    for i < j {
        temp := (j - i) * min(height[i], height[j])
        area = max(area, temp)
        if (height[i] < height[j]) {
            i++
        } else {
            j--
        }
    }
    return area
}

func assert(cond bool) {
    if (!cond) {
        panic("not equal")
    }
}

func main() {
    input := [9]int{1,8,6,2,5,4,8,3,7}
    assert(maxArea(input[:]) == 49)       
}