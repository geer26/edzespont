use rbe::db::connection;
// use std::io::Error;
// use rbe::run;
// use rbe::res::config;

#[tokio::main]
async fn main() {
    // let cfg = config::Config::build_config().expect("Load config failed...");
    // run(cfg);
    let _pool = connection::new_pool().await;
    println!("Hello, world!")
}
