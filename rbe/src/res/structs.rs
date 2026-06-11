#[derive(Debug)]
pub struct Test {
    integer: u32,
    string: String,
    float: f64,
}

impl Test {
    pub fn new() -> Self {
        Test {
            integer: 0,
            string: "Hello world".to_string(),
            float: 1.1
        }
    }

    pub fn set(&mut self, integer: Option<u32>, string: Option<String>, float: Option<f64>) -> Option<&Test> {
        self.integer = integer.unwrap_or(self.integer);
        if let Some(s) = string {
            self.string = s;
        }
        self.float = float.unwrap_or(self.float);
        Some(self)
    }

    pub fn get(&self) -> Option<&Test> {
        Some(self)
    }
}
