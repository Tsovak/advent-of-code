use std::fs;
use std::path::Path;

fn is_sequence_safe(sequence: &[i32]) -> bool {
    let is_increasing = sequence.windows(2).all(|w| w[0] < w[1]);
    let is_decreasing = sequence.windows(2).all(|w| w[0] > w[1]);

    if !(is_increasing || is_decreasing) {
        return false;
    }

    sequence.windows(2).all(|w| {
        let diff = (w[0] - w[1]).abs();
        diff >= 1 && diff <= 3
    })
}

fn is_report_safe(report: &str) -> bool {
    // parse the report into levels
    let levels: Vec<i32> = report
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();

    // check if the full sequence is safe
    if is_sequence_safe(&levels) {
        return true;
    }

    // try removing each level and check if the resulting sequence is safe
    for i in 0..levels.len() {
        let test_levels: Vec<i32> = levels
            .iter()
            .enumerate()
            .filter(|&(index, _)| index != i)
            .map(|(_, &val)| val)
            .collect();

        if is_sequence_safe(&test_levels) {
            return true;
        }
    }

    false
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

fn main() {
    let lines = read_lines();

    let safe_reports = lines.iter().filter(|line| is_report_safe(line)).count();

    println!("{}", safe_reports);
}
