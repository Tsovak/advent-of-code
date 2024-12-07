use regex::Regex;
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

fn find_xs_count(line: &str) -> usize {
    line.matches("XMAS").count() + line.matches("SAMX").count()
}

fn find_3x3_patterns(matrix: &Vec<Vec<char>>) -> usize {
    let valid_patterns = vec![
        vec!['M', 'S', 'M', 'S'],
        vec!['S', 'M', 'S', 'M'],
        vec!['S', 'S', 'M', 'M'],
        vec!['M', 'M', 'S', 'S'],
    ];

    let mut count = 0;
    for i in 0..=matrix.len() - 3 {
        for j in 0..=matrix[0].len() - 3 {
            let corners = vec![
                matrix[i][j],
                matrix[i][j + 2],
                matrix[i + 2][j],
                matrix[i + 2][j + 2],
            ];
            let center = matrix[i + 1][j + 1];

            if center == 'A' {
                for pattern in &valid_patterns {
                    if corners == *pattern {
                        count += 1;
                        break;
                    }
                }
            }
        }
    }
    count
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let matrix = read_matrix();
    let result = find_3x3_patterns(&matrix);
    println!("{}", result);
    Ok(())
}
