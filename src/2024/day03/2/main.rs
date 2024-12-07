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

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let lines = read_lines().join("\n");

    let pattern = Regex::new(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))")?;
    let matches = pattern.captures_iter(&lines);

    let mut result = 0;
    let mut do_calc = true;

    for cap in matches {
        if cap.get(3).is_some() || cap.get(4).is_some() {
            do_calc = cap.get(3).is_some();
        } else {
            let a: i32 = cap.get(1).unwrap().as_str().parse()?;
            let b: i32 = cap.get(2).unwrap().as_str().parse()?;
            if do_calc {
                result += a * b;
            }
        }
    }

    println!("{}", result);
    Ok(())
}
