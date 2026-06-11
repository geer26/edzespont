use serde::{Deserialize, Serialize};
use uuid::Uuid;


#[derive(Debug, Serialize, Deserialize)]
pub struct WO {
    r#type: String,
    exercise: String,
    time: u32,
    fixed: String,
    max_reps: u32,
}

impl WO {

    pub fn new(r#type: &str,
        exercise: &str,
        time: u32,
        fixed: &str,
        max_reps: u32) -> Self {
        return WO{
            time,
            max_reps,
            r#type: String::from(r#type),
            exercise: String::from(exercise),
            fixed: String::from(fixed)
        }
    }

}


#[derive(Debug, Serialize, Deserialize)]
pub struct Workout {
    _id: String,
    name: String,
    available: String,
    need_ename: bool,
    workout: Vec<WO>,
}

impl Workout {

    pub fn new(name: &str, available: &str, need_ename: bool) -> Self {
        Workout {
            need_ename,
            _id: Uuid::new_v4().simple().to_string(),
            name: String::from(name),
            available: String::from(available),
            workout: Vec::new()
        }
    }

}
