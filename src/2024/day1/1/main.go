package main

import (
	_ "embed"
	"fmt"
	"sort"
	"strconv"
	"strings"
)

//go:embed data.txt
var fileContents string

func readAndProcessData(contents string) (int, error) {
	var firstColumn []int
	var secondColumn []int

	lines := strings.Split(contents, "\n")
	for _, line := range lines {
		// skip empty lines
		if line == "" {
			continue
		}

		// split the line and convert to integers
		parts := strings.Fields(line)
		if len(parts) < 2 {
			continue
		}

		first, err := strconv.Atoi(parts[0])
		if err != nil {
			return 0, err
		}
		second, err := strconv.Atoi(parts[1])
		if err != nil {
			return 0, err
		}

		firstColumn = append(firstColumn, first)
		secondColumn = append(secondColumn, second)
	}

	// sort columns
	sort.Ints(firstColumn)
	sort.Ints(secondColumn)

	// calculating
	var result int
	for i := range firstColumn {
		diff := firstColumn[i] - secondColumn[i]
		if diff < 0 {
			diff = -diff
		}
		result += diff
	}

	return result, nil
}

func main() {
	result, err := readAndProcessData(fileContents)
	if err != nil {
		fmt.Println("Error processing file:", err)
		return
	}

	fmt.Println(result)
}
