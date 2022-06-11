use std::collections::HashMap;
use vector2d::Vector2D;

pub const UP: Vector2D<i32> = Vector2D{x:0,y:-1};
pub const DOWN: Vector2D<i32> = Vector2D{x:0,y:1};
pub const LEFT: Vector2D<i32> = Vector2D{x:-1,y:0};
pub const RIGHT: Vector2D<i32> = Vector2D{x:1,y:0};

pub enum StartPos {
    VectorPos(Vector2D<i32>),
    CharPos(char)
}

#[derive(Debug)]
pub struct Keypad {
    keys: HashMap<(i32,i32),char>,
    cursor: Vector2D<i32>
}

impl Keypad {
    pub fn new(key_string:&str,start_pos:StartPos) -> Self {
        
        let mut keys_map: HashMap<(i32,i32),char> = HashMap::new();

        for (j,line) in key_string.lines().enumerate() {
            for (i,c) in line.chars().enumerate() {
                if c!=' ' { keys_map.insert((i as i32,j as i32), c); }
            }
        }

        let mut pos = Vector2D::new(0,0);
        
        match start_pos {
            StartPos::VectorPos(v) => { pos = v; },
            StartPos::CharPos(c) => {
                let mut c_pos: Option<(i32,i32)> = Option::None;
                for ((x,y),cc) in &keys_map {
                    if cc == &c {
                        if let Some(_) = c_pos { panic!("Double starting key {c}!") }
                        c_pos = Some((*x,*y));
                    }
                }
                if let Some(v) = c_pos { pos = Vector2D::new(v.0,v.1); }
            }
        }

        Keypad{keys:keys_map, cursor:pos}
    }

    pub fn try_move(&mut self, m:&Vector2D<i32>) {
        let new_pos = self.cursor + *m;
        if self.keys.contains_key(&vec2d_to_tuple(&new_pos)) {
            self.cursor = new_pos;
        }
    }

    pub fn char_move(&mut self, c:char) {
        let next_move = match c {
            'U' => UP,
            'D' => DOWN,
            'L' => LEFT,
            'R' => RIGHT,
            _ => unreachable!()
        };
        self.try_move(&next_move);
    }

    pub fn get_char(&self) -> char {
        *self.keys.get(
            &vec2d_to_tuple(&self.cursor)
        ).expect("Cursor not at valid position!")
    }
}

fn vec2d_to_tuple(v:&Vector2D<i32>) -> (i32,i32) {
    (v.x,v.y)
}