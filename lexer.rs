enum Tokem {
    token_eof = -1,

    token_identifier = -4,
    token_number = -5 
}

func getToken() -> i32 {

}

use std::io::{self, Read};

fn main() -> io::Result<()> {
    let mut buffer = String::new();
    let stdin = io::stdin();
    let mut handle = stdin.lock();

    handle.read_to_string(&mut buffer)?;
    Ok(())
}