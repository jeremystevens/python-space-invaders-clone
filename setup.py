import sys
from cx_Freeze import setup, Executable
# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": [""]}

# GUI applications require a different base on Windows (the default is for a
# console application).
includes = ["os"]
base = None
if sys.platform == "win32":
    base = "Win32GUI"
    
setup(  name = "SpaceInvaders",
        version = "0.1",
        description = "a space invaders clone",
        icon = "invader.ico",
        options = {"build_exe": {"includes": includes}},
executables = [Executable("spaceinvaders.py", base=base)])
