import ctypes
import os
import platform
import tkinter as tk

from src.Common.Constants import constants
from src.UI.HomeScreen import HomeScreen
from src.Utility.ConfigUtility import ConfigUtility
from src.Utility.FileUtility import FileUtility


class EducativeScraper:
    def __init__(self):
        print("""
                Educative Scraper (version 3.0.6 Dev Branch), developed by Anilabha Datta
                Project Link: https://github.com/anilabhadatta/educative.io_scraper/tree/v3-dev
                Check out ReadMe for more information about this project.
                Use the GUI to start scraping.
        """)

        self.fileUtil = FileUtility()
        self.configUtil = ConfigUtility()
        self.loadBasicUtility()
        self.root = tk.Tk()
        img = tk.PhotoImage(file=os.path.join(constants.commonFolderPath, "icon.png"))
        self.root.iconphoto(True, img)
        self.run()


    def loadBasicUtility(self):
        self.fileUtil.createFolderIfNotExists(constants.OS_ROOT)
        self.configUtil.createDefaultConfigIfNotExists()


    def run(self):
        HomeScreen(self.root).createHomeScreen()
        self.root.mainloop()


if __name__ == '__main__':
    if platform.system() == "Windows":
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("EducativeScraper")
    app = EducativeScraper()