use std::cmp::Reverse;
use itertools::Itertools;

const INPUT: &str = include_str!("input.txt");
const SAMPLE: &str = include_str!("sample.txt");

fn main() {
    let sample1 = part1(SAMPLE);
    assert_eq!(sample1,24_000);
    
    let sample2 = part2(SAMPLE);
    assert_eq!(sample2,45_000);

    let (ans1,ans2) = (part1(INPUT),part2(INPUT));
    println!("Answer to part 1: {ans1}");
    println!("Answer to part 2: {ans2}");
}

fn part1(data: &str) -> usize {
    data
        .lines()
        .map(|l| l.parse::<usize>().ok())
        .batching(|num_iter| 
                  num_iter.map_while(|n| n).sum1::<usize>()
                  )
        .max()
        .unwrap()
}

fn part2(data: &str) -> usize {
    data
        .lines()
        .map(|l| l.parse::<usize>().ok())
        .batching(|num_iter|
                  num_iter.map_while(|n| n).sum1::<usize>()
                  )
        .map(Reverse)
        .k_smallest(3)
        .map(|x| x.0)
        .sum()
}
