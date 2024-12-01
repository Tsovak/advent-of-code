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

func calculateSimilarityScore(contents string) (int, error) {
	var firstColumn []int
	rightCounter := make(map[int]int)

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
		rightCounter[second]++
	}

	// sort first column
	sort.Ints(firstColumn)

	// calculate score
	similarityScore := 0
	for _, num := range firstColumn {
		similarityScore += num * rightCounter[num]
	}

	return similarityScore, nil
}

func main() {
	result, err := calculateSimilarityScore(fileContents)
	if err != nil {
		fmt.Println("Error processing file:", err)
		return
	}

	fmt.Println(result)
}
