use std::collections::{HashMap,HashSet};
use Vec;
use itertools::Itertools;

fn main() {
    let data: Vec<&str> = include_str!("../input.txt").lines().collect();
    let mut cities: HashSet<&str> = HashSet::new();
    let mut dists: HashMap<(&str,&str),u32> = HashMap::new();

    for d in &data {
        let words: Vec<&str> = d.split(" ").collect();
        match words[..] {
            [a,_,b,_,val] => {
                cities.insert(a);
                cities.insert(b);
                let val = val.parse::<u32>().expect("NaN");
                dists.insert(as_key(a,b), val);
            }
            _ => unreachable!()
        }
    }
    println!("{:?}",cities);
    let cities_num = cities.len();
    let min: u32 =  cities.iter().permutations(cities_num).map(|perm|
                        perm.iter().zip(perm.iter().skip(1))
                        .map(|(a,b)| dists.get(&as_key(a,b)).unwrap()).sum()).min().unwrap();
    let max: u32 =  cities.iter().permutations(cities_num).map(|perm|
                        perm.iter().zip(perm.iter().skip(1))
                        .map(|(a,b)| dists.get(&as_key(a,b)).unwrap()).sum()).max().unwrap();
    /* let mut min: u32 = 1000000000;
    for perm in cities.iter().permutations(cities_num) {
        println!("-----------");
        for (a,b) in perm.iter().zip(perm.iter().skip(1)) {
            println!("{:?}",(a,b));
        }
    } */

    
    println!("min: {}, max: {}",min,max);
}

fn as_key<'a>(a:&'a str, b:&'a str) -> (&'a str, &'a str){
    if a<b { return (a,b) }
    (b,a)
}