package main

import (
	_ "embed"
	"fmt"
	"strings"
)

//go:embed data.txt
var fileContents string

func readMatrix() [][]rune {
	lines := strings.Split(strings.TrimSpace(fileContents), "\n")
	matrix := make([][]rune, len(lines))
	for i, line := range lines {
		matrix[i] = []rune(line)
	}
	return matrix
}

func find3x3Patterns(matrix [][]rune) int {
	validPatterns := [][]rune{
		[]rune("MSMS"),
		[]rune("SMSM"),
		[]rune("SSMM"),
		[]rune("MMSS"),
	}

	count := 0
	for i := 0; i <= len(matrix)-3; i++ {
		for j := 0; j <= len(matrix[0])-3; j++ {
			corners := []rune{
				matrix[i][j],
				matrix[i][j+2],
				matrix[i+2][j],
				matrix[i+2][j+2],
			}
			center := matrix[i+1][j+1]

			if center == 'A' {
				for _, pattern := range validPatterns {
					if cornersMatch(corners, pattern) {
						count++
						break
					}
				}
			}
		}
	}
	return count
}

func cornersMatch(corners, pattern []rune) bool {
	cornersStr := string(corners)
	patternStr := string(pattern)
	return cornersStr == patternStr
}

func main() {
	matrix := readMatrix()
	result := find3x3Patterns(matrix)
	fmt.Println(result)
}
