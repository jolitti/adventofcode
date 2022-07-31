// 118

use itertools::Itertools;
use regex::Regex;

pub fn is_valid_ipv7(s:&str) -> bool {
    let brackets_pattern = Regex::new(r"\[.*?\]").unwrap();
    let inside_brackets = brackets_pattern.find_iter(s)
                            .map(|m| &m.as_str()[1..m.as_str().len()-1]).collect::<Vec<_>>();
    let outside_brackets = brackets_pattern.split(s).collect::<Vec<_>>();

    //println!("{inside_brackets:?}");
    //println!("{outside_brackets:?}");

    for s in inside_brackets {
        if has_abba(s) { return false; }
    }
    for s in outside_brackets {
        if has_abba(s) { return true; }
    }

    false
}

fn has_abba(s:&str) -> bool {
    for window in s.chars().collect::<Vec<_>>().windows(4) {
        if is_abba(window) { return true; }
    }
    
    false
}

fn is_abba(s:&[char]) -> bool {
    assert_eq!(s.len(),4);
    let (a,b,c,d) = s.iter().next_tuple().unwrap();

    a != b && a == d && b == c
}

pub fn supports_ssl(s:&str) -> bool {

    let brackets_pattern = Regex::new(r"\[.*?\]").unwrap();
    let inside_brackets = brackets_pattern.find_iter(s)
                            .map(|m| &m.as_str()[1..m.as_str().len()-1]).collect::<Vec<_>>();
    let outside_brackets = brackets_pattern.split(s).collect::<Vec<_>>();

    for s in outside_brackets {
        for triplet in s.chars().collect::<Vec<_>>().windows(3) {
            let (a,b,c) = triplet.iter().next_tuple().unwrap();
            if a == c && a != b {
                let opposite_str: String = [*b,*a,*b].iter().collect();
                for inside_s in &inside_brackets {
                    if inside_s.contains(opposite_str.as_str()) { return true; }
                }
            }
        }
    }

    false
}