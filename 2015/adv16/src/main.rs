use std::collections::HashMap;

const DATA: &str = include_str!("input.txt");

fn main() {
    let mut parameters: HashMap<String,usize> = HashMap::new();
    parameters.insert(String::from("children"), 3);
    parameters.insert(String::from("cats"),7);
    parameters.insert(String::from("samoyeds"),2);
    parameters.insert(String::from("pomeranians"),3);
    parameters.insert(String::from("akitas"),0);
    parameters.insert(String::from("vizlas"),0);
    parameters.insert(String::from("goldfish"),5);
    parameters.insert(String::from("trees"),3);
    parameters.insert(String::from("cars"),2);
    parameters.insert(String::from("perfumes"),1);
}


struct Sue {
    items: HashMap<String,usize>
}
impl Sue {
    pub fn matches(&self,parameters: HashMap<String,usize>) -> bool {

        for (p,n) in parameters.iter() {
            if self.items.contains_key(p) {
                if self.items.get(p).unwrap() != n {
                    return false;
                }
            }
        }

        true
    }
}