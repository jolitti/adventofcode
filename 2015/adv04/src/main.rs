// NOTE: Solved the second part in m.py

use md5;

fn main() {
    let x = first_valid_num(&"iwrupvqb");
    println!("{}",x);
}

fn _five_zeroes(s:&str) -> bool {
    &s[..5] == "00000"
}
fn six_zeroes(s:&str) -> bool {
    &s[..6] == "000000"
}

fn first_valid_num(s:&str) -> i32 {
    let mut i = 0;
    loop{
        let concat = format!("{}{}",s,i);
        let hash_digest = md5::compute(concat);
        let hash = format!("{:x}",hash_digest);

        if six_zeroes(&hash) {return i;}
        println!("{}",hash);
        i+=1;
    }
}