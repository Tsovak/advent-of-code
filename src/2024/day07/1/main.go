package main

import (
	_ "embed"
	"fmt"
	"strconv"
	"strings"
)

//go:embed data.txt
var fileContents string

func evaluateExpression(numbers []int, ops []string) int {
	result := numbers[0]
	for i, op := range ops {
		if op == "+" {
			result += numbers[i+1]
		} else {
			result *= numbers[i+1]
		}
	}
	return result
}

func findValidEquations(desiredSum int, numbers []int) [][]string {
	var validEquations [][]string
	allowedOperations := []string{"+", "*"}

	// generate all possible operation combinations
	var generateCombinations func(int, []string)
	generateCombinations = func(depth int, current []string) {
		if depth == len(numbers)-1 {
			// try the current combination
			result := evaluateExpression(numbers, current)
			if result == desiredSum {
				validEquations = append(validEquations, append([]string{}, current...))
			}
			return
		}

		for _, op := range allowedOperations {
			generateCombinations(depth+1, append(current, op))
		}
	}

	generateCombinations(0, []string{})
	return validEquations
}

func main() {
	lines := strings.Split(strings.TrimSpace(fileContents), "\n")

	totalCalibration := 0
	for _, line := range lines {
		parts := strings.Split(line, ": ")
		desiredSum, _ := strconv.Atoi(parts[0])

		numberStrs := strings.Fields(parts[1])
		numbers := make([]int, len(numberStrs))
		for i, numStr := range numberStrs {
			numbers[i], _ = strconv.Atoi(numStr)
		}

		validEquations := findValidEquations(desiredSum, numbers)
		if len(validEquations) > 0 {
			totalCalibration += desiredSum
		}
	}

	fmt.Println(totalCalibration)
}
