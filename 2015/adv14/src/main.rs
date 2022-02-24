use Vec;
use regex::Regex;

fn main() {
    let data: Vec<&str> = include_str!("../input.txt").lines().collect();

    let part1 = &data.iter().map(|s| Reindeer::new(s).dist_traveled(2503)).max().unwrap();
    println!("Answer to part 1: {}", part1);

    let mut reindeers2: Vec<Reindeer2> = data.iter().map(|s| Reindeer2::new(s)).collect();
    for _ in 0..2503 {
        for r in &mut reindeers2 {
            r.step();
        }
        let head = reindeers2.iter_mut().max_by_key(|r| r.traveled).unwrap().traveled;
        for r in &mut reindeers2 { if r.traveled==head {r.add_point()} }
        /* for r in &reindeers2 { println!("{}",r.traveled); }
        println!("---------") */
    }
    let part2 = reindeers2.iter().map(|r| r.points).max().unwrap();
    println!("Answer to part 2: {}", part2);
}

#[derive(Debug)]
struct Reindeer {
    speed: u32,
    travel_time: u32,
    rest_time: u32
}

impl Reindeer {
    fn new(s:&str) -> Self {
        let nums_re = Regex::new(r"[0-9]+").unwrap();
        let nums: Vec<u32> = nums_re.find_iter(s)
                            .map(|x| x.as_str().parse::<u32>().unwrap())
                            .collect();
        if let &[a,b,c] = &nums[..] {
            return Reindeer{
                speed:a,
                travel_time:b,
                rest_time:c
            }
        }
        else {panic!("Incorrect reindeer string");}
    }

    /// Time of the period and distance traveled
    fn period(&self) -> (u32,u32) {
        let p = self.travel_time + self.rest_time;
        (p, self.speed * self.travel_time)
    }

    /// Distance and time remaining (< period)
    fn dist_rough(&self, secs: u32) -> (u32,u32) {
        let (period, dist) = self.period();
        let (num_of_periods, remaining) = (secs/period, secs%period);
        (num_of_periods*dist,remaining)
    }

    fn dist_traveled(&self, secs: u32) -> u32 {
        let (d1, remaining) = self.dist_rough(secs);
        let d2 = match remaining>=self.travel_time {
            true => { self.speed*self.travel_time },
            false => { self.speed*remaining }
        };
        d1 + d2
    }
}

#[derive(Debug)]
enum TravelState {
    Travel(u32),
    Rest(u32)
}

#[derive(Debug)]
struct Reindeer2 {
    speed: u32,
    travel_time:u32,
    rest_time: u32,

    traveled: u32,
    points: u32,
    state: TravelState
}

impl Reindeer2 {
    fn new(s:&str) -> Self {
        let nums_re = Regex::new(r"[0-9]+").unwrap();
        let nums: Vec<u32> = nums_re.find_iter(s)
                            .map(|x| x.as_str().parse::<u32>().unwrap())
                            .collect();
        if let &[a,b,c] = &nums[..] {
            return Reindeer2{
                speed:a,
                travel_time:b,
                rest_time:c,
                points:0,
                traveled:0,
                state:TravelState::Travel(0)
            }
        }
        else {panic!("Incorrect reindeer string");}
    }

    fn add_point(&mut self) { self.points += 1 }

    fn step(&mut self) {
        match self.state {
            TravelState::Travel(x) => {
                self.traveled += self.speed;
                if x+1>=self.travel_time {
                    self.state = TravelState::Rest(0);
                }
                else {
                    self.state = TravelState::Travel(x+1);
                }
            },
            TravelState::Rest(x) => {
                if x+1>=self.rest_time {
                    self.state = TravelState::Travel(0);
                }
                else {
                    self.state = TravelState::Rest(x+1);
                }
            }
        }
    }
}