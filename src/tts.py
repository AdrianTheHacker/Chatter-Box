import pyttsx3

import constants
import os


engine = pyttsx3.init()


def say_message(message):
    """
    Says <message> using TTS engine.

    This is used for fast debugging when testing
    discord bot's ability to read and speak messages.
    """
    engine.say(message)


def __clear_audio():
    """
    Clears audio.
    Used before updating the audio.
    """
    try:
        os.remove(constants.audio_file_path)

    except FileNotFoundError:
        print(f"File '{constants.audio_file_path}' doesn't exist.")


def create_tts_audio_file(message):
    """
    Using the text in <message>, this creates a TTS (text-to-speech) mp3 file and stores 
    the file in "audio_file\sounds.mp3".
    """
    __clear_audio()

    engine.save_to_file(message, constants.audio_file_path)
    engine.runAndWait()
