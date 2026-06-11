use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize)]
pub struct RoomSpectator {
    sid: String,
}

impl RoomSpectator {

    pub fn new(sid: &str) -> Self {
        RoomSpectator{
            sid: String::from(sid),
        }
    }

    pub fn get(&self) -> serde_json::Value {
        serde_json::to_value(self).unwrap()
    }

}
