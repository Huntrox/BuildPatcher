import asyncio
import itchApi
import tkinter as tk
from tkinter import  StringVar, ttk, filedialog, scrolledtext

padding = {'padx': 4, 'pady': 4}
padding_btn = {'padx': 4, 'pady': 2}
padding_label = {'padx': 3, 'pady': 4}
padding_entry = {'padx': 4, 'pady': 4}

EWN ="EWN"
SEWN ="SEWN"

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("300x320")
        self.title("Build Patcher")
        self.resizable(True, False)
        
            
        self.iconbitmap(r'icon.ico')
        self.build_path_input = StringVar()
        self.game_page_option = StringVar()
        self.channel_option = StringVar()
        self.build_version_input = StringVar()
        self.console_output = StringVar()
        self.console = scrolledtext.ScrolledText(
            self, wrap=tk.WORD, width=40, height=1.5, font=("Helvetica", 10))

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=1)

        self.style = ttk.Style(self)
        self.style.configure('TLabel', font=('Helvetica', 11, 'bold'))
        self.style.configure('TButton', font=('Helvetica', 11))
        self.style.configure('TEntry', font=('Helvetica', 11))
        

        self.api = itchApi.ItchApi(config.url)
        asyncio.run(self.api.get_games())
        # make array of api.games username and channels
        self.game_pages = self.api.games
        self.game_page_option.set(self.game_pages[0])

        self.layer = 0;
        
        self.draw_path_container()
        self.draw_game_page_container()
        self.draw_channel_container()
        self.draw_version_content()
        self.draw_footer()


    def draw_path_container(self):
        
        tk.Frame(self, height=1, bg="black").grid(
            column=0,columnspan=3, row=self.layer, sticky='EWN',**padding)
        self.layer_indent()
        ttk.Label(self, text="Build Path: ", style="BW.TLabel").grid(
            column=0, row=self.layer, sticky='EWN',**padding_label)
        # self.build_path_input.set(preferences.butlerPath)
        self.layer_indent()
        
        path_entry_field = ttk.Entry(self, textvariable=self.build_path_input)
        path_entry_field.grid(row=self.layer, column=0, columnspan=2,
                              sticky=EWN,**padding_entry)
        
        path_button = ttk.Button(self, text="Browse", command=self.browse_path)
        path_button.grid(row=self.layer,column=2, sticky=EWN, **padding_btn)

    def draw_game_page_container(self):
        
        self.layer_indent()
        ttk.Label(self, text="Game Page: ", style="BW.TLabel").grid(
            column=0, row=self.layer, sticky=EWN, **padding_label)
        self.layer_indent()
        game_page_menu = ttk.Combobox(
            self, textvariable=self.game_page_option, values=self.game_pages)
        game_page_menu.grid(row=self.layer, column=0, columnspan=3,
                            sticky=EWN, **padding)
        game_page_menu['state'] = 'readonly'

    def draw_channel_container(self):
        
        self.layer_indent()
        ttk.Label(self, text="Channel: ", style="BW.TLabel").grid(
            column=0, row=self.layer, sticky=EWN, **padding_label)
        opt = ["Win", "Mac", "Linux"]

        self.channel_option.set(opt[0])
        self.layer_indent()
        channel_option_menu = ttk.Combobox(
            self, textvariable=self.channel_option, values=opt)
        channel_option_menu.grid(
            row=self.layer, column=0, columnspan=3, sticky=EWN, **padding)
        channel_option_menu['state'] = 'readonly'

    def draw_version_content(self):
        
        self.layer_indent()
        label = ttk.Label(self, text="Version: ", style="BW.TLabel").grid(
            column=0, row=self.layer, sticky=EWN, **padding_label)
        self.build_version_input.set("1.0.0")
        self.layer_indent()
        version_entry_field = ttk.Entry(self, textvariable=self.build_version_input).grid(
            row=self.layer, column=0, columnspan=3, sticky=EWN, **padding)

    def draw_footer(self):
        self.layer_indent(2)
        ttk.Button(self, text="Upload Build", command=self.on_build_btn).grid(
            column=0, row=self.layer, columnspan=3, ipady=20, sticky=SEWN, **padding_btn)
        
        progressbar = ttk.Progressbar(self, orient=tk.HORIZONTAL, length=200, mode='determinate')

    def on_build_btn(self):
        asyncio.run(self.on_build())

    def get_console_output(self, value):
        self.console.config(state="normal")
        self.console.delete(1.0, "end")
        self.console.insert(1.0, value)
        self.console.config(state="disabled")
        self.console.update()

    async def on_build(self):
        version = self.build_version_input.get()
        build_path = self.build_path_input.get()
        channel = self.channel_option.get()
        game_page = self.game_page_option.get()
        
        output = await self.api.upload_build(build_path, game_page, channel, version)
        self.console_output.set(output)
        self.get_console_output(output)
        
    def layer_indent(self,height = 1): 
        self.layer += height

    def browse_path(self):
        file_path = filedialog.askopenfilename(
            initialdir="/", title="Select file", filetypes=(("Zip files", "*.zip"),("Rar files","*.rar"),("all files", "*.*")))
        self.build_path_input.set(file_path)

class Config:
    def __init__(self):
        self.apiToken = None
        self.butlerPath = None

        with open("config.txt", 'r') as config_file:
            #read the file line by line
            for line in config_file:
                #split the line by the = sign
                splitLine = line.split('=')
                #if the first part of the line is the api token
                if splitLine[0] == 'apiToken':
                    #set the api token to the second part of the line
                    self.apiToken = splitLine[1].strip()
                #if the first part of the line is the butler path
                # elif splitLine[0] == 'butlerPath':
                #     #set the butler path to the second part of the line
                #     self.butlerPath = splitLine[1].strip()       
        self.url = f'https://itch.io/api/1/{self.apiToken}/my-games'
  
config = Config()

if __name__ == "__main__":
    app = App()
    app.mainloop()