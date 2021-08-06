use cfg_if::cfg_if;
use calc::Compile;

cfg_if!{
    if #[cfg(feature = "default")]{
        use calc::jit as Engine;
    } else {
        use calc::Interpreter as Engine;
    }
}

fn main(){
    let args: Vec<String> = std::env::args().collect();
    if args.len() < 2 {
        eprintln!("No input file was provided");
        std::process::exit(-1);
    }
    println!(
        "{:?}", Engine::from_source(&std::fs::read_to_string(&args[1]).unwrap()).unwrap()
    )
}