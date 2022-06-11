pub use vector2d::Vector2D;

use std::cmp::max;

pub static UP: Vector2D<i32> = Vector2D{x:0,y:1};
pub static DOWN: Vector2D<i32> = Vector2D{x:0,y:-1};
pub static LEFT: Vector2D<i32> = Vector2D{x:-1,y:0};
pub static RIGHT: Vector2D<i32> = Vector2D{x:1,y:0};

pub fn is_inbounds_square(v:&Vector2D<i32>,limit:i32) -> bool 
{
    let dist = max(v.x.abs(), v.y.abs());
    dist <= limit
}

pub fn dir_char_to_vec(c:&char) -> Option<Vector2D<i32>> {
    match c {
        'U' => Some(UP),
        'D' => Some(DOWN),
        'L' => Some(LEFT),
        'R' => Some(RIGHT),
        _ => None
    }
}

pub fn pos_to_digit(v:Vector2D<i32>) -> i32 {
    let (x,y) = (v.x,v.y);

    match (x,y) {
        (-1,1) => 1,
        (0,1) => 2,
        (1,1) => 3,
        (-1,0) => 4,
        (0,0) => 5,
        (1,0) => 6,
        (-1,-1) => 7,
        (0,-1) => 8,
        (1,-1) => 9,
        _ => unreachable!()
    }
}