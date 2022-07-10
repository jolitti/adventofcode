use regex::{self,Regex};
use std::collections::HashMap;

#[derive(Debug)]
pub struct Room {
    letters: String,
    checksum: String,
    code: i32
}

impl Room {
    pub fn new(s:&str) -> Self {
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
            letters,
            checksum,
            code
        }
    }

    fn is_valid(self) -> bool {
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

    pub fn value(self) -> i32 {
        let code = self.code;
        match self.is_valid() {
            true => code,
            false => 0
        }
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