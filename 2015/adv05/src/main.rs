use std::collections::HashMap;
use Vec;
use std::fs;

fn main() {
    //println!("{}",has_double_couple("aaaa"));


    let data : String = fs::read_to_string("input.txt").expect("File not found!");
    let data : Vec<_> = data.lines().collect();

    let mut total = 0;
    for d in data {
        if is_nice(&d) { total += 1; }
    }
    println!("{}",total);

    let data : String = fs::read_to_string("input.txt").expect("File not found!");
    let data : Vec<_> = data.lines().collect();
    let mut total2 = 0;
    for d in data { if is_nice2(d) { total2 += 1; }}
    println!("{}",total2);
}

fn is_nice(s:&str) -> bool {
    three_vowels(s) && double_letter(s) && has_not_forb_str(s)
}
fn is_nice2(s:&str) -> bool {
    has_double_couple(s) && double_letter_with_sep(s)
}

fn three_vowels(s:&str) -> bool {
    let vows : Vec<char> = "aeiou".chars().collect();
    let mut letters: HashMap<char,i32> = HashMap::new();
    for c in s.chars(){
        *letters.entry(c).or_insert(0) += 1;
    };

    let mut total : i32 = 0;
    for v in vows{
        total += letters.get(&v).unwrap_or(&0);
    };
    total >= 3
}

fn double_letter(s:&str) -> bool{
    let chars: Vec<char> = s.chars().collect();
    for i in 0..s.len()-1{
        if chars[i]==chars[i+1] {return true};
    };
    false
}

fn has_not_forb_str(s:&str) -> bool{
    let forbidden_strs : Vec<&str> = vec!["ab", "cd", "pq", "xy"];
    for f in forbidden_strs{
        if s.contains(f) {return false;}
    };
    true
}

fn has_double_couple(s:&str) -> bool {
    //println!("Testing double couple");
    for i in 0..s.len()-3 {
        let refstr : &str = &s[i..i+2];
        //println!("ref1 = {}",refstr);
            for j in i+2..s.len()-1 {
                let refstr2 = &s[j..j+2];
                //println!("ref2 = {}",refstr2);
                if refstr == refstr2 { return true; }
        };
    };

    false
}

fn double_letter_with_sep(s:&str) -> bool {
    let chars: Vec<char> = s.chars().collect();
    for i in 0..s.len()-2{
        if chars[i]==chars[i+2] {return true};
    };
    false
}