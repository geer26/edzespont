use sqlx::postgres::PgPoolOptions;
use sqlx::{Pool, Postgres};


pub async fn new_pool() -> Result<Pool<Postgres>, sqlx::Error> {
    let pool = PgPoolOptions::new()
        .max_connections(5)
        .connect("postgres://postgres:password@localhost/test").await?;
    Ok(pool)
}
