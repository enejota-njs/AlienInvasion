import sys, os

import alien_invasion.alien_invasion as ai

dirpath = os.getcwd()
sys.path.append(dirpath)
if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)

ai.run_game()