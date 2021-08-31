use std::fs;

fn main() {
    let data = read_input_data("../d09-input.txt");
    let preamble = 25;
    let mut solution: bool = false;
    let mut index = 0 + preamble - 1;
    loop {
        println!("{} = {} = {}", index, data[index], data[index + preamble]);
        'outer: for j in data[index..index + preamble].iter() {
            'inner: for k in data[index..index + preamble].iter() {
                println!(
                    "{} == {} == {} == {}",
                    index,
                    j,
                    k,
                    j.parse::<i32>().unwrap() + k.parse::<i32>().unwrap()
                        == data[index].parse::<i32>().unwrap()
                );
                if (j.parse::<i32>().unwrap() + k.parse::<i32>().unwrap()
                    == data[index].parse::<i32>().unwrap())
                    && (j.parse::<i32>().unwrap() != k.parse::<i32>().unwrap())
                {
                    println!("\n{} - {} - {}\n", data[index], j, k);
                    solution = true;
                    continue 'outer;
                }
            }
            if solution == true {
                continue 'outer;
            }
        }
        if solution == true {
            solution = !solution;
            index += 1;
        }
    }
    println!("Finished!");
}

fn read_input_data(filename: &str) -> Vec<String> {
    println!("{}", filename);
    let input = fs::read_to_string(filename)
        .unwrap()
        .lines()
        .map(|line| line.to_string())
        .collect();
    input
}
