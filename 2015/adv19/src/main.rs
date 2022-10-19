// 576 207

use rand::seq::SliceRandom;
use std::collections::HashSet;

const DATA: &str = include_str!("input.txt");

fn main() {
    let initial_molecule: String = String::from(DATA.lines().last().unwrap());
    let substitutions: Vec<(String,String)> = DATA.lines().filter(|l| l.split(" ").count()==3)
        .map(|l|
            {
                let words = l.split(" ").collect::<Vec<_>>();
                let (a,_,c) = (words[0],words[1],words[2]);
                return (String::from(a),String::from(c));
            }
    ).collect::<Vec<_>>();

    let new_molecules = get_evolutions(&initial_molecule, &substitutions);
    println!("First answer: {}",new_molecules.len());

    // //////////////////////////////////////////////////////////////
    // SECOND PART

    /*let mut iters = 0;
    let mut molecules = HashSet::new();
    molecules.insert(String::from("e"));

    loop {
        if molecules.contains(&initial_molecule) {
            break;
        }
        molecules = get_evolutions_multiple(&molecules, &substitutions,initial_molecule.len());
        iters += 1;

        println!("{}",molecules.len());
    }*/

    //println!("Second answer: {iters}");

    // SHOTGUN APPROACH
    /* let mut min = 10000000usize;
    for _ in 0..100 {

    } */

    // VERY LAZY SOLUTION (might infinite loop)
    let ans2 = reverse_substitutions(&initial_molecule, &String::from("e"), &substitutions);

    println!("Second answer: {ans2} or less");

}

fn get_evolutions(molecule:&String, subs:&Vec<(String,String)>) -> HashSet<String> {
    let mut ans: HashSet<String> = HashSet::new();
    for (source,new) in subs {
        let source_len = source.len();
        let positions: Vec<_> = molecule.match_indices(source).collect();
        for (p,_) in positions {
            let mut mol = molecule.clone();
            mol.replace_range(p..p+source_len, &new);
            ans.insert(mol);
        }
    }
    ans
}

fn _get_evolutions_multiple(molecules:&HashSet<String>,subs:&Vec<(String,String)>,max_len:usize) -> HashSet<String> {
    let mut ans = HashSet::new();
    for mol in molecules {
        ans.extend(get_evolutions(mol,subs).iter().filter(|s| s.len()<=max_len).map(|s|s.clone()));
    }
    ans
}

fn get_first_repl(s:&String, rule:&(String,String)) -> String {
    let (source,new) = rule;
    let positions: Vec<_> = s.match_indices(source).collect();
    let p = positions[0].0;
    let mut mol = s.clone();
    mol.replace_range(p..p+source.len(), &new);
    mol
}

fn reverse_substitutions(target:&String,seed:&String,subs:&Vec<(String,String)>) -> usize {
    let mut steps = 0usize;
    let mut mol = target.clone();

    while &mol!=seed {
        let rule = subs.choose(&mut rand::thread_rng()).unwrap();
        let inv_rule = (rule.1.clone(),rule.0.clone());
        if mol.contains(&rule.1) {
            mol = get_first_repl(&mol, &inv_rule);
            steps+=1;
        }
        //println!("{mol}");
    }

    steps
}