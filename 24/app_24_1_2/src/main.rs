extern crate itertools;
extern crate permutation;
use std::collections::VecDeque;
use std::convert::TryInto;
use itertools::Itertools;
use std::cmp;

fn main() {
    let lines = include_str!("../input.txt").lines().collect::<Vec<&str>>();
    let mut grid: Vec<Vec<char>> = Vec::new();

    for e in lines.iter() {
        let v_tmp = e.chars().collect::<Vec<char>>();
        grid.push(v_tmp);
    }

    let result = solve(grid);
    
    println!("Part1: {}\nPart2: {}", result[0], result[1]);
}

#[derive(Clone)]
struct Point {
    pos_x: i32,
    pos_y: i32,
    moves: i32
}

fn bfs_from(grid: Vec<Vec<char>>, positions: Vec<Vec<i32>>, positions_num: Vec<i32>, pos: i32, start_pos: Vec<usize>) -> Vec<i32> {
    let mut dist: Vec<i32> = Vec::new();

    let moves_x: [i32; 4] = [-1, 0, 0, 1];
    let moves_y: [i32; 4] = [0, -1, 1, 0];

    for e in positions_num.iter() {
        if e != &pos {
            let mut visited = vec![vec![false; grid[0].len()]; grid.len()];

            let mut starting_point = Point{pos_x: start_pos[0] as i32, pos_y: start_pos[1] as i32, moves: 0};
            

            if pos != 0 {
                let start_index = positions_num.iter().position(|x| *x == pos).unwrap();
                
                starting_point = Point{pos_x: positions[start_index][0], pos_y: positions[start_index][1], moves: 0};
            
                visited[starting_point.pos_y as usize][starting_point.pos_x as usize] = true;
            } else {
                visited[start_pos[1]][start_pos[0]] = true;
            }

            let end_index = positions_num.iter().position(|x| *x == *e).unwrap();
            let mut deque: VecDeque<Point> = VecDeque::new();
            deque.push_back(starting_point);
            while deque.len() > 0 {
                let point = deque.pop_front().unwrap();

                if point.pos_x == positions[end_index][0] && point.pos_y == positions[end_index][1] {
                    dist.push(point.moves);
                    break;
                }

                for i in 0..4 {
                    let row: usize = (point.pos_y + moves_y[i]).try_into().unwrap();
                    let col: usize = (point.pos_x + moves_x[i]).try_into().unwrap();

                    if grid[row][col] != '#' && visited[row][col] == false {
                        let new_point = Point{pos_x: point.pos_x + moves_x[i] ,pos_y: point.pos_y + moves_y[i], moves: point.moves + 1};
                        visited[row][col] = true;
                        deque.push_back(new_point);
                    }
                }
            } 
        } else {
            dist.push(0);
        }
    }
    return dist;
}

fn solve(grid: Vec<Vec<char>>) -> Vec<i32> {
    let mut positions: Vec<Vec<i32>> = Vec::new();
    let mut positions_num: Vec<i32> = Vec::new();
    let mut dist: Vec<Vec<i32>> = Vec::new();
    let mut start_pos: Vec<usize> = Vec::new();

    for (i, e1) in grid.iter().enumerate() {
        for j in 0..e1.len() {
            if e1[j].is_digit(10) && e1[j] != '0' {
                let mut tmp: Vec<i32> = Vec::new();
                tmp.push(j.try_into().unwrap());
                tmp.push(i.try_into().unwrap());
                positions.push(tmp);
                let n:i32 = e1[j] as i32 - 0x30;
                positions_num.push(n);
            } else if e1[j] == '0' {
                start_pos.push(j);
                start_pos.push(i);
            }
        } 
    }

    let permutation = permutation::sort(&positions_num);
    positions = permutation.apply_slice(&positions);
    positions_num = permutation.apply_slice(&positions_num);

    for i in 0..(positions_num.len() + 1) {
        dist.push(bfs_from(grid.clone(), positions.clone(), positions_num.clone(), i.try_into().unwrap(), start_pos.clone()));
    }
    
    let mut min_moves_p1 = 100000;
    let mut min_moves_p2 = 100000;
    for perm in positions_num.clone().iter().permutations(positions_num.len()).unique() {
        let mut path: i32 = 0;
        path += dist[0][(*perm[0] - 1) as usize];
        for i in 1..perm.len() {
            path += dist[*perm[i-1] as usize][(*perm[i] - 1) as usize];
        }
        min_moves_p1 = cmp::min(min_moves_p1, path);
        path += dist[0][(*perm[perm.len() - 1] - 1) as usize];
        min_moves_p2 = cmp::min(min_moves_p2, path);
    }

    let res = vec![min_moves_p1, min_moves_p2];

    return res;
}