// 209 136

use vector2d::Vector2D;
use std::ops::Neg;
use std::ops::Mul;

use std::collections::HashSet;

static DATA: &str = include_str!("input.txt");
static EXAMPLE_1: &str = "R2, L3";
static EXAMPLE_2: &str = "R2, R2, R2";
static EXAMPLE_3: &str = "R8, R4, R4, R8";

fn main() {
    solve_1(EXAMPLE_1);
    solve_1(EXAMPLE_2);
    solve_1(DATA);

    println!("");

    solve_2(EXAMPLE_3);
    solve_2(DATA);
}

fn solve_1(data: &str) {
    let instructions: Vec<&str> = data.trim().split(", ").collect();

    let mut position: Vector2D<i32> = Vector2D::new(0,0);
    let mut facing: Vector2D<i32> = Vector2D::new(0,1);

    // println!("{instructions:?}");

    for instr in instructions {
        let rotation = &instr[0..1];
        let steps = &instr[1..];
        let steps: i32 = steps.parse().unwrap();

        facing = rotate(
            &facing, 
            match rotation {
                "R" => RotDir::RIGHT,
                "L" => RotDir::LEFT,
                _ => unreachable!()
            }
        );
        
        let tot_steps = facing.mul(steps);
        position = position + tot_steps;
    }

    let distance = position.x.abs() + position.y.abs();
    println!("Final distance: {distance}");
}

fn solve_2(data: &str) {
    let instructions: Vec<&str> = data.trim().split(", ").collect();

    let mut visited: HashSet<(i32,i32)> = HashSet::new();
    let mut position: Vector2D<i32> = Vector2D::new(0,0);
    let mut facing: Vector2D<i32> = Vector2D::new(0,1);

    // println!("{instructions:?}");

    'outer_loop: for instr in instructions {
        let rotation = &instr[0..1];
        let steps = &instr[1..];
        let steps: i32 = steps.parse().unwrap();

        facing = rotate(
            &facing, 
            match rotation {
                "R" => RotDir::RIGHT,
                "L" => RotDir::LEFT,
                _ => unreachable!()
            }
        );
        
        for _ in 0..steps {
            let pos_tuple = (position.x,position.y);
            if let Some(_) = visited.get(&pos_tuple) { break 'outer_loop; }
            else { visited.insert(pos_tuple); }

            position = position + facing;
        }
    }

    let distance = position.x.abs() + position.y.abs();
    println!("First revisit: {distance}");
}

enum RotDir {
    LEFT,
    RIGHT
}

fn rotate<T>(v:&Vector2D<T>,dir: RotDir) -> Vector2D<T>
where T: Neg<Output = T> + Copy
{
    let (xx,yy) = (v.x, v.y);
    match dir {
        RotDir::LEFT => {Vector2D{x:-yy,y:xx}},
        RotDir::RIGHT => {Vector2D{x:yy,y:-xx}}
    }
}