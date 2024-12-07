use std::collections::HashSet;
use std::fs;
use std::path::Path;
fn read_matrix() -> Vec<Vec<char>> {
    let current_file = Path::new(file!());
    let current_dir = current_file
        .parent()
        .expect("Failed to get parent directory");
    let file_path = current_dir.join("data.txt");

    fs::read_to_string(file_path)
        .expect("Failed to read file")
        .lines()
        .map(|line| line.chars().collect())
        .collect()
}

type Matrix = Vec<Vec<char>>;
type Position = (i32, i32, i32);

fn find_guard(matrix: &Matrix) -> Position {
    for (i, row) in matrix.iter().enumerate() {
        for (j, &cell) in row.iter().enumerate() {
            if cell == '^' {
                return (i as i32, j as i32, 0);
            }
        }
    }
    panic!("No guard found in matrix");
}

fn step_guard(matrix: &Matrix) -> usize {
    let dx = [-1, 0, 1, 0];
    let dy = [0, 1, 0, -1];

    let row_len = matrix.len() as i32;
    let col_len = matrix[0].len() as i32;

    let guard = find_guard(matrix);
    let mut visited = HashSet::new();
    visited.insert((guard.0, guard.1));

    let mut current_pos = guard;

    loop {
        let (x, y, direction) = current_pos;

        let nx = x + dx[direction as usize];
        let ny = y + dy[direction as usize];

        // bounds
        if nx < 0 || nx >= row_len || ny < 0 || ny >= col_len {
            break;
        }

        if matrix[nx as usize][ny as usize] == '#' {
            // turn right
            let new_direction = (direction + 1) % 4;
            current_pos = (x, y, new_direction);
        } else {
            // move forward
            visited.insert((nx, ny));
            current_pos = (nx, ny, direction);
        }
    }

    visited.len()
}

fn main() {
    let matrix = read_matrix();
    let result = step_guard(&matrix);
    println!("{}", result);
}
