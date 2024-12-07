use regex::Regex;
use std::fs;
use std::path::Path;

fn read_lines() -> Vec<String> {
    let current_file = Path::new(file!());
    let current_dir = current_file
        .parent()
        .expect("Failed to get parent directory");
    let file_path = current_dir.join("data.txt");

    fs::read_to_string(file_path)
        .expect("Failed to read file")
        .lines()
        .map(|line| line.to_string())
        .collect()
}

fn find_xs_count(line: &str) -> usize {
    line.matches("XMAS").count() + line.matches("SAMX").count()
}

fn get_diagonals(matrix: &Vec<Vec<char>>) -> Vec<Vec<char>> {
    let rows = matrix.len();
    let cols = matrix[0].len();
    let mut diagonals = Vec::new();

    // main diagonals
    for d in (1 - rows as i32)..(cols as i32) {
        let mut diag = Vec::new();
        for r in 0..rows {
            let c = d + r as i32;
            if c >= 0 && c < cols as i32 {
                diag.push(matrix[r][c as usize]);
            }
        }
        if !diag.is_empty() {
            diagonals.push(diag);
        }
    }

    // reversed matrix diagonals
    let reversed_matrix: Vec<Vec<char>> = matrix
        .iter()
        .map(|row| row.iter().rev().cloned().collect())
        .collect();

    for d in (1 - rows as i32)..(cols as i32) {
        let mut diag = Vec::new();
        for r in 0..rows {
            let c = d + r as i32;
            if c >= 0 && c < cols as i32 {
                diag.push(reversed_matrix[r][c as usize]);
            }
        }
        if !diag.is_empty() {
            diagonals.push(diag);
        }
    }

    diagonals
}

fn transpose(matrix: &Vec<Vec<char>>) -> Vec<Vec<char>> {
    let rows = matrix.len();
    let cols = matrix[0].len();

    (0..cols)
        .map(|c| (0..rows).map(|r| matrix[r][c]).collect())
        .collect()
}

fn main() {
    let lines = read_lines();
    let matrix: Vec<Vec<char>> = lines.iter().map(|line| line.chars().collect()).collect();

    let mut all_lines = Vec::new();

    // diagonals
    all_lines.extend(get_diagonals(&matrix));

    // rows
    all_lines.extend(matrix.clone());

    // columns
    all_lines.extend(transpose(&matrix));

    let count: usize = all_lines
        .iter()
        .map(|line| find_xs_count(&line.iter().collect::<String>()))
        .sum();

    println!("{}", count);
}
