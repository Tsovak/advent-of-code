package main

import (
	_ "embed"
	"fmt"
	"strconv"
	"strings"
)

//go:embed data.txt
var fileContents string

type rule struct {
	before, after int
}

func parse(input string) ([]rule, [][]int) {
	lines := strings.Split(strings.TrimSpace(input), "\n")

	separatorIdx := -1
	for i, line := range lines {
		if line == "" {
			separatorIdx = i
			break
		}
	}

	rules := make([]rule, len(lines[:separatorIdx]))
	for i, line := range lines[:separatorIdx] {
		parts := strings.Split(line, "|")
		before, _ := strconv.Atoi(parts[0])
		after, _ := strconv.Atoi(parts[1])
		rules[i] = rule{before, after}
	}

	// parse updates
	var updates [][]int
	for _, line := range lines[separatorIdx+1:] {
		var update []int
		for _, num := range strings.Split(line, ",") {
			n, _ := strconv.Atoi(num)
			update = append(update, n)
		}
		updates = append(updates, update)
	}

	return rules, updates
}

func isValidUpdate(update []int, rules []rule) bool {
	// for quick lookups
	indexMap := make(map[int]int)
	for i, num := range update {
		indexMap[num] = i
	}

	for _, rule := range rules {
		beforeIdx, beforeExists := indexMap[rule.before]
		afterIdx, afterExists := indexMap[rule.after]

		if beforeExists && afterExists && beforeIdx > afterIdx {
			return false
		}
	}
	return true
}

func main() {
	rules, updates := parse(fileContents)

	sum := 0
	for _, update := range updates {
		if isValidUpdate(update, rules) {
			middleIdx := len(update) / 2
			sum += update[middleIdx]
		}
	}

	fmt.Println(sum)
}
