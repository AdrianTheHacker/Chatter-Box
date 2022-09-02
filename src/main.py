import dotenv

import os

from discord_client import bot


def main():
    environment_variables = dotenv.load_dotenv()
    discord_token = os.getenv("DISCORD_BOT_TOKEN")

    bot.run(discord_token)


if __name__ == "__main__":
    main()
