// 409147

mod room;
use room::Room;

const INPUT: &str = include_str!("input.txt");

fn main() {

    let total: i32 = INPUT.lines().map(|l| Room::new(l).value()).sum();
    println!("First answer: {total}");
}
