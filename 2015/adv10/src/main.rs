use {String};

fn main() {
    // 329356 ? no
    // 252594 ? correct for 40 iter
    // 3579328 for 50 iter
    let mut s = String::from("1113222113");
    
    for i in 0..50 {
        println!("{}", i);
        s = next_ls_str(&s);
    }
    println!("{}",s.len());
}

fn next_ls_str(s:&String) -> String {
    let mut ans = String::new();
    let mut char_ref = s.chars().next().unwrap();
    let mut char_count: u32 = 0;
    for c in s.chars() {
        if c == char_ref {
            char_count += 1;
        }
        else {
            ans += &char_count.to_string();
            ans += &char_ref.to_string();
            char_ref = c;
            char_count = 1;
        }
    };
    ans += &char_count.to_string();
    ans += &char_ref.to_string();
    ans
}