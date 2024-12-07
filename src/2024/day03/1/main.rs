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

fn extract(line: &str) -> i32 {
    let pattern = Regex::new(r"mul\((\d{1,3}),(\d{1,3})\)").unwrap();
    pattern
        .captures_iter(line)
        .map(|cap| {
            let n1: i32 = cap.get(1).unwrap().as_str().parse().unwrap();
            let n2: i32 = cap.get(2).unwrap().as_str().parse().unwrap();
            n1 * n2
        })
        .sum()
}

fn main() {
    let lines = read_lines();
    let result: i32 = lines.iter().map(|line| extract(line)).sum();
    println!("{}", result);
}
