package main

import (
	_ "embed"
	"fmt"
	"strconv"
	"strings"
)

//go:embed data.txt
var fileContents string

func isLevelValid(level []string) bool {
	// strings to integers
	levelInt := make([]int, len(level))
	for i, l := range level {
		num, err := strconv.Atoi(l)
		if err != nil {
			return false
		}
		levelInt[i] = num
	}

	isIncreasing := true
	isDecreasing := true

	for i := 0; i < len(levelInt)-1; i++ {
		if levelInt[i] >= levelInt[i+1] {
			isIncreasing = false
		}
		if levelInt[i] <= levelInt[i+1] {
			isDecreasing = false
		}
	}

	if !(isIncreasing || isDecreasing) {
		return false
	}

	for i := 0; i < len(levelInt)-1; i++ {
		diff := abs(levelInt[i] - levelInt[i+1])
		if diff < 1 || diff > 3 {
			return false
		}
	}

	return true
}

// abs is a helper function to calculate absolute value
func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func process(contents string) int {
	lines := strings.Split(contents, "\n")

	reportCount := 0
	for _, line := range lines {
		levels := strings.Fields(line)
		if isLevelValid(levels) {
			reportCount++
		}
	}

	return reportCount
}

func main() {
	result := process(fileContents)
	fmt.Println(result)
}
