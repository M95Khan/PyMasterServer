import tkinter
import tkinter.messagebox
import customtkinter
import urllib.request
from PIL import Image
import os

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("red")

class App2(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("X-Teamer Portal (Legacy Version)")
        self.geometry(f"{1280}x{880}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Welcome Mahad Khan\n", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="X-Contract")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.profile, text="Client Contract")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        #self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        #self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Logout", command=self.logout)
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        #self.textbox = customtkinter.CTkTextbox(self, width=250)
        #self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=820, height=600)
        self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Profile")
        self.tabview.add("Project")
        self.tabview.add("Rewards")
        self.tabview.add("Milestones")
        self.tabview.tab("Profile").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Project").grid_columnconfigure(0, weight=1)

        current_path = os.path.dirname(os.path.realpath(__file__))

        #self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("Profile"), dynamic_resizing=False,
        #                                                values=["Value 1", "Value 2", "Value Long Long Long"])
        #self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        #self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("Profile"),
         #                                           values=["Value 1", "Value 2", "Value Long....."])
        #self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
        #self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Profile"), text="InputDialog",
         #                                                  command=self.open_input_dialog_event)
        #self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        #self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Project"), text="Here is project history")
        #self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

        urllib.request.urlretrieve("https://lh3.googleusercontent.com/pw/AMWts8DcHEva4yEWNqbTCFCyjhka-uvl65Y9rcAAVw9nHQE4ub83mmPVPTVSIFeu1c3nDj-Z1sgGc1Dt3_G-N06rvdVpMX3MX2UPeCcXLLr8YhdvGcO0X8zfrWXcZpQb_KdI9q_Zcl9fF3x9E49sNB18fUg=w960-h685-no?authuser=0", "profile.png")
        
        self.bg_image = customtkinter.CTkImage(Image.open("profile.png"),
                                               size=(800, 570))
        self.bg_image_label = customtkinter.CTkLabel(self.tabview.tab("Profile"), image=self.bg_image, text="")
        self.bg_image_label.grid(row=0, column=0)
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/test_images/tracker.png"),
                                               size=(800, 570))
        self.bg_image_label = customtkinter.CTkLabel(self.tabview.tab("Rewards"), image=self.bg_image, text_color="white")
        self.bg_image_label.grid(row=0, column=0)
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/test_images/xmilestones.png"),
                                               size=(800, 570))
        self.bg_image_label = customtkinter.CTkLabel(self.tabview.tab("Milestones"), image=self.bg_image, text="")
        self.bg_image_label.grid(row=0, column=0)

        # create radiobutton frame
        self.radiobutton_frame = customtkinter.CTkFrame(self, width=100)
        self.radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Active Reward Breakdown:", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0, text="20-01-23 8000USD")
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1, text="10-02-23 8000USD")
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=2, text="20-02-23 8000USD")
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_4 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=3, text="10-03-23 8000USD")
        self.radio_button_4.grid(row=4, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_5 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=4, text="20-03-23 8000USD")
        self.radio_button_5.grid(row=5, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_6 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=5, text="10-04-23 8000USD")
        self.radio_button_6.grid(row=6, column=2, pady=10, padx=20, sticky="n")

        # create checkbox and switch frame
        #self.checkbox_slider_frame = customtkinter.CTkFrame(self, width=100)
        #self.checkbox_slider_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        #self.checkbox_1 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        #self.checkbox_1.grid(row=1, column=0, pady=(20, 10), padx=20, sticky="n")
        #self.checkbox_2 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        #self.checkbox_2.grid(row=2, column=0, pady=10, padx=20, sticky="n")
        #self.switch_1 = customtkinter.CTkSwitch(master=self.checkbox_slider_frame, command=lambda: print("switch 1 toggle"))
        #self.switch_1.grid(row=3, column=0, pady=10, padx=20, sticky="n")
        #self.switch_2 = customtkinter.CTkSwitch(master=self.checkbox_slider_frame)
        #self.switch_2.grid(row=4, column=0, pady=(10, 20), padx=20, sticky="n")

        # create slider and progressbar frame
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        #self.seg_button_1 = customtkinter.CTkSegmentedButton(self.slider_progressbar_frame)
        #self.seg_button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        #self.progressbar_2 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        #self.progressbar_2.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        #self.slider_1 = customtkinter.CTkSlider(self.slider_progressbar_frame, from_=0, to=1, number_of_steps=4)
        #self.slider_1.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        #self.slider_2 = customtkinter.CTkSlider(self.slider_progressbar_frame, orientation="vertical")
        #self.slider_2.grid(row=0, column=1, rowspan=5, padx=(10, 10), pady=(10, 10), sticky="ns")
        #self.progressbar_3 = customtkinter.CTkProgressBar(self.slider_progressbar_frame, orientation="vertical")
        #self.progressbar_3.grid(row=0, column=2, rowspan=5, padx=(10, 20), pady=(10, 10), sticky="ns")

        # set default values
        self.sidebar_button_3.configure(state="disabled", text="Unleash+")
        #self.checkbox_2.configure(state="disabled")
        #self.switch_2.configure(state="disabled")
        #self.checkbox_1.select()
        #self.switch_1.select()
        self.radio_button_2.configure(state="disabled")
        self.radio_button_3.configure(state="disabled")
        self.radio_button_4.configure(state="disabled")
        self.radio_button_5.configure(state="disabled")
        self.radio_button_6.configure(state="disabled")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        #self.optionmenu_1.set("CTkOptionmenu")
        #self.combobox_1.set("CTkComboBox")
        #self.slider_1.configure(command=self.progressbar_2.set)
        #self.slider_2.configure(command=self.progressbar_3.set)
        self.progressbar_1.configure(mode="indeterminnate")
        self.progressbar_1.start()
        #self.textbox.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)
        #self.seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
        #self.seg_button_1.set("Value 2")

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def logout(self):
        self.destroy()
        app_re = App()
        app_re.mainloop() 

    def profile(self):
         app_3 = App3()
         app_3.mainloop()       


class App(customtkinter.CTk):
    width = 900
    height = 600

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("X-Teamer Portal (Legacy Version")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        # load and create background image
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/test_images/x-team.jpg"),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        # create login frame
        self.login_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.login_frame.grid(row=0, column=0, sticky="ns")
        self.login_label = customtkinter.CTkLabel(self.login_frame, text="X-TEAMER\nSign In",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        self.username_entry = customtkinter.CTkEntry(self.login_frame, width=200, placeholder_text="username")
        self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.password_entry = customtkinter.CTkEntry(self.login_frame, width=200, show="*", placeholder_text="password")
        self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
        self.login_button = customtkinter.CTkButton(self.login_frame, text="Login", command=self.login_event, width=200)
        self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))

        # create main frame
        self.main_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_label = customtkinter.CTkLabel(self.main_frame, text="Welcome",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.main_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        self.back_button = customtkinter.CTkButton(self.main_frame, text="Back", command=self.back_event, width=200)
        self.back_button.grid(row=1, column=0, padx=30, pady=(15, 15))


    def login_event(self):
        # print("Login pressed - username:", self.username_entry.get(), "password:", self.password_entry.get())
        if self.username_entry.get() == "mahad1khan95@yahoo.com" and self.password_entry.get() == "123Herewego@@":  
         self.destroy()  # remove login frame To make it more [resentable & to stop gobling up of space.
         app2 = App2()
         app2.mainloop()
        else:
            self.login_frame.grid_forget()
            self.main_frame2 = customtkinter.CTkFrame(self, corner_radius=0)
            self.main_frame2.grid_columnconfigure(0, weight=1)
            self.main_label = customtkinter.CTkLabel(self.main_frame2, text="Incorrect Username or Password",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
            self.main_label.grid(row=0, column=0, padx=30, pady=(150, 15))
            self.back_button = customtkinter.CTkButton(self.main_frame2, text="Back", command=self.back_event, width=200)
            self.back_button.grid(row=1, column=0, padx=30, pady=(15, 15))
            self.main_frame2.grid(row=0, column=0, sticky="ns", padx=100) 

    def back_event(self):
        self.main_frame2.grid_forget()  # remove main frame
        self.login_frame.grid(row=0, column=0, sticky="ns")  # show login frame
       
class App3(customtkinter.CTk):
    width = 900
    height = 600

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Mahad Khan's Profile")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        # load and create background image
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/test_images/x-team.jpg"),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        self.login_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.login_frame.grid(row=0, column=0, sticky="ns")

        self.login_label = customtkinter.CTkLabel(self.login_frame, text="X-TEAMER\nSign In",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))

if __name__ == "__main__":
    app = App()
    app.mainloop()