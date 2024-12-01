use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::path::Path;

fn calculate_similarity_score(filename: &Path) -> i32 {
    let file = File::open(filename).expect("Unable to open file");
    let reader = BufReader::new(file);

    let (left_list, right_list): (Vec<i32>, Vec<i32>) = reader
        .lines()
        .map(|line| {
            let line = line.expect("Could not read line");
            let parts: Vec<i32> = line
                .split_whitespace()
                .map(|num| num.parse().expect("Failed to parse number"))
                .collect();
            (parts[0], parts[1])
        })
        .unzip();

    // counting
    let mut right_counter = HashMap::new();
    for &num in &right_list {
        *right_counter.entry(num).or_insert(0) += 1;
    }

    left_list
        .iter()
        .map(|&num| num * right_counter.get(&num).cloned().unwrap_or(0))
        .sum()
}

fn main() {
    let exe_path = std::env::current_exe().expect("Failed to get executable path");
    let exe_dir = exe_path.parent().expect("Failed to get executable directory");
    let data_path = exe_dir.join("data.txt");

    let result = calculate_similarity_score(&data_path);
    println!("{}", result);
}