import webbrowser
import time
import os

def renameFiles():
    saved_dir = os.getcwd()
    for fileName in os.listdir("/tmp/prank"):
        os.chdir("/tmp/prank")
        os.rename(fileName,fileName.translate(None,"0123456789"))   
    os.chdir(saved_dir)

renameFiles()
