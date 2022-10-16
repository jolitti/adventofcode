const DATA: &str = include_str!("input.txt");

fn main() {

    let mut s1 = Screen::new(DATA);
    for _ in 0..100 { s1.iterate(false); }
    println!("First answer: {}",s1.lights_on());

    let mut s2 = Screen::new(DATA);
    s2.set_corners(true);
    for _ in 0..100 { s2.iterate(true); }
    println!("Second answer: {}",s2.lights_on());
}



struct Screen {
    lights: Vec<Vec<bool>>
}
impl Screen {
    pub fn new(s:&str) -> Screen {
        let mut lights: Vec<Vec<bool>> = Vec::new();
        for line in s.lines() {
            lights.push(line.chars().map(|c| 
                match c {
                    '#' => true,
                    '.' => false,
                    _ => unreachable!()
                }
            ).collect::<Vec<bool>>());
        }
        Screen{lights}
    }

    pub fn lights_on(&self) -> i32 {
        self.lights.iter().flatten().filter(|x| **x).count() as i32
    }

    fn is_on(&self,x:i32,y:i32) -> bool {
        if x<0 || y<0 { return false; }
        let size = self.lights.len() as i32;
        if x>=size || y>=size { return false; }
        self.lights[y as usize][x as usize]
    }

    fn nearby(x:i32,y:i32) -> Vec<(i32,i32)> {
        let mut ans = Vec::new();
        for dx in [-1,0,1] {
            for dy in [-1,0,1] {
                if dx==0 && dy==0 { continue }
                ans.push((x+dx,y+dy));
            }
        }
        ans
    }

    fn nearby_on(&self,x:i32,y:i32) -> i32 {
        let mut ans = 0;
        for (xx,yy) in Screen::nearby(x, y) {
            if self.is_on(xx, yy) { ans+=1; }
        }
        ans
    }

    fn next_pixel_iteration(&self,x:i32,y:i32) -> bool {
        let state = self.is_on(x, y);
        let near_on = self.nearby_on(x, y);

        if state {
            if near_on==2 || near_on ==3 { return true; }
            else { return false; }
        }
        else {
            if near_on==3 { true }
            else { false }
        }
    }

    fn next_pixel_iter_corners_stuck(&self,x:i32,y:i32) -> bool {
        let dims = self.lights.len() as i32;
        if (x==0 || x==dims-1) && (y==0||y==dims-1) {
            true
        }
        else { self.next_pixel_iteration(x, y) }
    }

    // TODO create iterate function
    fn iterate(&mut self,corners_stuck:bool) {
        let mut new_lights: Vec<Vec<bool>> = Vec::new();
        for y in 0..self.lights.len() as i32 {
            let mut new_line = Vec::new();
            for x in 0..self.lights[0].len() as i32 {
                if corners_stuck {
                    new_line.push(self.next_pixel_iter_corners_stuck(x, y));
                }
                else {
                    new_line.push(self.next_pixel_iteration(x, y));
                }
            }
            new_lights.push(new_line);
        }
        self.lights = new_lights;
    }

    fn set_corners(&mut self, value: bool) {
        let last_index = self.lights.len() as usize - 1 ;
        for y in [0,last_index] {
            for x in [0,last_index] {
                self.lights[y][x] = value;
            }
        }
    }
}