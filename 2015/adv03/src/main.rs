use std::fs;
use std::collections::HashMap;
use cgmath::Vector2;
use std::mem;

fn main() {
    let data = fs::read_to_string("input.txt").expect("Failed to read file");

    let mut santa1 = Vector2{x:0,y:0};
    let mut santa2 = santa1.clone();
    let mut map : HashMap<Vector2<i32>,i32> = HashMap::new();

    for c in data.chars()
    {
        let dir:Vector2<i32> = match &c {
            '^' => {Vector2{x:0,y:1}},
            '<' => {Vector2{x:-1,y:0}},
            'v' => {Vector2{x:0,y:-1}},
            '>' => {Vector2{x:1,y:0}},
            _ => {Vector2{x:0,y:0}}
        };
        santa1 += dir;
        let old_val:i32 = map.get(&santa1).unwrap_or(&0).clone();

        map.insert(santa1,old_val+1);
        

        mem::swap(&mut santa1,&mut santa2);
    }

    println!("{}",map.len());
}
