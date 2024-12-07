use std::collections::HashMap;
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

#[derive(Debug)]
struct Rule {
    before: i32,
    after: i32,
}

fn parse_input(input: &str) -> (Vec<Rule>, Vec<Vec<i32>>) {
    let mut sections = input.trim().split("\n\n");

    let rules = sections
        .next()
        .unwrap()
        .lines()
        .map(|line| {
            let mut parts = line.split('|');
            Rule {
                before: parts.next().unwrap().parse().unwrap(),
                after: parts.next().unwrap().parse().unwrap(),
            }
        })
        .collect();

    let updates = sections
        .next()
        .unwrap()
        .lines()
        .map(|line| line.split(',').map(|n| n.parse().unwrap()).collect())
        .collect();

    (rules, updates)
}

fn is_valid_update(update: &[i32], rules: &[Rule]) -> bool {
    let index_map: HashMap<i32, usize> = update.iter().enumerate().map(|(i, &n)| (n, i)).collect();

    rules.iter().all(
        |rule| match (index_map.get(&rule.before), index_map.get(&rule.after)) {
            (Some(&before_idx), Some(&after_idx)) => before_idx < after_idx,
            _ => true,
        },
    )
}
fn main() {
    let lines = read_lines();
    let content = lines.join("\n");
    let (rules, updates) = parse_input(&content);

    let sum_valid = updates
        .iter()
        .filter(|update| is_valid_update(update, &rules))
        .map(|update| update[update.len() / 2])
        .sum::<i32>();

    println!("{}", sum_valid);
}
