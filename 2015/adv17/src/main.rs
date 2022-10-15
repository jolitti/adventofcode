// 1638

const DATA: &str = include_str!("input.txt");

fn main() {
    let containers = DATA.lines().map(|l| l.parse::<usize>().unwrap()).collect::<Vec<_>>();
    let mut answer1: usize = 0;
    for i in 0..2usize.pow(containers.len() as u32) {
        let mask = format!("{i:b}");
        if subset(&containers, mask).iter().sum::<usize>()==150 { answer1 += 1; };
    }
    println!("First answer: {answer1}");

    let mut min_cont: usize = containers.len();
    let mut min_cont_ways: usize = 0;
    for i in 0..2usize.pow(containers.len() as u32) {
        let mask = format!("{i:b}");
        let subs = subset(&containers, mask);
        if subs.iter().sum::<usize>()==150 {
            let num_of_cont = subs.len();
            if num_of_cont < min_cont {
                min_cont = num_of_cont;
                min_cont_ways = 1;
            }
            else if num_of_cont == min_cont {
                min_cont_ways += 1;
            }
        }
    }
    println!("Second answer: {min_cont_ways}");
}

fn subset(v:&Vec<usize>,mask:String) -> Vec<usize> {
    let length = v.len();
    let mask = format!("{:0>width$}",mask,width=length);
    //println!("{mask}");
    let mut ans: Vec<usize> = Vec::new();
    for (num,bit) in v.iter().zip(mask.chars()) {
        if bit=='1' {
            ans.push(*num);
        }
    }
    ans
}