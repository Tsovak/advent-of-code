package main

import (
	_ "embed"
	"fmt"
	"strings"
)

//go:embed data.txt
var fileContents string

func findXsCount(line string) int {
	return strings.Count(line, "XMAS") + strings.Count(line, "SAMX")
}

func transposeMatrix(matrix [][]rune) [][]rune {
	rows, cols := len(matrix), len(matrix[0])
	transposed := make([][]rune, cols)
	for i := range transposed {
		transposed[i] = make([]rune, rows)
	}

	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			transposed[j][i] = matrix[i][j]
		}
	}
	return transposed
}

func getDiagonals(matrix [][]rune) [][]rune {
	rows, cols := len(matrix), len(matrix[0])
	diagonals := [][]rune{}

	// main and anti-diagonals
	for d := 1 - rows; d < cols; d++ {
		diag := []rune{}
		for r := 0; r < rows; r++ {
			c := d + r
			if c >= 0 && c < cols {
				diag = append(diag, matrix[r][c])
			}
		}
		if len(diag) > 0 {
			diagonals = append(diagonals, diag)
		}
	}

	// Reversed matrix diagonals
	reversedMatrix := make([][]rune, rows)
	for i := range matrix {
		reversedMatrix[i] = make([]rune, cols)
		for j := range matrix[i] {
			reversedMatrix[i][j] = matrix[i][cols-1-j]
		}
	}

	for d := 1 - rows; d < cols; d++ {
		diag := []rune{}
		for r := 0; r < rows; r++ {
			c := d + r
			if c >= 0 && c < cols {
				diag = append(diag, reversedMatrix[r][c])
			}
		}
		if len(diag) > 0 {
			diagonals = append(diagonals, diag)
		}
	}

	return diagonals
}

func main() {
	lines := strings.Split(strings.TrimSpace(fileContents), "\n")

	matrix := make([][]rune, len(lines))
	for i, line := range lines {
		matrix[i] = []rune(line)
	}

	var allLines [][]rune

	diagonals := getDiagonals(matrix)
	allLines = append(allLines, diagonals...)

	// rows
	allLines = append(allLines, matrix...)

	// columns
	columns := transposeMatrix(matrix)
	allLines = append(allLines, columns...)

	// count XS
	count := 0
	for _, lineRunes := range allLines {
		line := string(lineRunes)
		count += findXsCount(line)
	}

	fmt.Println(count)
}
