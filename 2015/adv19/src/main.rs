use std::collections::HashSet;

const DATA: &str = include_str!("input.txt");

fn main() {
    let initial_molecule: String = String::from(DATA.lines().last().unwrap());
    let subs_number = DATA.lines().count() - 1;
    let substitutions: Vec<(String,String)> = DATA.lines().filter(|l| l.split(" ").count()==3)
        .map(|l|
            {
                let words = l.split(" ").collect::<Vec<_>>();
                let (a,_,c) = (words[0],words[1],words[2]);
                return (String::from(a),String::from(c));
            }
    ).collect::<Vec<_>>();

    println!("{substitutions:?}");
}
