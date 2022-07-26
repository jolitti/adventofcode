// 2414bc77 437e60fc

use md5;
use std::collections::HashMap;

const INPUT: &str = "wtnhxymk";

fn main() {

    // let ans1 = get_password(INPUT, 8);
    
    // println!("First answer: {ans1}");

    let ans2 = get_password_2(INPUT, 8);

    println!("Second answer: {ans2}");
}


fn get_password_1(s:&str, target_len: usize) -> String {
    let mut ans: String = String::new();
    let mut index = 0usize;

    while ans.len() < target_len {
        let new_str = format!("{s}{index}");
        let digest = md5::compute(new_str);
        let hash_str = format!("{digest:x}");

        if let Some(c) = sixth_char(hash_str.as_str()) {
            ans.push(c);
        }

        index += 1;
    }

    ans
}

fn get_password_2(s:&str, target_len:usize) -> String {
    let mut char_map: HashMap<usize,char> = HashMap::new();
    let mut index = 0usize;
    let mut solved = 0usize;
    
    while solved < target_len {
        let source_str = format!("{s}{index}");
        let digest = md5::compute(source_str);
        let hash_str = format!("{digest:x}");

        if let Some((n,c)) = sixth_char_2(&hash_str) {
            if !char_map.contains_key(&n) {
                char_map.insert(n,c);
                solved += 1;

                println!("{}",partial_str(&char_map, target_len));
            }
        }

        index += 1;
    }

    partial_str(&char_map, target_len)
}

fn partial_str(map:&HashMap<usize,char>, len: usize) -> String {
    let mut ans = String::new();
    for i in 0..len {
        ans.push(*map.get(&i).unwrap_or(&'_'));
    }
    ans
}

fn sixth_char(s:&str) -> Option<char> {

    if s.len() < 6 { return None; }

    match &s[..5]
    {
        "00000" => { s.chars().nth(5) },
        _ => None
    }
}

fn sixth_char_2(s:&str) -> Option<(usize,char)> {

    if s.len() < 7 { return None; }

    match &s[..5] {
        "00000" => {
            let index = s.chars().nth(5)?.to_digit(10)? as usize;
            if index > 7 { None }
            else { Some((index,s.chars().nth(6)?)) }
        },
        _ => None
    }

}