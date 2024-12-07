use std::collections::{HashMap, VecDeque};
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

fn topological_sort(update: &[i32], rules: &[Rule]) -> Vec<i32> {
    let mut graph: HashMap<i32, Vec<i32>> = HashMap::new();
    let mut in_degree: HashMap<i32, i32> = HashMap::new();

    update.iter().for_each(|&n| {
        graph.entry(n).or_default();
        in_degree.insert(n, 0);
    });

    // graph building
    for rule in rules {
        if update.contains(&rule.before) && update.contains(&rule.after) {
            graph.entry(rule.before).or_default().push(rule.after);
            *in_degree.entry(rule.after).or_default() += 1;
        }
    }

    let mut result = Vec::new();
    let mut queue: VecDeque<i32> = update
        .iter()
        .filter(|&&n| in_degree[&n] == 0)
        .copied()
        .collect();

    while let Some(current) = queue.pop_front() {
        result.push(current);

        if let Some(neighbors) = graph.get(&current) {
            for &next in neighbors {
                in_degree.entry(next).and_modify(|e| *e -= 1);
                if in_degree[&next] == 0 {
                    queue.push_back(next);
                }
            }
        }
    }

    result
}

fn main() {
    let lines = read_lines();
    let content = lines.join("\n");
    let (rules, updates) = parse_input(&content);

    let sum_invalid = updates
        .iter()
        .filter(|update| !is_valid_update(update, &rules))
        .map(|update| {
            let sorted = topological_sort(update, &rules);
            sorted[sorted.len() / 2]
        })
        .sum::<i32>();

    println!("{}", sum_invalid);
}
