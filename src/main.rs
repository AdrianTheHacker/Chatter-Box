use std::collections::HashMap;

use env_file_reader::read_file;
use tokio;

mod discord_bot;


#[tokio::main]
async fn main() {
    // Configure the client with your Discord bot token in the environment.
    let env_var: HashMap<String, String> = read_file(r".env").expect("Expected a token in the environment");
    let bot_token: &String = &env_var["DISCORD_TOKEN"];
    
    // Create the client
    let mut client: serenity::Client = discord_bot::create_client(&bot_token).await;

    // Start a single shard, and start listening to events.
    //
    // Shards will automatically attempt to reconnect, and will perform
    // exponential backoff until it reconnects.
    if let Err(why) = client.start().await {
        println!("Client error: {:?}", why);
    }
}