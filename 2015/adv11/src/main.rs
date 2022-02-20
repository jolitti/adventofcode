use String;
use Vec;
use itertools::izip;

fn main() {
    /* for c in "abcdefghijkmnopqrtuvwxyz".chars() {
        println!("{} -> {}",c,next_char(c).0)
    } */

    println!("{}",next_str(String::from("aaa")));
    println!("{}",next_str(String::from("aabaz")));
    println!("{}",next_str(String::from("zzz")));

    println!("{}",has_inc_straight(String::from("abcdffaa")));
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

fn has_forbidden_letters(s:String) -> bool {
    let forb_list = ['i','o','l'];
    for c in s.chars() {
        if forb_list.contains(&c) {return true}
    }
    false
}

fn has_inc_straight(s:String) -> bool {
    for (x,y,z) in izip!(s.chars(),s.chars().skip(1),s.chars().skip(2)) {
        if y == next_char(x).0 && z == next_char(y).0 {return true}
    }
    false
}