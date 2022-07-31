// 118 260

mod util;
mod test;
use rayon::prelude::*;

const INPUT: &str = include_str!("input.txt");

fn main() {
    
    let lines = INPUT.lines().collect::<Vec<_>>();
    let ans1 = lines.par_iter().filter(|addr| util::is_valid_ipv7(addr)).count();

    let ans2 = lines.par_iter().filter(|addr| util::supports_ssl(addr)).count();

    println!("Answer to first part: {ans1}");
    println!("Answer to scond part: {ans2}");
}