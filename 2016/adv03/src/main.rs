// 983 1836

const TRIANGLES_STR: &str = include_str!("input.txt");

fn main() {
    
    let count1 = first_part(&TRIANGLES_STR);
    println!("First part: {count1}");

    let count2 = second_part(&TRIANGLES_STR);
    println!("Second part: {count2}");

}

fn first_part(triangle_list:&str) -> u32 {
    let mut count: u32 = 0;

    for triangle in triangle_list.trim().lines() {
        let mut numbers: Vec<u32> = 
            triangle.split_whitespace()
            .map(|s| s.parse::<u32>().unwrap())
            .collect();

        if is_valid_triangle(&mut numbers) {
            count += 1;
        }
    }

    count
}

fn second_part(triangle_list:&str) -> u32 {
    let mut count: u32 = 0;
    let mut line_iter = triangle_list.trim().lines().peekable();
    let (mut va, mut vb, mut vc): (Vec<u32>,Vec<u32>,Vec<u32>) = 
        (Vec::new(),Vec::new(),Vec::new());

    while line_iter.peek().is_some() {
        for _ in 0..3 {
            let line = line_iter.next();

            let numbers: Vec<u32> = 
                line.unwrap().split_whitespace()
                .map(|s| s.parse::<u32>().unwrap())
                .collect();

            va.push(numbers[0]);
            vb.push(numbers[1]);
            vc.push(numbers[2]);
        }

        if is_valid_triangle(&mut va) {count+=1};
        if is_valid_triangle(&mut vb) {count+=1};
        if is_valid_triangle(&mut vc) {count+=1};

        va.clear();
        vb.clear();
        vc.clear();
    }

    count
}

fn is_valid_triangle(v:&mut Vec<u32>) -> bool {
    for _ in 0..3 {
        v.rotate_right(1);
        if !first_less_than_sum(&v) {
            return false
        }
    }

    true
    
}

fn first_less_than_sum(candidate:&Vec<u32>) -> bool {

    if let &[a,b,c] = &candidate[..] {
        a < b+c
    }
    else {panic!("Not a triangle!")}

}

#[test]
fn test_triangle() {
    assert!(is_valid_triangle(vec![2,3,4]));
    assert!(!is_valid_triangle(vec![5,10,25]));
}