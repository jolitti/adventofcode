use std::collections::HashMap;
use std::fs;
use regex::Regex;
use Vec;

fn main() {
    let data = fs::read_to_string("input.txt").expect("File not found");
    let data: Vec<&str> = data.lines().collect();
    let mut lights: HashMap<(i32,i32),i32> = HashMap::new();

    for (i,s) in data.iter().enumerate() {
        println!("{}",i);
        let act = get_action(s);
        let coords = get_all_points(extract_coords(s));

        for c in coords {
            match act {
                // TODO
                Action::On => { *lights.entry(c).or_insert(0) += 1; },
                Action::Off => { 
                    let brightness = lights.get(&c).unwrap_or(&0);
                    if brightness>&0 { *lights.entry(c).or_insert(0) -= 1; }
                 },
                Action::Toggle => { *lights.entry(c).or_insert(0) += 2; },
            }
        };
    }

    let mut tot = 0;
    for ((_,_),state) in lights{
        tot += state;
    }
    println!("The total brightness is {}",tot);
}

fn extract_coords(s:&str) -> [i32;4]{
    let re = Regex::new(r"-?\d+").unwrap();

    let mut ans: [i32;4] = [0,0,0,0];
    let caps = re.captures_iter(s);
    for (i,c) in caps.enumerate(){
        ans[i] = c.get(0).unwrap().as_str().parse().expect("Number not found!");
    };
    return ans;
}

fn get_all_points(pts: [i32;4]) -> Vec<(i32,i32)>{
    let [x1,y1,x2,y2] = pts;
    let area = (x2-x1+1) * (y2-y1+1);
    //println!("{}",area);

    let mut ans: Vec<(i32,i32)> = vec![(0,0);area.try_into().unwrap()];

    let mut index = 0;
    for i in x1..=x2 {
        for j in y1..=y2 {
            ans[index] = (i,j);
            index += 1;
        };
    };

    //println!("{}",index);

    ans
}

enum Action{
    On,
    Off,
    Toggle
}

fn get_action(s:&str) -> Action {

    if s.starts_with("turn on") { Action::On}
    else if s.starts_with("turn off") { Action::Off }
    else { Action::Toggle }
}