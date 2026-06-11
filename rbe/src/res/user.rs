use serde::{Deserialize, Serialize};
// use uuid::Uuid;


#[derive(Debug, Serialize, Deserialize)]
pub struct User {
    _id: String,
    username: String,
    email: String,
    password_hash: String,
    is_superuser: bool,
    fingerprint: String,
    timestamp: f32,
    plan: String,
    number_of_tries: u8,
}