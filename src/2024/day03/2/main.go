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

func main() {
	lines := strings.ReplaceAll(fileContents, "\n", "")
	pattern := regexp.MustCompile(`mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))`)
	matches := pattern.FindAllStringSubmatch(lines, -1)

	result := 0
	do := true

	for _, match := range matches {
		if match[3] != "" || match[4] != "" {
			do = match[3] != ""
		} else {
			a, _ := strconv.Atoi(match[1])
			b, _ := strconv.Atoi(match[2])
			if do {
				result += a * b
			}
		}
	}

	fmt.Println(result)

}
