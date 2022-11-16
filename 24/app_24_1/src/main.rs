extern crate itertools;
use std::collections::VecDeque;
use std::convert::TryInto;
use itertools::Itertools;
use std::io::{stdin,stdout,Write};

fn main() {
    let lines = include_str!("../input.txt").lines().collect::<Vec<&str>>();
    let mut grid: Vec<Vec<char>> = Vec::new();

    for e in lines.iter() {
        let v_tmp = e.chars().collect::<Vec<char>>();
        grid.push(v_tmp);
    }

    for e in grid.iter() {
        println!("{:?}", e);
    }

    let result = bfs(grid);
    
    println!("{result}");
}

#[derive(Clone)]
struct Point {
    pos_x: i32,
    pos_y: i32,
    reached: i32,
    visited: Vec<Vec<bool>>,
    moves: i32,
    nodes: Vec<Vec<i32>>,
    heuristic: i32
}

fn heuristic(point: Point) -> i32 {
    let mut h: i32 = 0;
    for e in point.nodes.iter() {
        let d: i32 = i32::abs(e[0] - point.pos_x) + i32::abs(e[1] - point.pos_y);
        h += d;
    }
    h += point.moves;
    // h = h * h;
    return h;
}

fn bfs(grid: Vec<Vec<char>>) -> i32 {
    let mut deque: VecDeque<Point> = VecDeque::new();
    let mut positions: Vec<Vec<i32>> = Vec::new();
    let mut position_num: Vec<&char> = Vec::new();
    let mut position_per: Vec<Vec<&char>> = Vec::new();
    let mut start_pos: Vec<usize> = Vec::new();

    for (i, e1) in grid.iter().enumerate() {
        for j in 0..e1.len() {
            if e1[j].is_digit(10) && e1[j] != '0' {
                let mut tmp: Vec<i32> = Vec::new();
                tmp.push(j.try_into().unwrap());
                tmp.push(i.try_into().unwrap());
                positions.push(tmp);
                position_num.push(&e1[j]);
            } else if e1[j] == '0' {
                start_pos.push(j);
                start_pos.push(i);
            }
        } 
    }
    
    let mut min_moves = 100000;
    let mut c = 1;
    for perm in position_num.clone().iter().permutations(position_num.len()).unique() {
        println!("{}/{} {:?} {}", c, 7 * 6 * 5 * 24, perm, min_moves);
        c += 1;
        // position_per.push(perm);
        let mut visited = vec![vec![false; grid[0].len()]; grid.len()];
        let mut point = Point{pos_x: 1,pos_y: 1, reached: 0, visited: visited.clone(), moves: 0, nodes: positions.clone(), heuristic: 0};
        point.visited[start_pos[1]][start_pos[0]] = true;
        // point.heuristic = heuristic(point.clone());
        deque.push_back(point.clone());

        let moves_x: [i32; 4] = [-1, 0, 0, 1];
        let moves_y: [i32; 4] = [0, -1, 1, 0];

        let mut num_usize: usize = point.reached.try_into().unwrap();
        let mut goal_index = position_num.iter().position(|x| *(&x) == perm[num_usize]).unwrap();
        // let goal_pos: Vec<i32> = positions.clone()[goal_index];

        while deque.len() > 0 {
            // deque.make_contiguous().sort_by_key(|x| x.heuristic);

            point = deque.pop_front().unwrap();

            // println!("x:{} y:{} r:{} h:{} m:{}", point.pos_x, point.pos_y, point.reached, point.heuristic, point.moves);
            // println!("{} {} {}", point.moves, min_moves, point.reached);
            if point.reached == positions.len().try_into().unwrap() {
                if point.moves < min_moves {
                    min_moves = point.moves;
                }
                break;
                // return point.moves;
            }
            else if point.moves > min_moves {
                break;
            }

            // let mut tmp_que: Vec<Point> = Vec::new();

            for i in 0..4 {
                let row: usize = (point.pos_y + moves_y[i]).try_into().unwrap();
                let col: usize = (point.pos_x + moves_x[i]).try_into().unwrap();


                if grid[row][col] != '#' && visited[row][col] == false {
                    let curr_pos = vec![point.pos_x + moves_x[i], point.pos_y + moves_y[i]];
                    if curr_pos == positions[goal_index] {
                        let mut new_point = Point{pos_x: point.pos_x + moves_x[i], pos_y: point.pos_y + moves_y[i], reached: point.reached, visited: visited.clone(), moves: point.moves + 1, nodes: point.clone().nodes, heuristic: 0};
                        // let index = new_point.nodes.iter().position(|x| *x == curr_pos).unwrap();
                        // new_point.nodes.remove(index);
                        // new_point.heuristic = heuristic(new_point.clone());
                        visited = vec![vec![false; grid[0].len()]; grid.len()];
                        visited[row][col] = true;
                        if num_usize < perm.len() - 1 {
                            num_usize += 1;
                            goal_index = position_num.iter().position(|x| *(&x) == perm[num_usize]).unwrap();
                        }
                        new_point.reached += 1;
                        deque.clear();
                        deque.push_back(new_point.clone());
                        break;
                        // tmp_que.push(new_point);
                    } else {
                        let mut new_point = Point{pos_x: point.pos_x + moves_x[i] ,pos_y: point.pos_y + moves_y[i], reached: point.reached, visited: point.clone().visited, moves: point.moves + 1, nodes: point.clone().nodes, heuristic: 0};
                        visited[row][col] = true;
                        // new_point.heuristic = heuristic(new_point.clone());
                        deque.push_back(new_point);
                        // tmp_que.push(new_point);
                    }
                }



            }

            // tmp_que.sort_by_key(|x| x.heuristic);

            // for e in tmp_que.iter() {
            //     deque.push_back(e.clone());
            // }
            
            // let mut s=String::new();
            // let _=stdout().flush();
            // stdin().read_line(&mut s).expect("Did not enter a correct string");
            // break;
        }
        // break;
    }

    return min_moves;
}