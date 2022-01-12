use std::fs;
use std::collections::HashMap;

fn main() {
    let data = fs::read_to_string("input.txt").expect("Failed to read file");

    let mut x = 0;
    let mut y = 0;

    let mut map : HashMap<[i32;2],i32>= HashMap::new();

    for c in data.chars(){
        let n = map.get(&[x,y]);
        let n : i32 = match n{
            Some(x) => *x,
            None => 0
        };
        
        match c{
            '^' => {y+=1},
            'v' => {y -= 1},
            '>' => {x += 1},
            '<' => {x -= 1},
            _ => continue
        }

        map.insert([x,y], n+1);
    }
    let n = map.get(&[x,y]);
    let n : i32 = match n{
        Some(x) => *x,
        None => 0
    };
    map.insert([x,y], n+1);

    println!("{}",map.len());
}
