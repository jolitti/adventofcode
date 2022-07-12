// 409147 991

mod room;
use room::Room;

const INPUT: &str = include_str!("input.txt");
const TARGET_ROOM: &str = "northpole object storage ";

fn main() {

    let total: i32 = INPUT.lines().map(|l| Room::new(l).value()).sum();
    println!("First answer: {total}");

    let real_rooms = INPUT.lines()
                    .map(|l| Room::new(l))
                    .filter(|r| r.is_valid())
                    .collect::<Vec<_>>();

    for r in real_rooms {
        if r.real_name() == TARGET_ROOM {
            println!("{}{} {}",r.real_letters,r.code,r.real_name());
        }
    }
}
