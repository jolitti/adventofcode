// 84452 D65C3

mod keypad;
use keypad::Keypad;
use keypad::StartPos;

const NORMAL_KEYS_STR: &str = include_str!("keypads/normal.txt");
const CRAZY_KEYS_STR: &str = include_str!("keypads/crazy.txt");

const EXAMPLE_MOVES: &str = include_str!("example.txt");
const MOVES: &str = include_str!("input.txt");

const START_CHAR: char = '5';

fn main() {
    let example_1 = solve_keypad(NORMAL_KEYS_STR, START_CHAR, EXAMPLE_MOVES);
    let example_2 = solve_keypad(CRAZY_KEYS_STR, START_CHAR, EXAMPLE_MOVES);

    assert_eq!(example_1, String::from("1985"));
    assert_eq!(example_2, String::from("5DB3"));

    let answer_1 = solve_keypad(NORMAL_KEYS_STR, START_CHAR, MOVES);
    let answer_2 = solve_keypad(CRAZY_KEYS_STR, START_CHAR, MOVES);

    println!("First answer: {answer_1}");
    println!("Second answer: {answer_2}");
}

fn solve_keypad(keys:&str,start_char:char,moves:&str) -> String {
    let mut answer = String::new();
    
    let mut keyp = Keypad::new(keys,StartPos::CharPos(start_char));

    for line in moves.trim().lines() {
        for c in line.chars() {
            keyp.char_move(c);
        }
        answer = answer + &keyp.get_char().to_string();
    }

    answer
}