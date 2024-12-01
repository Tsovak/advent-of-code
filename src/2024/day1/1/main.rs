use std::fs::File;
use std::io::{BufRead, BufReader};
use std::path::Path;

fn read_and_process_data<P: AsRef<Path>>(filename: P) -> Result<i32, Box<dyn std::error::Error>> {
    let file = File::open(filename)?;
    let reader = BufReader::new(file);

    let mut first_column = Vec::new();
    let mut second_column = Vec::new();

    for line in reader.lines() {
        let line = line?;
        let nums: Vec<i32> = line
            .split_whitespace()
            .map(|s| s.parse().unwrap())
            .collect();

        first_column.push(nums[0]);
        second_column.push(nums[1]);
    }

    first_column.sort_unstable();
    second_column.sort_unstable();

    // Calculate sum of absolute differences
    let result = first_column
        .iter()
        .zip(second_column.iter())
        .map(|(a, b)| (a - b).abs())
        .sum();

    Ok(result)
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let root_dir = std::env::current_dir()?;
    let filename = root_dir.join("data.txt");

    match read_and_process_data(&filename) {
        Ok(result) => {
            println!("{}", result);
            Ok(())
        }
        Err(e) => {
            eprintln!("Error processing file: {}", e);
            Err(e)
        }
    }
}