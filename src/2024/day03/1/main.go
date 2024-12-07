package main

import (
	_ "embed"
	"fmt"
	"regexp"
	"strconv"
	"strings"
)

//go:embed data.txt
var fileContents string

func extract(line string) int {
	pattern := `mul\((\d{1,3}),(\d{1,3})\)`
	re := regexp.MustCompile(pattern)
	matches := re.FindAllStringSubmatch(line, -1)

	sum := 0
	for _, match := range matches {
		n1, _ := strconv.Atoi(match[1])
		n2, _ := strconv.Atoi(match[2])
		sum += n1 * n2
	}

	return sum
}

func process(lines []string) int {
	result := 0
	for _, line := range lines {
		result += extract(line)
	}

	return result
}

func main() {
	result := process(strings.Split(strings.TrimSpace(fileContents), "\n"))
	fmt.Println(result)
}
