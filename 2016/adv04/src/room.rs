use regex::{self,Regex};
use std::collections::HashMap;

#[derive(Debug)]
pub struct Room {
    pub real_letters: String,
    pub letters: String,
    checksum: String,
    pub code: i32
}

impl Room {
    pub fn new(s:&str) -> Self {
        let real_letters = String::from(
            Regex::new(r"[a-z\-]*").unwrap().find(s).unwrap().as_str()
        );

        let letters = s.chars()
                    .take_while(|c| !c.is_numeric())
                    .filter(|c| c.is_alphabetic())
                    .collect::<String>();

        let checksum_regex = Regex::new(r"\[[a-z]*\]").unwrap();
        let mut checksum = String::from(checksum_regex.find(s).unwrap().as_str());
        checksum.pop();
        checksum.remove(0);

        let number_regex = Regex::new(r"[0-9]+").unwrap();
        let code = number_regex.find(s).unwrap().as_str().parse::<i32>().unwrap();

        Room {
            real_letters,
            letters,
            checksum,
            code
        }
    }

    pub fn is_valid(&self) -> bool {
        let mut dict: HashMap<char,i32> = HashMap::new();
        for c in self.letters.chars() {
            let num = dict.get(&c).unwrap_or(&0);
            dict.insert(c, num+1);
        }
        let mut pairs = dict.iter().collect::<Vec<_>>();
        pairs.sort_by(|a,b| compare_dict(a, b));
        pairs.reverse();

        let first_five = pairs[..5].iter().map(|(a,_)| *a).collect::<String>();
        first_five == self.checksum
    }

    pub fn value(&self) -> i32 {
        let code = self.code;
        match self.is_valid() {
            true => code,
            false => 0
        }
    }

    pub fn real_name(&self) -> String {
        let mut ans = String::new();
        for c in self.real_letters.chars() {
            ans.push(
                match c {
                    '-' => ' ',
                    _ => shift_letter(c, self.code)
                }
            );
        }
        ans
    }
}

use std::cmp::Ordering;
fn compare_dict(a:&(&char,&i32),b:&(&char,&i32)) -> std::cmp::Ordering {
    let (a_c, a_num) = a;
    let (b_c, b_num) = b;

    let num_ord = a_num.cmp(b_num);

    if num_ord != Ordering::Equal { num_ord }
    else { b_c.cmp(a_c) }
}

const LETTERS: &str = "abcdefghijklmnopqrstuvwxyz";

fn letter_to_num(c:char) -> i32 {
    let chars_to_letters: HashMap<char,i32> = LETTERS
                                        .chars()
                                        .enumerate()
                                        .map(|(n,c)| (c,n as i32))
                                        .collect();

    *chars_to_letters.get(&c).unwrap()
}

fn num_to_letter(n:i32) -> char {
    let letters_to_chars: HashMap<i32,char> = LETTERS
                                        .chars()
                                        .enumerate()
                                        .map(|(n,c)| (n as i32, c))
                                        .collect();

    *letters_to_chars.get(&n).unwrap()
}

pub fn shift_letter(c:char,i:i32) -> char {
    let x = (letter_to_num(c) + i % LETTERS.len() as i32) % LETTERS.len() as i32;
    num_to_letter(x)
} 