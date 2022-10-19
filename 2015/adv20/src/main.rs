// 665280 705600

use divisors::get_divisors;
const OBJECTIVE: usize = 2900000;
const OBJECTIVE_2: usize = 29000000;

fn main() {

    let mut i:usize = 1;
    /* for x in 1usize..=9 {
        let mut divs = corrected_divisors(x);
        divs.sort();
        println!("{}: {:?}",x,divs);
    } */
    loop {
        if score(i) >= OBJECTIVE { break; }
        i += 1;
    }
    println!("First answer: {i}");

    //i = 23023001; // Found by doing a rough search
    i = 1;
    loop {
        if score_3(i,50,11) >= OBJECTIVE_2 { break; }
        i+=1;
        //println!("{i}");
    }
    println!("Second score: {i}");
}

fn corrected_divisors(x:usize) -> Vec<usize> {
    if x == 1 { return vec![1]; }
    if x == 2 { return vec![1,2]; }

    let mut divs =  get_divisors(x);
    divs.extend(vec![1,x]);
    divs
}

fn score(x:usize) -> usize {
    corrected_divisors(x).iter().sum()
}

fn _score_2(x:usize) -> usize {
    let divs = corrected_divisors(x);
    let divs = divs.iter().filter( |n| *n*&50usize>=x).collect::<Vec<_>>();
    divs.iter().map(|n|**n).sum::<usize>()*11
}

fn score_3(x:usize, limit:usize, multiply_by:usize) -> usize {
    let divs = corrected_divisors(x);
    let divs = divs.iter().filter(|n| *n*&limit>=x).collect::<Vec<_>>();
    divs.iter().map(|n|**n).sum::<usize>()*multiply_by
}