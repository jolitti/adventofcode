use std::collections::HashMap;
use std::fs;
use String;

fn main() {
    let data = fs::read_to_string("input.txt").expect("Failed to open file");
    let data: Vec<String> = data.lines().map(|x| String::from(x)).collect();
    let mut wires: HashMap<String,u16> = HashMap::new();

    for d in data {
        let (op,target) = get_op(&d);
        let result = match op {
            BitOp::Not(x) => { 
                let num = wires.get(&x).unwrap_or(&0);
                !num
            },
            BitOp::And(x,y) => {
                let (a,b) = (wires.get(&x).unwrap_or(&0),wires.get(&y).unwrap_or(&0));
                a & b
            },
            BitOp::And1(x) => {
                let num = wires.get(&x).unwrap_or(&0);
                1 & num
            },
            BitOp::Or(x,y) => {
                let (a,b) = (wires.get(&x).unwrap_or(&0),wires.get(&y).unwrap_or(&0));
                a | b
            },
            BitOp::Lshift(x,y) => {
                let x = wires.get(&x).unwrap_or(&0);
                x << y
            },
            BitOp::Rshift(x,y) => {
                let x = wires.get(&x).unwrap_or(&0);
                x >> y
            },
            BitOp::Assign(x) => {
                let num = wires.get(&x).unwrap_or(&0);
                *num
            },
            BitOp::Literal(x) => {
                x
            }
        };

        wires.insert(target, result);
    }

    println!("{}",wires.get(&String::from("a")).unwrap_or(&0));
}

#[derive(Debug)]
enum BitOp {
    Not(String),
    Or(String,String),
    And(String,String),
    And1(String),
    Lshift(String,u16),
    Rshift(String,u16),
    Assign(String),
    Literal(u16)
}

fn get_op(s:&String) -> (BitOp,String){
    let words: Vec<String> = s.split(" ").map(|x| String::from(x)).collect();
    let target = words[words.len()-1].clone();

    return match &words[..] {
        [a,_,_] => {
            if !a.parse::<u16>().is_ok() {return (BitOp::Assign(a.clone()),target)}
            let value: u16 = a.parse().expect("Not a number");
            (BitOp::Literal(value),target)
        },
        [_,b,_,d] => {
            (BitOp::Not(b.clone()),d.clone())
        },
        [a,b,c,_,e] => {
            let (a,c,e) = (a.clone(),c.clone(),e.clone());
            if a == "1" {return (BitOp::And1(c),e)}
            match b.as_str() {
                "AND" => (BitOp::And(a,c),e),
                "OR" => (BitOp::Or(a,c),e),
                "LSHIFT" => (BitOp::Lshift(a,c.parse().expect("NaN")),e),
                "RSHIFT" => (BitOp::Rshift(a,c.parse().expect("NaN")),e),

                _ => panic!()
            }
        },
        _ => {panic!()}
    }
}