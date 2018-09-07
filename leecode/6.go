package main

import "bytes"

func convert(s string, numRows int) string {
    if numRows == 1 {
        return s
    }

    temp := make([]bytes.Buffer, numRows)
    row := 0
    direction := 1
    for i := 0; i < len(s); i++ {
        temp[row].WriteByte(s[i])
        if ((0 != i) && (row == 0 || row == numRows - 1)) {
            direction = 0 - direction
        }
        row += direction
    }

    result := new(bytes.Buffer)
    for _, v := range temp {
        result.Write(v.Bytes())
    }

    return result.String()

}

func assert(cond bool) {
    if (!cond) {
        panic("not equal")
    }
}

func main() {
    str := "abcde"
    assert(convert(str, 2) == "acebd")
    assert(convert(str, 3) == "aebdc")
}