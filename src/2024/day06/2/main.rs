use rayon::prelude::*;
use std::collections::{HashMap, HashSet};
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

fn visited_guard_path(
    matrix: &Matrix,
    guard: Position,
    row_len: i32,
    col_len: i32,
) -> Option<usize> {
    let dx = [-1, 0, 1, 0];
    let dy = [0, 1, 0, -1];

    let mut visited = HashSet::new();
    let mut visited_states = HashSet::new();

    visited.insert((guard.0, guard.1));
    visited_states.insert(guard);

    let mut current_pos = guard;

    loop {
        let (x, y, direction) = current_pos;
        let nx = x + dx[direction as usize];
        let ny = y + dy[direction as usize];

        if nx < 0 || nx >= row_len || ny < 0 || ny >= col_len {
            break;
        }

        if matrix[nx as usize][ny as usize] == '#' {
            let new_direction = (direction + 1) % 4;
            current_pos = (x, y, new_direction);
        } else {
            visited.insert((nx, ny));
            current_pos = (nx, ny, direction);
        }

        if visited_states.contains(&current_pos) {
            return None;
        }
        visited_states.insert(current_pos);
    }

    Some(visited.len())
}

fn find_positions(matrix: &Matrix) -> usize {
    let row_len = matrix.len();
    let col_len = matrix[0].len();
    let guard_pos = find_guard(matrix);
    let row_len_i32 = row_len as i32;
    let col_len_i32 = col_len as i32;

    (0..row_len)
        .into_par_iter()
        .flat_map(|i| (0..col_len).into_par_iter().map(move |j| (i, j)))
        .filter(|&(i, j)| {
            let cell = matrix[i][j];
            if cell == '^' || cell == '#' {
                return false;
            }

            let mut matrix_copy = matrix.clone();
            matrix_copy[i][j] = '#';

            visited_guard_path(&matrix_copy, guard_pos, row_len_i32, col_len_i32).is_none()
        })
        .count()
}

fn main() {
    let mut matrix = read_matrix();
    let result = find_positions(&mut matrix);
    println!("{}", result);
}
