static TOTAL_SPOONS: u64 = 100;

use Vec;
use itertools::Itertools;
use std::{iter,cmp};
use regex::Regex;

#[derive(Debug)]
struct Ingredient {
    capacity: i64,
    durability: i64,
    flavor: i64,
    texture: i64,
    calories: i64
}
impl Ingredient {
    fn new(s:&str) -> Self {
        //println!("{s}");
        let nums = Regex::new(r"-?\d+").unwrap();
        let nums: Vec<i64> = nums.find_iter(s)
                                .map(|x| x.as_str()
                                .parse::<i64>().expect("NaN"))
                                .collect();
        //println!("{nums:?}");
        match &nums[..] {
            &[a,b,c,d,e] => {
                Ingredient{
                    capacity: a,
                    durability: b,
                    flavor: c,
                    texture: d,
                    calories: e
                }
            }
            _ => panic!("Invalid ingredient string")
        }
    }
    fn to_array(&self) -> [i64;5] {
        [
            self.capacity,
            self.durability,
            self.flavor,
            self.texture,
            self.calories
        ]
    }
}

fn main() {
    let data: Vec<&str> = include_str!("../input00.txt").lines().collect();
    let ingrs: Vec<Ingredient> = data.iter().map(|s| Ingredient::new(s)).collect();


    let x = vec_int_prod(&ingrs[0].to_array(),44);
    println!("{x:?}");

    /* let max = all_combinations(ingrs.len() as u64, 100).map(|comb| {
                    //println!("{comb:?}");
                    recipe_points(&comb, &ingrs)
                }
                ).max().unwrap();

    println!("{max}") */
}

fn recipe_points(spoons: &Vec<u64>, ingredients: &Vec<Ingredient>) -> u64 {
    let mut pts: [i64;5] = [0;5];
    for (sp,ingr) in spoons.iter().zip(ingredients.iter()) {
        pts = vec_sum(&pts,&vec_int_prod(&ingr.to_array(),*sp as i64));
    }
    pts.iter().map(|x| *cmp::max(x,&0) as u64).product()
}

fn all_combinations1(n: u64) -> impl Iterator<Item = Vec<u64>> {
    itertools::repeat_n(0..=TOTAL_SPOONS, n as usize)
        .multi_cartesian_product()
        .filter(|v| v.iter().sum::<u64>() == TOTAL_SPOONS)
}


fn cons<T: Copy>(x: T, xs: &[T]) -> Vec<T> {
    let mut v = Vec::with_capacity(xs.len() + 1);
    v.push(x);
    v.extend(xs);
    v
}

fn all_combinations(n: u64, cap: u64) -> Box<dyn Iterator<Item = Vec<u64>>> {
    assert_ne!(n, 0);
    if n == 1 {
        Box::new(iter::once(vec![cap]))
    } else {
        Box::new((0..=cap).flat_map(move |x| all_combinations(n - 1, cap - x).map(move |xs| cons(x, &xs))))
    }
}

fn vec_sum(a:&[i64;5],b:&[i64;5]) -> [i64;5] {
    let [a1,a2,a3,a4,a5] = a;
    let [b1,b2,b3,b4,b5] = b;
    [a1+b1,a2+b2,a3+b3,a4+b4,a5+b5]
}
fn vec_int_prod(a:&[i64;5],x:i64) -> [i64;5] {
    let [a1,a2,a3,a4,a5] = a;
    [a1*x,a2*x,a3*x,a4*x,a5*x]
}