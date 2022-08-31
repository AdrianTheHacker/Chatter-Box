import dotenv

import os

import discord_client
from tts import create_tts_audio_file, say_message


def main():
    # environment_variables = dotenv.load_dotenv()
    # discord_token = os.getenv("DISCORD_TOKEN")

    # client.run(discord_token)

    say_message("Hello, world!")
    create_tts_audio_file("Hello, world!")


if __name__ == "__main__":
    main()
