fn main() {
    let commands = include_str!("../input.txt").lines().collect::<Vec<&str>>();
    let mut rows: Vec<Vec<String>> = Vec::new();
    let mut cols: Vec<String> = Vec::new();
    let mut row = "x0";
    for (pos, e) in commands.iter().enumerate() {
        if pos == 0 || pos == 1 {
            continue;
        }
        let mut v1 = e.split(" ").collect::<Vec<&str>>();
        v1.retain(|&i| i != "");
        let tmp = v1[0].split("-").collect::<Vec<&str>>();
        if tmp[1] != row {
            row = tmp[1];
            rows.push(cols.clone());
            cols.clear();
        }
        let a: i32 = v1[1].replace("T", "").parse().unwrap();
        if tmp[1] == "x0" && tmp[2] == "y0" {
            cols.push("(.)".to_string());
        }
        else if tmp[1] == "x34" && tmp[2] == "y0" {
            cols.push(" G ".to_string());
        }
        else if v1[2] == "0T" {
            cols.push(" _ ".to_string());
        }
        else if a >= 100 {
            cols.push(" # ".to_string());
        } else {
            cols.push(" . ".to_string());
        }
        
    }
    rows.push(cols.clone());
    for i in 0..rows[0].len() {
        for e in rows.iter() {
            print!("{}", e[i]);
        }
        println!("");
    }
    println!("Answer equals to: 14 + 32 + 20 + 7 + 32 * 5 = 233 (Manualy counted)");
}

