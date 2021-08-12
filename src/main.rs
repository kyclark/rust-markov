fn main() {
    if let Err(e) = markov::get_args().and_then(markov::run) {
        eprintln!("{}", e);
        std::process::exit(1);
    }
}
