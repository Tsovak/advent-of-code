use std::collections::HashMap;
use std::fs;
use std::path::Path;

fn read_numbers() -> Vec<u64> {
    let current_file = Path::new(file!());
    let current_dir = current_file
        .parent()
        .expect("Failed to get parent directory");
    let file_path = current_dir.join("data.txt");

    fs::read_to_string(file_path)
        .expect("Failed to read file")
        .split_whitespace()
        .map(|num| num.parse().expect("Failed to parse number"))
        .collect()
}

fn split(number: u64) -> Vec<u64> {
    if number == 0 {
        return vec![1];
    }

    let number_str = number.to_string();
    if number_str.len() % 2 == 0 {
        let half = number_str.len() / 2;
        let first = number_str[..half].parse().unwrap();
        let second = number_str[half..].parse().unwrap();
        vec![first, second]
    } else {
        vec![number * 2024]
    }
}

fn blinking(numbers: Vec<u64>, until: usize) -> usize {
    let mut stones: HashMap<u64, usize> = HashMap::new();
    for &n in &numbers {
        *stones.entry(n).or_insert(0) += 1;
    }

    for _ in 0..until {
        let mut new_stones: HashMap<u64, usize> = HashMap::new();

        for (&n, &count) in stones.iter() {
            for split_num in split(n) {
                *new_stones.entry(split_num).or_insert(0) += count;
            }
        }

        stones = new_stones;
    }

    stones.values().sum()
}

fn main() {
    let numbers = read_numbers();
    let result = blinking(numbers, 75);

    println!("{}", result);
}
