from discord.ext import commands

extensions = []
load_list = [f"modules.{ext}" for ext in extensions]
reload_list = []

def setup(bot):
    for ext in load_list:
        try:
            bot.load_extension(ext)
        except commands.ExtensionAlreadyLoaded:
            reload_list.append(ext)
        except Exception as err:
            print(f"{ext} not loaded! ({err})")
        else:
            print(f"{ext} loaded!")

    for ext in reload_list:
        try:
            bot.reload_extension(ext)
        except Exception as err:
            print(f"{ext} not reloaded! ({err})")
        else:
            print(f"{ext} reloaded!")

# Block execution of this file alone
if __name__ == "__main__":
    exit()