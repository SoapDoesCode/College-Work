from time import sleep as wait
from asyncio import run, sleep as asyncWait
from sys import path

path = "peripherals"
if path not in path:
    path.append(path)

import keyboardControl as keyboard
import mouseControl as mouse
import win11.mods.webUtils as webUtils

run(webUtils.open_URL("https://my.nulc.ac.uk/", "Edge", True))
run(webUtils.new_tab_to_url("https://docs.google.com"))
run(webUtils.new_tab_to_url("https://teams.microsoft.com"))
run(webUtils.new_tab_to_url("https://chatgpt.com"))
run(webUtils.new_tab_to_url("discord://"))
run(webUtils.new_tab_to_url("vscode://"))
run(webUtils.new_tab_to_url("about:blank"))