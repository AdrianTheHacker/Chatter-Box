use delete::{delete_file};

use gtts::save_to_file;


fn clear_audio(file_path: &str) {
    // Deletes Sound.mp3.
    // Ran before creating an audio file.

    delete_file(file_path).unwrap();
}

pub fn create_audio(message: &str) {
    let file_path: &str = r"audio_files\Sound.mp3";
    clear_audio(&file_path);

    // Creates an audio_files\Sound.mp3.
    // This mp3 file contains the TTS of the message.
    save_to_file(message, &file_path);
}