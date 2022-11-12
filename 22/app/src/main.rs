fn main() {
    let commands = include_str!("../input.txt").lines().collect::<Vec<&str>>();
    let mut count = 0;
    for (pos, e) in commands.iter().enumerate() {
        if pos == 0 || pos == 1 {
            continue;
        }
        let mut v1 = e.split(" ").collect::<Vec<&str>>();
        v1.retain(|&i| i != "");
        if v1[2] != "0T" {
            for n in 2..commands.len() {
                if n == pos {
                    continue;
                }
                let mut v2 = commands[n].split(" ").collect::<Vec<&str>>();
                v2.retain(|&i| i != "");

                if v1[1] != v2[1] || v1[2] != v2[2] || v1[3] != v2[3] || v1[4] != v2[4] {
                    let a: i32 = v1[2].replace("T", "").parse().unwrap();
                    let b: i32 = v2[3].replace("T", "").parse().unwrap();
                    if a <= b {
                        count += 1;
                    }
                }
            }
        }
    }
    println!("Number of pairs is {}", count);
}
