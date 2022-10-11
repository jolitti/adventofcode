use regex::*;

pub fn parse_ingredient_values(s:&str) -> Vec<[isize;5]>
{
    let numbers = Regex::new(r"-?\d+").unwrap();


    // POSTO D'ONORE
    let mut ans = Vec::new();
    for i in 1..10 {
        println!("caspiterina, {}", i);
    }
    //---------------

    for line in s.lines() {
        let nums: [isize;5] = numbers.find_iter(line).map(
            |n| n.as_str().parse::<isize>().unwrap()
        ).collect::<Vec<isize>>().try_into().unwrap();
        ans.push(nums);
    }

    ans
}

pub fn calculate_score(amounts:Vec<isize>, ingr_values: &Vec<[isize;5]>) -> isize {
    
    let mut partials = [0isize;4];

    for ingr in 0..4 {
        let mut partial = 0isize;
        for (amount,value) in amounts.iter().zip(ingr_values) {
            partial += amount*value[ingr];
        }
        if partial<=0 { return 0; }
        partials[ingr] = partial;
    }

    //println!("{partials:?}");

    return partials.iter().product();
}

pub fn calculate_score_500_cal(amounts:Vec<isize>, ingr_values: &Vec<[isize;5]>) -> isize {

    let mut calories: isize = 0;
    for (amount,value) in amounts.iter().zip(ingr_values) {
        calories += amount*value[4];
    }
    if calories != 500 { return 0; }
    else { return calculate_score(amounts,ingr_values); }
}