package main

import (
	_ "embed"
	"strconv"
	"strings"
)

//go:embed data.txt
var fileContents string

func split(number uint64) []uint64 {
	if number == 0 {
		return []uint64{1}
	}

	numberStr := strconv.FormatUint(number, 10)
	if len(numberStr)%2 == 0 {
		half := len(numberStr) / 2
		return []uint64{
			mustParseUint(numberStr[:half]),
			mustParseUint(numberStr[half:]),
		}
	}
	return []uint64{number * 2024}
}

func mustParseUint(s string) uint64 {
	num, err := strconv.ParseUint(s, 10, 64)
	if err != nil {
		panic(err)
	}
	return num
}

func blinking(numbers []uint64, until int) int {
	stones := make(map[uint64]int)
	for _, n := range numbers {
		stones[n]++
	}

	for i := 0; i < until; i++ {
		newStones := make(map[uint64]int)

		for n, count := range stones {
			splits := split(n)
			for _, split := range splits {
				newStones[split] += count
			}
		}

		stones = newStones
	}
	total := 0
	for _, count := range stones {
		total += count
	}
	return total

}

func main() {
	line := strings.TrimSpace(strings.Split(fileContents, "\n")[0])
	numbers := make([]uint64, 0)
	for _, numStr := range strings.Fields(line) {
		num := mustParseUint(numStr)
		numbers = append(numbers, num)
	}

	total := blinking(numbers, 75)
	println(total)
}
