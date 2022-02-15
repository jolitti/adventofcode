mod electro;
use electro::WireSystem;
use String;
use std::fs;

fn main() {
    let data = fs::read_to_string("input.txt").expect("Failed to open file");
    let data: Vec<String> = data.lines().map(|x| String::from(x)).collect();
    let mut ws = WireSystem::new();
    ws.add_line(&String::from("1 -> 1"));

    for d in data { ws.add_line(&d) }
    println!("{}",ws.get_wire(&String::from("a")));
}