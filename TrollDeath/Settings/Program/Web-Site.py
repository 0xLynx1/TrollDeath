from Config.Util import *
from Config.Config import *
import webbrowser
Title("Web Site")
print(f"""
{color.WHITE}[{color.RED}01{color.WHITE}] {color.RED}->{color.WHITE} gunslol
{color.WHITE}[{color.RED}02{color.WHITE}] {color.RED}->{color.WHITE} Telegram
{color.WHITE}[{color.RED}03{color.WHITE}] {color.RED}->{color.WHITE} Twitter
""")

choice = input(f"{color.RED}{INPUT} Site -> {color.RESET}")
if choice in ['1', '01']:
    site = f"{website}"
    webbrowser.open_new_tab(site)
    print(f"\n{color.RED}{INFO} Access to the site \"{color.WHITE}{site}{color.RED}\"" + color.RESET)
    Continue()
    Reset()
if choice in ['2', '02']:
    site = f"{discord_server}"
    webbrowser.open_new_tab(site)
    print(f"{color.RED}\n{INFO} Access to the Discord server \"{color.WHITE}{site}{color.RED}\"" + color.RESET)
    Continue()
    Reset()

if choice in ['3', '03']:
    site = f"{github_tool}"
    webbrowser.open_new_tab(site)
    print(f"\n{color.RED}{INFO} Access to the site \"{color.WHITE}{site}{color.RED}\"" + color.RESET)
    Continue()
    Reset()