import time
import tkinter
import tkinter.messagebox
import customtkinter
import subprocess
import os
from PIL import Image
import configparser

# First checks before launching the launcher

config = configparser.ConfigParser()
config.read('launchersettings.ini')
gamechannel = config['Launcher']['channel']

if gamechannel == 'Stable':
    dariopath = 'super-dario/'
else:
    dariobin = 'super-dario-preview/'

theme = config['Launcher']['theme']

homepath = os.path.expanduser('~')
scooppath = '/scoop/'
dariobin = homepath + scooppath + dariopath + 'dario.exe'
darioinstalled = os.path.exists(dariobin)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Window Properties

        self.title("FB Launcher")
        self.geometry("700x400")
        self.resizable(False)

        # set grid layout 1x2

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

         # Functions for launcher buttons

        def dariolaunch():
            ldario = subprocess.Popen(dariobin, shell=True)
            self.withdraw()
            ldario.wait()
            self.deiconify()

        # create navigation frame

        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        # Launcher name/logo

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="FB Launcher",
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # Sidebar Buttons

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Downloads",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Settings",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        # Appearence menu options

        self.setlabel = customtkinter.CTkLabel(self.navigation_frame, text="Theme:")
        self.setlabel.grid(row=5, column=0, padx=20, pady=0, sticky="nsew")
        self.appearance_mode_menu = customtkinter.CTkComboBox(self.navigation_frame, values=["System", "Dark", "Light"], variable=theme,
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=0)
        self.spacer = customtkinter.CTkLabel(self.navigation_frame, text="") # Just a blank label to add some space
        self.spacer.grid(row=7, column=0, padx=20, pady=2) # label position

        # create home frame

        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="")
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        # Things in the first frame

        self.homelabel = customtkinter.CTkLabel(master=self.home_frame, text="Select a game to launch")
        self.darioimg = customtkinter.CTkImage(Image.open("assets/games/dario.png"), size=(130, 200))
        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="", image=self.darioimg, command=dariolaunch)
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="CTkButton", compound="right")
        self.home_frame_button_2.grid(row=1, column=1, padx=20, pady=10)
        self.home_frame_button_3 = customtkinter.CTkButton(self.home_frame, text="CTkButton", compound="top")
        self.home_frame_button_3.grid(row=1, column=2, padx=20, pady=10)

        # create second frame

        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure(0, weight=1)

        # Things in the second frame

        self.prog = customtkinter.CTkProgressBar(self.second_frame, mode="indeterminate")
        self.prog.grid(row=0, column=0, padx=20, pady=10)
        self.dllabel = customtkinter.CTkLabel(self.second_frame, text="No Active Downloads Yet.")
        self.dllabel.grid(row=1, column=0, padx=20, pady=10)

        # create third frame

        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.third_frame.grid_columnconfigure(0, weight=1)

        # Things is the third frame

        self.label = customtkinter.CTkLabel(self.third_frame, text="Ajusts the settings of the this launcher", compound="top")
        self.label.grid(row=1, column=0, padx=20, pady=10)
        self.label2 = customtkinter.CTkLabel(self.third_frame, text="Content Release channel: ", anchor="w")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.check = customtkinter.CTkComboBox(self.third_frame, values=["Stable", "Preview",], command=self.channel, variable=gamechannel)
        self.check.grid(row=2, column=1, padx=20, pady=10)

        # select default frame

        self.select_frame_by_name("home")


    def select_frame_by_name(self, name):

        # set button color for selected button

        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame

        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()



    # Functions to select frames

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")


    # Function to toggle dark mode

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
        th3m3 = config["Launcher"]
        th3m3['theme'] = new_appearance_mode
        with open('launchersettings.ini', 'w') as configfile:
            config.write(configfile)

    # Function to toggle content release channel
    
    def channel(self, new_channel):
        gamechannel = new_channel
        if gamechannel == 'Stable':
            dariopath = 'dario-game/'
            l = config["Launcher"]
            l['channel'] = "Stable"
            with open('launchersettings.ini', 'w') as configfile:
                config.write(configfile)
        else:
            dariopath = 'dario-game-preview/'
            l = config["Launcher"]
            l['channel'] = "Preview"
            with open('launchersettings.ini', 'w') as configfile:
                config.write(configfile)
            

# Only when called directly

if __name__ == "__main__":

    # Launch UI

    app = App()
    app.mainloop()