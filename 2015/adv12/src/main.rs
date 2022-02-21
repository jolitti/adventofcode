use regex::Regex;
use serde_json::{self,Value};

fn main() {
    let data = include_str!("../input.txt");
    let num = Regex::new(r"[-]?\d+").unwrap();

    let sum: i32 = num.find_iter(data).map(|x| x.as_str().parse::<i32>().unwrap()).sum();
    println!("{}",sum);

    let j: serde_json::Value = serde_json::from_str(data).expect("Not valid json");

    println!("{}",sum_obj_ignore_red(&j));
}

fn sum_obj_ignore_red(o:&serde_json::Value) -> i64 {
    match o {
        Value::Array(v) => { return v.iter().map(|x| sum_obj_ignore_red(x)).sum() },
        Value::Object(vec) => {
            for (_,v) in vec {
                if let Value::String(x) = v {
                    if x.to_string() == "red" { return 0 }
                }
            }
            return vec.iter().map(|(_,v)| sum_obj_ignore_red(v)).sum()
        },
        Value::Number(x) => {return x.as_i64().unwrap()},
        _ => { println!("{:?}",o) }
    }
    0
}