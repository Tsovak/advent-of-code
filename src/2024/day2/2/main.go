package main

import (
	_ "embed"
	"fmt"
	"strconv"
	"strings"
)

//go:embed data.txt
var fileContents string

func isSequenceSafe(sequence []int) bool {
	isIncreasing := true
	isDecreasing := true

	for i := 0; i < len(sequence)-1; i++ {
		if sequence[i] >= sequence[i+1] {
			isIncreasing = false
		}
		if sequence[i] <= sequence[i+1] {
			isDecreasing = false
		}
	}

	if !(isIncreasing || isDecreasing) {
		return false
	}

	for i := 0; i < len(sequence)-1; i++ {
		diff := abs(sequence[i] - sequence[i+1])
		if diff < 1 || diff > 3 {
			return false
		}
	}

	return true
}

func isReportSafe(report string) bool {
	strLevels := strings.Fields(report)
	levels := make([]int, len(strLevels))

	for i, strLevel := range strLevels {
		level, err := strconv.Atoi(strLevel)
		if err != nil {
			return false
		}
		levels[i] = level
	}

	if isSequenceSafe(levels) {
		return true
	}

	for i := range levels {
		testLevels := make([]int, 0, len(levels)-1)
		testLevels = append(testLevels, levels[:i]...)
		testLevels = append(testLevels, levels[i+1:]...)

		if isSequenceSafe(testLevels) {
			return true
		}
	}

	return false
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	lines := strings.Split(fileContents, "\n")

	safeReports := 0
	for _, line := range lines {
		if isReportSafe(line) {
			safeReports++
		}
	}

	fmt.Println(safeReports)
}
