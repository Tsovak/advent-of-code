package main

import (
	_ "embed"
	"fmt"
	"strings"
)

//go:embed data.txt
var fileContents string

type Position struct {
	x, y, direction int
}

func findGuard(matrix [][]rune) Position {
	for i, row := range matrix {
		for j, cell := range row {
			if cell == '^' {
				return Position{i, j, 0}
			}
		}
	}
	panic("No guard found in matrix")
}

func stepGuard(matrix [][]rune) int {
	dx := []int{-1, 0, 1, 0}
	dy := []int{0, 1, 0, -1}

	rowLen := len(matrix)
	colLen := len(matrix[0])

	guard := findGuard(matrix)
	visited := make(map[string]bool)
	visited[fmt.Sprintf("%d,%d", guard.x, guard.y)] = true

	currentPos := guard

	for {
		nx := currentPos.x + dx[currentPos.direction]
		ny := currentPos.y + dy[currentPos.direction]

		// bounds
		if nx < 0 || nx >= rowLen || ny < 0 || ny >= colLen {
			break
		}

		if matrix[nx][ny] == '#' {
			// turn right
			currentPos.direction = (currentPos.direction + 1) % 4
		} else {
			// move forward
			visited[fmt.Sprintf("%d,%d", nx, ny)] = true
			currentPos = Position{nx, ny, currentPos.direction}
		}
	}

	return len(visited)
}

func main() {
	lines := strings.Split(strings.TrimSpace(fileContents), "\n")

	matrix := make([][]rune, len(lines))
	for i, line := range lines {
		matrix[i] = []rune(line)
	}

	result := stepGuard(matrix)
	fmt.Println(result)

}
