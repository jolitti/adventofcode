use regex::Regex;

const RECT_STR: &str = "rect";
const ROTATE_ROW_STR: &str = "rotate row";
const ROTATE_COL_STR: &str = "rotate column";

pub struct Screen {
    pixels: Vec<Vec<bool>>
}

pub enum ScreenCommand {
    Rect(usize,usize),
    RotateRow(usize,usize),
    RotateCol(usize,usize)
}

impl Screen {

    const SIZE: (usize,usize) = (50,6);

    pub fn new() -> Screen {
        let mut pixels: Vec<Vec<bool>> = Vec::new();
        let (x_size,y_size) = Screen::SIZE;

        for _ in 0..x_size {
            let col = vec![false;y_size];
            pixels.push(col);
        }

        Screen{pixels}
    }

    pub fn execute<T: Into<Option<ScreenCommand>>>(&mut self, cmd: T) {
        let opt_cmd = cmd.into();

        if let Some(command) = opt_cmd {
            match command {
                ScreenCommand::Rect(x_len,y_len) => {
                    for x in 0..x_len {
                        for y in 0..y_len {
                            self.pixels[x][y] = true;
                        }
                    }
                },
                ScreenCommand::RotateCol(x_pos,amount) => {
                    self.pixels[x_pos].rotate_right(amount);
                },
                ScreenCommand::RotateRow(y_pos,amount) => {
                    let mut row = vec![false;Screen::SIZE.0];
                    for x in 0..Screen::SIZE.0 {
                        row[x] = self.pixels[x][y_pos];
                    }
                    row.rotate_right(amount);
                    for x in 0..Screen::SIZE.0 {
                        self.pixels[x][y_pos] = row[x];
                    }
                }
            }
        }
    }

    pub fn execute_str(&mut self, s:&str) {
        let cmd = get_command(s);
        self.execute(cmd);
    }

    pub fn lit_pixels(&self) -> usize {
        self.pixels.iter().flatten().filter(|p| **p).count()
    }

    pub fn representation(&self) -> String {
        let mut ans = String::new();
        let (x_size,y_size) = Screen::SIZE;

        for y in 0..y_size {
            for x in 0..x_size {
                if self.pixels[x][y] { ans.push('#'); }
                else { ans.push(' '); }
            }
            ans.push('\n');
        }

        ans
    }
}

pub fn get_command(s:&str) -> Option<ScreenCommand> {
    let number_pattern = Regex::new(r"\d+").unwrap();
    let nums = number_pattern
                .find_iter(s)
                .map(|m| m.as_str().parse::<usize>().unwrap())
                .collect::<Vec<_>>();

    if nums.len() != 2 { return None; }
    let (a,b) = (nums[0],nums[1]);

    if s.starts_with(RECT_STR) { return Some(ScreenCommand::Rect(a,b)) }
    else if s.starts_with(ROTATE_ROW_STR) { return Some(ScreenCommand::RotateRow(a,b)) }
    else if s.starts_with(ROTATE_COL_STR) { return Some(ScreenCommand::RotateCol(a,b)) }

    None
}