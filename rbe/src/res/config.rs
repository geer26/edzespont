use std::io::Error;
use std::env;
use serde_json::to_string;




#[derive(Debug)]
pub struct Config {
    backend_port: String,
    access_token_secret: String,
    refresh_token_secret: String,
    secret_key: String,
    wtf_csrf_secret_key: String,
    jwt_hash_algorythm: String,
    max_passwprd_tries: u8,
    // <------------------ SOCKERSERVER SETTINGS
    ping_timeout: u8, // The time in seconds that the client waits for the server to respond before disconnecting.
                        //The default is 5 seconds.
    ping_interval: u8, //The interval in seconds at which the server pings the client.
                        //The default is 25 seconds. For advanced control,
                        //a two element tuple can be given, where the first number is the ping
                        // interval and the second is a grace period added by the server.
    stripe_publishable_key: String,
    stripe_secret_key: String,
    stripe_billing_address: String,
    stripe_endpoint_secret: String,
    stripe_domain_url: String,
    short_term_period: u8, // in minutes
    long_term_perion: u8, // in hours
    flush_term: u8, // in seconds - flushes the mistakenly disconneced clients
    cookie_expiration_time: u8, //in hours
    csrf_expiration_time: u8, //in hours
    refresh_expiration_time: u8, //in hours
    access_expiration_time: u8, //in minutes
    temp_user_validity: u8, //in minutes
    contact_mail: String,
    mail_username: String,
    mail_password: String,
    mail_server: String,
    mail_port: String,
    mail_use_tls: bool,
    //MAIL_USE_SSL: bool,
    mail_default_sender: String,
    mongo_uri: String,
    db: String,
    db_host: String,
    db_port: String,
    db_alias: String,
    db_user: String,
    db_password: String
}



#[allow(non_snake_case)]
impl Config {

    pub fn build_config() -> Result<Self, Error> {
        // return Err(Error::other("something went wrong"));
        let config = Config{
            backend_port: env::var("BACKEND_PORT").unwrap_or_else(|_| String::from("5001")),
            access_token_secret: env::var("ACCESSTOKENSECRET").unwrap_or_else(|_| String::from("4CC35_533CR37")),
            refresh_token_secret: env::var("REFRESHTOKENSECRET").unwrap_or_else(|_| String::from("R3FR3SH_53CR37")),
            secret_key: env::var("SECRET_KEY").unwrap_or_else(|_| String::from("53CR37_K3Y")),
            wtf_csrf_secret_key: env::var("WTF_CSRF_SECRET_KEY").unwrap_or_else(|_| String::from("W7F_53CR37")),
            jwt_hash_algorythm: env::var("JWT_HASH_ALGORYTHM").unwrap_or_else(|_| String::from("JWT_53CR37")),
            max_passwprd_tries: env::var("MAX_PASSWORD_TRIES").unwrap_or_else(|_| "5".to_string())
                    .parse::<u8>()
                    .unwrap_or(5),
            ping_timeout: env::var("PING_TIMEOUT").unwrap_or_else(|_| "10".to_string())
                    .parse::<u8>()
                    .unwrap_or(10),
            ping_interval: env::var("PING_INTERVAL").unwrap_or_else(|_| "25".to_string())
                    .parse::<u8>()
                    .unwrap_or(25),
            stripe_publishable_key: env::var("STRIPE_PUBLISHABLE_KEY").unwrap_or_else(|_| String::from("STRIPE_PUBLISHABLE_KEY")),
            stripe_secret_key: env::var("STRIPE_SECRET_KEY").unwrap_or_else(|_| String::from("STRIPE_SECRET_KEY")),
            stripe_billing_address: env::var("STRiPE_BILLING_ADDRESS").unwrap_or_else(|_| String::from("STRiPE_BILLING_ADDRESS")),
            stripe_endpoint_secret: env::var("STRIPE_ENDPOINT_SECRET").unwrap_or_else(|_| String::from("STRIPE_ENDPOINT_SECRET")),
            stripe_domain_url: env::var("STRIPE_DOMAIN_URL").unwrap_or_else(|_| String::from("STRIPE_DOMAIN_URL")),
            short_term_period: env::var("SHORT_TERM_PERIOD").unwrap_or_else(|_| "15".to_string())
                    .parse::<u8>()
                    .unwrap_or(15),
            long_term_perion: env::var("LONG_TERM_PERIOD").unwrap_or_else(|_| "24".to_string())
                    .parse::<u8>()
                    .unwrap_or(24),
            flush_term: env::var("COOKIE_EXPIRATION_TIME").unwrap_or_else(|_| "120".to_string())
                    .parse::<u8>()
                    .unwrap_or(120),
            cookie_expiration_time: env::var("COOKIE_EXPIRATION_TIME").unwrap_or_else(|_| "24".to_string())
                    .parse::<u8>()
                    .unwrap_or(24),
            csrf_expiration_time: env::var("CSRF_EXPIRATION_TIME").unwrap_or_else(|_| "24".to_string())
                    .parse::<u8>()
                    .unwrap_or(24),
            refresh_expiration_time: env::var("REFRESH_EXPIRATION_TIME").unwrap_or_else(|_| "24".to_string())
                    .parse::<u8>()
                    .unwrap_or(24),
            access_expiration_time: env::var("ACCESS_EXPIRATION_TIME").unwrap_or_else(|_| "15".to_string())
                    .parse::<u8>()
                    .unwrap_or(15),
            temp_user_validity: env::var("TEMP_USER_VALIDITY").unwrap_or_else(|_| "15".to_string())
                    .parse::<u8>()
                    .unwrap_or(15),
            contact_mail: env::var("CONTACT_MAIL").unwrap_or_else(|_| String::from("contact@repforge.hu")),
            mail_username: env::var("MAIL_USERNAME").unwrap_or_else(|_| String::from("noreply@repforge.hu")),
            mail_password: env::var("MAIL_PASSWORD").unwrap_or_else(|_| String::from("726354Valami01?")),
            mail_server: env::var("MAIL_SERVER").unwrap_or_else(|_| String::from("smtp.forpsi.com")),
            mail_port: env::var("MAIL_PORT").unwrap_or_else(|_| String::from("587")),
            mail_use_tls: env::var("MAIL_USE_TLS").unwrap_or_else(|_| "true".to_string())
                    .parse::<bool>()
                    .unwrap_or(true),
            mail_default_sender: env::var("MAIL_DEFAULT_SENDER").unwrap_or_else(|_| String::from("noreply@repforge.hu")),
            mongo_uri: env::var("MONGO_URI").unwrap_or_else(|_| String::from("mongodb://HinataHyuga:n6IUEypfSM1Hl4A6Xk0zWd0iAZLdub0J7ozrKGHnnhdqM9K4A1EhO3afX1ETQJIW@localhost:27017/kettDB")),
            db: env::var("DB").unwrap_or_else(|_| String::from("kettDB")),
            db_host: env::var("DBHOST").unwrap_or_else(|_| String::from("localhost")),
            db_port: env::var("DBPORT").unwrap_or_else(|_| String::from("27017")),
            db_alias: env::var("DBALIAS").unwrap_or_else(|_| String::from("default")),
            db_user: env::var("DBUSER").unwrap_or_else(|_| String::from("HinataHyuga")),
            db_password: env::var("DBPASSWORD").unwrap_or_else(|_| String::from("n6IUEypfSM1Hl4A6Xk0zWd0iAZLdub0J7ozrKGHnnhdqM9K4A1EhO3afX1ETQJIW")),
        };

        println!("Config built...");
        Ok(config)
    }

    pub fn mongo_uri(&self) -> &str {
        self.mongo_uri.as_str()
    }

}
