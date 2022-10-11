// 18965440 15862900

mod cookie;
use std::cmp;
const SAMPLE_DATA: &str = include_str!("input00.txt");
const DATA: &str = include_str!("input.txt");

fn main() {
    println!("Hello world!");
    
    let sample_ingredients = cookie::parse_ingredient_values(SAMPLE_DATA);
    let sample_answer = get_max_2(sample_ingredients);
    println!("Sample answer = {sample_answer}");

    let ingredients = cookie::parse_ingredient_values(DATA);
    let answer1 = get_max_4(&ingredients);
    println!("First answer = {answer1}");

    let answer2 = get_max_4_500_cal(&ingredients);
    println!("Second answer = {answer2}");

    

    //let score = cookie::calculate_score_2(44,56,ingredients);
    //println!("{score}");
}

fn get_max_2(ingredients:Vec<[isize;5]>) -> isize {

    let mut max = 0isize;
    for a in 0..=100 {
        for b in 0..=100 {
            if a+b == 100 {
                let new_score = cookie::calculate_score(vec![a,b],&ingredients);
                max = cmp::max(max, new_score);
            }
        }
    }
    max
}

fn get_max_4(ingredients:&Vec<[isize;5]>) -> isize {
    let mut max = 0isize;
    for a in 0..=100 {
        for b in 0..=100 {
            for c in 0..=100 {
                for d in 0..=100 {
                    if a+b+c+d == 100 {
                        let new_score = cookie::calculate_score(vec![a,b,c,d],&ingredients);
                        max = cmp::max(max, new_score);                    
                    }
                }
            }
        }
    }
    max
}

fn get_max_4_500_cal(ingredients:&Vec<[isize;5]>) -> isize {
    let mut max = 0isize;
    for a in 0..=100 {
        for b in 0..=100 {
            for c in 0..=100 {
                for d in 0..=100 {
                    if a+b+c+d == 100 {
                        let new_score = cookie::calculate_score_500_cal(vec![a,b,c,d],&ingredients);
                        max = cmp::max(max, new_score);                    
                    }
                }
            }
        }
    }
    max
}