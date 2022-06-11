use vector2d::Vector2D;
mod vecutil;
mod keypad;

static EXAMPLE: &str = include_str!("example.txt");
static DATA: &str = include_str!("input.txt");

fn former_main() {
    print_solution(EXAMPLE);
    print_solution(DATA);
}

fn print_solution(s:&str) {
    let answer = solve(s);
    println!("{answer}");
}

fn solve(s:&str) -> i32 {
    let mut pos = Vector2D::new(0,0);
    let mut answer = 0;

    for line in s.trim().lines() {
        let (number,new_pos) = get_keypad_num(line, &pos);
        pos = new_pos;
        answer = answer*10 + number;
    }

    answer
}

fn get_keypad_num(s:&str, start_pos: &Vector2D<i32>) -> (i32, Vector2D<i32>) {
    let mut position = Vector2D{..*start_pos};

    for c in s.chars() {
        let next_move = vecutil::dir_char_to_vec(&c).unwrap();
        let next_pos = position + next_move;

        if vecutil::is_inbounds_square(&next_pos, 1) {
            position = position + next_move;
        }
    }

    (vecutil::pos_to_digit(position), position)
}