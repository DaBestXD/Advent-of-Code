package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func formatInput() *[]int {
	var convertedArray []int
	data, _ := os.ReadFile("../../puzzle_inputs/2025_day1_input.txt")
	for v := range strings.SplitSeq(string(data), "\n") {
		if v == "" {
			continue
		}
		num, _ := strconv.Atoi(v[1:])
		if v[0] == 'L' {
			num, _ = strconv.Atoi("-" + v[1:])
			convertedArray = append(convertedArray, num)
		} else {
			convertedArray = append(convertedArray, num)
		}
	}
	return &convertedArray
}

func main() {
	startPos := 50
	counter := 0
	for _, v := range *formatInput() {
		startPos += v
		startPos %= 100
		if startPos == 0 {
			counter++
		}
	}
	fmt.Printf("Count %d", counter)
}
