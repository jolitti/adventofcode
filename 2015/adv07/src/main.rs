use Vec;
use String;
use std::collections::HashMap;

fn main() {
    let mut data:Vec<String> = include_str!("../input_part_2.txt")
                                .lines()
                                .map(|x| String::from(x))
                                .collect();
    
    let mut computed_values: HashMap<String,u16> = HashMap::new();

    while !data.is_empty() {
        let mut data2: Vec<String> = Vec::new();

        for d in data {
            let wiring: Vec<&str> = d.split(" ").collect();

            match wiring[..] {
                [a,_,b] => {
                    // Literal
                    if let Ok(x) = a.parse::<u16>() { 
                        computed_values.insert(String::from(b), x); 
                    }
                    // Assignment
                    else if computed_values.contains_key(a) {
                        computed_values.insert(String::from(b),*computed_values.get(a)
                                            .expect("not found"));
                    }
                    // Assignment to not yet computed value
                    else {data2.push(d.clone());}
                },
                [_,a,_,b] => {
                    // (Not) an already known value
                    if computed_values.contains_key(a) {
                        let new_val = !computed_values.get(a).unwrap();
                        computed_values.insert(String::from(b), new_val);
                    }
                    else { data2.push(d.clone()) }
                },
                [a,op,b,_,c] => {
                    if let Ok(x) = a.parse::<u16>() { computed_values.insert(String::from(a), x); }
                    if let Ok(x) = b.parse::<u16>() { computed_values.insert(String::from(b), x); }

                    if !has_been_computed(&[a,b], &computed_values) { data2.push(d.clone()) }
                    else {
                        let (a_value, b_value) = (computed_values.get(a).unwrap(),
                                                computed_values.get(b).unwrap());
                        let result = match op {
                            "AND" => {a_value & b_value},
                            "OR" => { a_value | b_value },
                            "LSHIFT" => { a_value << b_value },
                            "RSHIFT" => { a_value >> b_value },
                            _ => unreachable!()
                        };
                        computed_values.insert(String::from(c), result);
                    }
                },
                _ => unreachable!()
            }
        }

        data = data2;
    }

    println!("{}",computed_values.get(&String::from("a")).expect("Not found"));

}

fn has_been_computed(wires:&[&str],wires_map:&HashMap<String,u16>) -> bool {
    for w in wires {
        let s = String::from(*w);
        if !wires_map.contains_key(&s) {return false}
    }
    true
}
