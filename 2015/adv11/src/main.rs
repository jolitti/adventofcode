use String;
use itertools::izip;
use fancy_regex::Regex;

fn main() {
    /* for c in "abcdefghijkmnopqrtuvwxyz".chars() {
        println!("{} -> {}",c,next_char(c).0)
    } */

    //let mut pass = String::from("hxbxwxba");
    let mut pass = String::from("hxbxxyzz");

    while !valid_password(&pass) { pass = next_str(pass) }
    println!("first pass: {}",pass);

    pass = next_str(pass);

    while !valid_password(&pass) { pass = next_str(pass) }
    println!("second pass: {}",pass);
}

fn next_char(c:char) -> (char,bool) {
    let ch = c.to_digit(36).unwrap();
    match ch>=35 {
        true => {('a',true)},
        false => {(char::from_digit(ch+1,36).unwrap(),false)}
    }
}

fn next_str(s:String) -> String {
    let mut ans = String::new();
    let mut rolling = true;
    for c in s.chars().rev() {
        if rolling {
            let (new_c,roll) = next_char(c);
            ans = format!("{}{}",new_c,ans);
            rolling = roll;
        }
        else {
            ans = format!("{}{}",c,ans);
        }
    }
    ans
}

fn has_forbidden_letters(s:&String) -> bool {
    let forb_list = ['i','o','l'];
    for c in s.chars() {
        if forb_list.contains(&c) {return true}
    }
    false
}

fn has_inc_straight(s:&String) -> bool {
    for (x,y,z) in izip!(s.chars(),s.chars().skip(1),s.chars().skip(2)) {
        if y == next_char(x).0 && z == next_char(y).0 &&  x!='z' && y!='z' {return true}
    }
    false
}

fn distinct_pairs(s:&String) -> usize {
    let pair_re = Regex::new(r"(\w)\1").unwrap();
    pair_re.find_iter(&s.to_string()).count()
}

fn valid_password(s:&String) -> bool {
    !has_forbidden_letters(s) &&
    has_inc_straight(s) &&
    distinct_pairs(s) >= 2
}