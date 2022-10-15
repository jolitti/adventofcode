// 40 241

use std::collections::HashMap;

const DATA: &str = include_str!("input.txt");

fn main() {
    let mut parameters: HashMap<String,usize> = HashMap::new();
    parameters.insert(String::from("children"), 3);
    parameters.insert(String::from("cats"),7);
    parameters.insert(String::from("samoyeds"),2);
    parameters.insert(String::from("pomeranians"),3);
    parameters.insert(String::from("akitas"),0);
    parameters.insert(String::from("vizslas"),0);
    parameters.insert(String::from("goldfish"),5);
    parameters.insert(String::from("trees"),3);
    parameters.insert(String::from("cars"),2);
    parameters.insert(String::from("perfumes"),1);

    let mut exact_values: HashMap<String,usize> = HashMap::new();
    exact_values.insert(String::from("children"), 3);
    exact_values.insert(String::from("samoyeds"),2);
    exact_values.insert(String::from("akitas"),0);
    exact_values.insert(String::from("vizslas"),0);
    exact_values.insert(String::from("cars"),2);
    exact_values.insert(String::from("perfumes"),1);
    let mut lower_bounds: HashMap<String,usize> = HashMap::new();
    lower_bounds.insert(String::from("cats"),7);
    lower_bounds.insert(String::from("trees"),3);
    let mut upper_bounds: HashMap<String,usize> = HashMap::new();
    upper_bounds.insert(String::from("pomeranians"),3);
    upper_bounds.insert(String::from("goldfish"),5);

    let sues = DATA.lines().map(|line| 
        Sue::new(line)
    ).collect::<Vec<_>>();

    //println!("{sues:?}");

    print!("First answer: ");
    for (i,s) in sues.iter().enumerate() {
        if s.matches(&parameters) {
            println!("{}",i+1);
            //println!("{s:?}");
        }
    }

    print!("Second answer: ");
    for (i,s) in sues.iter().enumerate() {
        if s.matches2(&exact_values,&lower_bounds,&upper_bounds) {
            println!("{}",i+1);
            //println!("{s:?}");
        }
    }
}

#[derive(Debug)]
struct Sue {
    items: HashMap<String,usize>
}
impl Sue {
    pub fn new(line:&str) -> Sue {
        let mut items: HashMap<String,usize> = HashMap::new();

        let words = line.split_ascii_whitespace().collect::<Vec<_>>();
        let words = words[2..].iter().collect::<Vec<_>>();

        for pair in words.chunks(2) {
            if let [k,n] = pair {
                let key = k.to_string().replace(":","");
                let mut number = n.to_string();
                number = number.replace(",","");
                items.insert(key, number.parse::<usize>().unwrap());
            }
        }

        Sue{items}
    }
    pub fn matches(&self,parameters: &HashMap<String,usize>) -> bool {

        for (p,n) in self.items.iter() {
            if parameters.contains_key(p) {
                if parameters.get(p).unwrap() != n {
                    return false;
                }
            }
            else {
                panic!("{}",p);
            }
        }
        true
    }

    pub fn matches2(
        &self,
        exact: &HashMap<String,usize>,
        lower: &HashMap<String,usize>,
        greater: &HashMap<String,usize>,
    ) -> bool {

        for (p,n) in self.items.iter() {
            if exact.contains_key(p) {
                if exact.get(p).unwrap() != n {
                    return false;
                }
            }
            else if lower.contains_key(p) {
                if lower.get(p).unwrap() >= n {
                    return false;
                }
            }
            else if greater.contains_key(p) {
                if greater.get(p).unwrap() <= n {
                    return false;
                }
            }
            else {
                panic!("{}",p);
            }
        }

        true
    }
}