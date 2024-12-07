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

type Point struct {
	x, y int
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

func visitedGuardPath(matrix [][]rune, guard Position) int {
	dx := []int{-1, 0, 1, 0}
	dy := []int{0, 1, 0, -1}

	rowLen := len(matrix)
	colLen := len(matrix[0])

	visited := make(map[Point]bool)
	visitedStates := make(map[Position]bool)

	visited[Point{guard.x, guard.y}] = true
	visitedStates[guard] = true

	currentPos := guard

	for {
		nx := currentPos.x + dx[currentPos.direction]
		ny := currentPos.y + dy[currentPos.direction]

		if nx < 0 || nx >= rowLen || ny < 0 || ny >= colLen {
			break
		}

		if matrix[nx][ny] == '#' {
			// turn right
			newDirection := (currentPos.direction + 1) % 4
			currentPos = Position{currentPos.x, currentPos.y, newDirection}
		} else {
			// move forward
			visited[Point{nx, ny}] = true
			currentPos = Position{nx, ny, currentPos.direction}
		}

		if visitedStates[currentPos] {
			return -1
		}
		visitedStates[currentPos] = true
	}

	return len(visited)
}

func findLoopingPositions(matrix [][]rune) int {
	rowLen := len(matrix)
	colLen := len(matrix[0])
	guard := findGuard(matrix)

	loopingPositions := 0

	for i := 0; i < rowLen; i++ {
		for j := 0; j < colLen; j++ {
			if matrix[i][j] == '^' || matrix[i][j] == '#' {
				continue
			}

			// save original value
			original := matrix[i][j]
			matrix[i][j] = '#'

			if visitedGuardPath(matrix, guard) == -1 {
				loopingPositions++
			}

			// restore original value
			matrix[i][j] = original
		}
	}

	return loopingPositions
}

func main() {
	lines := strings.Split(strings.TrimSpace(fileContents), "\n")
	matrix := make([][]rune, len(lines))
	for i, line := range lines {
		matrix[i] = []rune(line)
	}

	result := findLoopingPositions(matrix)
	fmt.Println(result)
}
