use std::collections::HashMap;
use {String, Vec};

pub struct WireSystem {
    wires: HashMap<String,Wire>
}

impl WireSystem {
    pub fn new() -> Self {
        WireSystem {wires: HashMap::new()}
    }

    pub fn get_wire(&self, s:&String) -> u16 {
        self.wires.get(s).expect("Wire not found").get_val(&self.wires)
    }

    pub fn add_line(&mut self, s: &String) {
        let words: Vec<String> = s.split(" ").map(|x| String::from(x)).collect();
        let target = words[words.len()-1].clone();

        self.wires.insert(target, Wire{ source: 
            match &words[..] {
                [a,_,_] => { match a.parse::<u16>() {
                    Err(_) => Gate::Assign(a.clone()),
                    Ok(x) => Gate::Literal(x)
                } },

                [_,b,_,_] => { Gate::Not(b.clone()) },

                [a,verb,b,_,_] => { 
                    let (a,b) = (a.clone(),b.clone());
                    let b_num = b.parse::<u16>();
                    match verb.as_str() {
                    "AND" =>  {Gate::And(a,b)},
                    "OR" => Gate::Or(a,b),
                    "LSHIFT" => Gate::Lshift(a,b_num.expect("NaN")),
                    "RSHIFT" => Gate::Rshift(a,b_num.expect("NaN")),
                    _ => unreachable!()
                }
                }

                _ => {unreachable!()}
            }
        });
    }
}

#[derive(Debug)]
struct Wire {
    source: Gate
}

impl Wire {
    fn get_val(&self,wires:&HashMap<String,Wire>) -> u16 {
        println!("{:?}",self);
        self.source.get_val(wires)
    }
}

#[derive(Debug)]
enum Gate {
    And(String,String),
    Or(String,String),
    Not(String),
    Lshift(String,u16),
    Rshift(String,u16),
    Assign(String),
    Literal(u16),

    //And1(String)
}

impl Gate {
    fn get_val(&self, wires:&HashMap<String,Wire>) -> u16 {
        match self {
            Gate::Literal(x) => x.clone(),
            Gate::Assign(x) => wires.get(x).expect("Not found").get_val(wires),
            Gate::Not(x) => !wires.get(x).expect("Not found").get_val(wires),
            Gate::And(a,b) => {
                let (a,b) = (wires.get(a).expect("Not Found").get_val(wires),
                wires.get(b).expect("Not found").get_val(wires));
                a & b
            },
            Gate::Or(a,b) => {
                let (a,b) = (wires.get(a).expect("Not Found").get_val(wires),
                wires.get(b).expect("Not found").get_val(wires));
                a | b
            },
            Gate::Lshift(x,n) => wires.get(x).expect("Not found").get_val(wires) << n,
            Gate::Rshift(x,n) => wires.get(x).expect("Not found").get_val(wires) >> n,

            //Gate::And1(x) => wires.get(x).expect("Not found").get_val(wires) & 1
        }
    }
}