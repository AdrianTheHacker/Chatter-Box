use tts_rust::{ GTTSClient, languages::Languages };

fn create_narrator(volume: f32, language: Languages) -> GTTSClient {
    // Creates and returns the GTTSClient.
    // GTTSClient is used for TTS.

    let narrator: GTTSClient = GTTSClient {
        volume: volume, 
        language: language, // use the Languages enum
    };

    narrator
}

pub fn speak(message: &str) {
    let narrator: GTTSClient = create_narrator(1.0, Languages::English);

    narrator.speak(message);
}