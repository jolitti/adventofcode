// asvcbhvg odqnikqv

use std::collections::HashMap;

const INPUT: &str = include_str!("input.txt");

fn main() {
    let mut ans = String::new();

    for i in 0..8 {
        let mut letters: HashMap<char,usize> = HashMap::new();

        for s in INPUT.lines() {
            let c = s.chars().nth(i).unwrap();

            let n = letters.entry(c).or_insert(0).clone();
            letters.insert(c, n + 1);
        }

        let mut letters = letters.iter().collect::<Vec<_>>();
        
        // original (most common): letters.sort_by(|a,b| b.1.cmp(a.1));
        letters.sort_by(|a,b| a.1.cmp(b.1));

        let (c,_) = letters[0];

        ans.push(*c);
    }
    println!("{ans}");
}
