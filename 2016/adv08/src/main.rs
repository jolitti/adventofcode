// 116 UPOJFLBCEZ

mod screen;
mod test;

use screen::Screen;

const INPUT: &str = include_str!("input.txt");

fn main() {
    let mut screen1 = Screen::new();

    for s in INPUT.lines() {
        screen1.execute_str(s);
    }

    let ans1 = screen1.lit_pixels();

    println!("First answer: {ans1}");

    println!("Second answer:");
    println!("{}",screen1.representation());
}
