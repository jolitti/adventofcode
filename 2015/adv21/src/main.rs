use itertools::Itertools;
use std::cmp;

fn main() {

    let sample_player = Combatant{life:8,atk:5,def:5};
    let sample_enemy = Combatant{life:12,atk:7,def:2};
    assert!(sample_player.wins_agains(&sample_enemy));
    assert!(sample_enemy.wins_agains(&sample_player));

    let weapons:Vec<Item> = vec![
        Item{cost:8,dmg:4,def:0},
        Item{cost:10,dmg:5,def:0},
        Item{cost:25,dmg:6,def:0},
        Item{cost:40,dmg:7,def:0},
        Item{cost:74,dmg:8,def:0},
    ];
    let armors:Vec<Item> = vec![
        Item{cost:0,dmg:0,def:0},
        Item{cost:13,dmg:0,def:1},
        Item{cost:31,dmg:0,def:2},
        Item{cost:53,dmg:0,def:3},
        Item{cost:75,dmg:0,def:4},
        Item{cost:102,dmg:0,def:5},
    ];
    let rings_1:Vec<Item> = vec![
        Item{cost:0,dmg:0,def:0},
        Item{cost:25,dmg:1,def:0},
        Item{cost:50,dmg:2,def:0},
        Item{cost:100,dmg:3,def:0},
        Item{cost:20,dmg:0,def:1},
        Item{cost:40,dmg:0,def:2},
        Item{cost:80,dmg:0,def:3},
    ];
    let rings_2:Vec<Item> = vec![
        Item{cost:0,dmg:0,def:0},
        Item{cost:25,dmg:1,def:0},
        Item{cost:50,dmg:2,def:0},
        Item{cost:100,dmg:3,def:0},
        Item{cost:20,dmg:0,def:1},
        Item{cost:40,dmg:0,def:2},
        Item{cost:80,dmg:0,def:3},
    ];

    let mut min_cost: usize = 99999999;
    let mut max_cost = 0usize;
    for x in weapons.iter()
            .cartesian_product(&armors)
            .cartesian_product(&rings_1)
            .cartesian_product(&rings_2) 
            {
                let items = vec![x.0.0.0,x.0.0.1,x.0.1,x.1];
                if items[2].cost == items[3].cost && items[2].cost != 0 { continue; }
                let cost = items.iter().map(|it|it.cost).sum::<usize>();
                let player = Combatant::player_from_items(&items);

                if player.wins_against_2(&ENEMY) && cost < min_cost { 
                    min_cost = cost; 
                    /*for i in &items {
                        print!("{},{},{} ",i.cost,i.dmg,i.def);
                    }
                    println!(". Cost = {cost}");
                    println!("Player attack = {}",player.atk);
                    println!("Player defense = {}",player.def);*/
                }
                if !player.wins_against_2(&ENEMY) && cost > max_cost {
                    max_cost = cost;
                }

    }
    println!("First answer: {min_cost}");
    println!("Second answer: {max_cost}");
}

#[derive(Debug)]
struct Item {
    cost: usize,
    dmg: usize,
    def: usize
}

#[derive(Debug)]
struct Combatant {
    life: usize,
    atk: usize,
    def: usize
}

impl Combatant {
    pub fn player_from_items(items:&Vec<&Item>) -> Combatant {
        let life = 100;
        let atk: usize = items.iter().map(|i|i.dmg).sum();
        let def: usize = items.iter().map(|i|i.def).sum();
        Combatant{life,atk,def}
    }
    pub fn wins_agains(&self,opponent:&Combatant) -> bool {
        let self_dmg = cmp::max(self.atk as i32-opponent.def as i32, 1) as usize;
        let opponent_dmg = cmp::max(opponent.atk as i32-self.def as i32, 1) as usize;
        //println!("{} - {}",self.life*self_dmg,opponent.life*opponent_dmg);
        self.life * self_dmg >= opponent.life * opponent_dmg
    }

    pub fn wins_against_2(&self,opponent:&Combatant) -> bool {
        let mut self_hp: i32 = self.life as i32;
        let mut opponent_hp = opponent.life as i32;
        let self_dmg = cmp::max(self.atk as i32-opponent.def as i32, 1);
        let opponent_dmg = cmp::max(opponent.atk as i32-self.def as i32, 1);

        loop {
            opponent_hp -= self_dmg;
            if opponent_hp <= 0 { return true; }
            self_hp -= opponent_dmg;
            if self_hp <= 0 { return false; }
        }
    }
}

const ENEMY: Combatant = Combatant{life:104,atk:8,def:1};