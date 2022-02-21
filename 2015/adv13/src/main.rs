use std::collections::{HashMap,HashSet};
use String;
use itertools::Itertools;

fn main() {
    let data: Vec<String>  = include_str!("../input.txt").lines().map(|x| String::from(x)).collect();
    let relations: HashMap<(&str,&str),i32> = data.iter().map(|l|
            match &l.split_whitespace().collect::<Vec<_>>()[..]
            {
                &[a,__,lg,n,_,_,_,_,_,_,b] => {
                    let mut b_iter = b.chars();
                    b_iter.next_back();
                    let b = b_iter.as_str();
                    let abs = n.parse::<i32>().expect("NaN");
                    let num: i32 = match lg {
                        "gain" => { abs },
                        "lose" => { -abs },
                        _ => unreachable!()
                    };
                    ((a,b),num)
                },
                _ => unreachable!()
            }
        ).collect();
    let mut guests: HashSet<&str> = data.iter().map(|x| 
                        *x.split_whitespace().collect::<Vec<_>>().get(0).expect("")).collect();
    guests.insert("You");
    
    let mut values: Vec<i32> = Vec::new();
    for perm in guests.iter().permutations(guests.len()) {
        let mut pairs: Vec<(&str,&str)> = perm.iter()
                                            .zip(perm.iter().skip(1))
                                            .map(|(x,y)| (**x,**y))
                                            .collect();
        pairs.push((perm.get(0).expect("Oob"),**(perm.get(perm.len()-1)).expect("Oob")));

        values.push(pairs.iter().map(|(x,y)| 
            relations.get(&(*x,*y)).unwrap_or(&0) + relations.get(&(y,x)).unwrap_or(&0)
        ).sum())
    }
    println!("{}",values.iter().max().expect(""))
}
