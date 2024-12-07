package main

import (
	_ "embed"
	"fmt"
	"slices"
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

func buildGraph(update []int, rules []rule) map[int][]int {
	graph := make(map[int][]int)
	inDegree := make(map[int]int)

	for _, num := range update {
		if _, exists := graph[num]; !exists {
			graph[num] = []int{}
		}
	}

	for _, rule := range rules {
		if slices.Contains(update, rule.before) && slices.Contains(update, rule.after) {
			graph[rule.before] = append(graph[rule.before], rule.after)
			inDegree[rule.after]++
		}
	}

	return graph
}

func topologicalSort(update []int, rules []rule) []int {
	graph := buildGraph(update, rules)
	inDegree := make(map[int]int)
	result := make([]int, 0, len(update))

	// initial in-degrees
	for _, num := range update {
		inDegree[num] = 0
	}
	for _, rule := range rules {
		if slices.Contains(update, rule.before) && slices.Contains(update, rule.after) {
			inDegree[rule.after]++
		}
	}

	// find nodes with no incoming edges
	var queue []int
	for _, num := range update {
		if inDegree[num] == 0 {
			queue = append(queue, num)
		}
	}

	for len(queue) > 0 {
		current := queue[0]
		queue = queue[1:]
		result = append(result, current)

		for _, neighbor := range graph[current] {
			inDegree[neighbor]--
			if inDegree[neighbor] == 0 {
				queue = append(queue, neighbor)
			}
		}
	}

	return result
}

func main() {
	rules, updates := parse(fileContents)

	sum := 0
	for _, update := range updates {
		if !isValidUpdate(update, rules) {
			sortedUpdate := topologicalSort(update, rules)
			middleIdx := len(sortedUpdate) / 2
			sum += sortedUpdate[middleIdx]
		}
	}

	fmt.Println(sum)
}
