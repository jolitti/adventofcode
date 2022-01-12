use std::fs;

fn main() {
    let data = fs::read_to_string("input.txt").expect("Failed to read file");
    let lines :Vec<&str> = data.split("\n").collect();
    let mut nums = Vec::<[i32;3]>::new();

    for l in lines{
        let mut split = l.split("x");
        let a : i32= split.next().expect("Not found").trim().parse().expect("Not a number");
        let b : i32= split.next().expect("Not found").trim().parse().expect("Not a number");
        let c : i32= split.next().expect("Not found").trim().parse().expect("Not a number");
        let mut x = [a, b ,c];
        x.sort();
        nums.push(x);
    }

    let mut total :i32  = 0;

    /* for [a,b,c] in nums {
        total += 3*a*b + 2*a*c + 2*b*c;
    } */

    for [a,b,c] in nums {
        total += 2*(a+b) + a*b*c;
    }

    println!("{}",total);
}
