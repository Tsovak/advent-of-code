use std::fs;
use std::path::Path;

fn is_level_valid(level: &[String]) -> bool {
    // strings to integers
    let level_int: Vec<i32> = match level.iter().map(|l| l.parse::<i32>()).collect() {
        Ok(nums) => nums,
        Err(_) => return false,
    };

    let is_increasing = level_int.windows(2).all(|w| w[0] < w[1]);
    let is_decreasing = level_int.windows(2).all(|w| w[0] > w[1]);

    if !(is_increasing || is_decreasing) {
        return false;
    }

    level_int.windows(2).all(|w| {
        let diff = (w[0] - w[1]).abs();
        diff >= 1 && diff <= 3
    })
}

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
        .filter(|line| !line.is_empty())
        .collect()
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let lines = read_lines();

    let report_count = lines
        .iter()
        .filter(|line| {
            let levels: Vec<String> = line.split_whitespace().map(|s| s.to_string()).collect();
            is_level_valid(&levels)
        })
        .count();

    println!("{}", report_count);
    Ok(())
}