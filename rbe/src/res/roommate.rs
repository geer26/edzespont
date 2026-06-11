use std::collections::HashMap;
// use std::error;
use serde::{Deserialize, Serialize};
use uuid::{Uuid};


#[derive(Debug, Serialize, Deserialize)]
pub struct RoomMate {
    name: String,
    sid: String,
    supervisor: bool,
    suspended: bool,
    competitor_name: String,
    ready_to_go: bool,
    finished: bool,
    res: HashMap<String, Option<serde_json::Value>>,
    status: HashMap<String, Option<serde_json::Value>>,
    id: String,
    exp: u32,
    colour: String,
    category: String,
    exercise_to_show: String,
    weight: u8
}

impl RoomMate {

    pub fn new(sid: &str, name: &str) -> Self {
        RoomMate {
            name: String::from(name),
            sid: String::from(sid),
            supervisor: false,
            suspended: false,
            competitor_name: "".to_string(),
            ready_to_go: false,
            finished: false,
            res: HashMap::new(),
            status: HashMap::new(),
            id: Uuid::new_v4().simple().to_string(),
            exp: 0,
            colour: "GREEN".to_string(),
            category: "".to_string(),
            exercise_to_show: "".to_string(),
            weight: 0
        }
    }

    pub fn get(&self) -> serde_json::Value {
        serde_json::to_value(self).unwrap()
    }

}
