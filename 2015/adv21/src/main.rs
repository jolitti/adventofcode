use itertools::Itertools;

fn main() {

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

    for x in weapons.iter()
            .cartesian_product(&armors)
            .cartesian_product(&rings_1)
            .cartesian_product(&rings_2) 
            {

                println!("{x:?}");

    }
}

#[derive(Debug)]
struct Item {
    cost: usize,
    dmg: usize,
    def: usize
}



