use std::fs;

fn main(){
    let data = fs::read_to_string("src/input.txt").expect("Failed to read file");
    let mut index = 0;

    for (i,c) in data.chars().enumerate(){
        match c {
            '(' => {index+=1;},
            ')' => {index-=1;},
            _ => {panic!("Invalid char!")}
        }
        if index < 0 {
            println!("{}",i+1);
            break;
        }
    }

    println!("{}",index);
}
