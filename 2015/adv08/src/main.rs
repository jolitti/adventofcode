use {Vec,String};
use regex::Regex;

fn main() {
    let data: Vec<&str> = include_str!("../input.txt").lines().collect();
    let mut strings: Vec<&str> = Vec::new();

    for d in data {
        let char_iter = d.chars();
        //char_iter.next();
        //char_iter.next_back();
        strings.push(char_iter.as_str());
    }

    let tot: i32 = strings.iter().map(|x| char_diff2(x)).sum();
    println!("{}",tot);
}

fn char_diff(s:&str) -> i32 {
    println!("Original: \"{}\"",s);
    let x = String::from(s);
    let litlen: i32 = (x.len() + 2) as i32;
    let mut tot: i32 = 0;

    let hex = Regex::new(r"\\[x][a-f0-9][a-f0-9]").unwrap();
    let escapes = Regex::new(r"\\.").unwrap();

    tot += hex.find_iter(s).count() as i32;
    let s2 = hex.replace_all(s, "").to_string();
    println!("After hex escape: {}",s2);

    tot += escapes.find_iter(s2.as_str()).count() as i32;
    let s2 = escapes.replace_all(s2.as_str(), "").to_string();
    println!("After regular escape: {}",s2);

    tot += s2.len() as i32;
    litlen - tot
}

fn char_diff2(s:&str) -> i32 {
    let x = String::from(s);
    let litlen = x.len() as i32;
    
    let mut tot: i32 = 2;
    for c in x.chars() {
        if c == '\\' { tot+= 1; }
        else if c == '\"' { tot += 1; }
        tot += 1;
    }

    tot - litlen
}