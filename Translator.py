import customtkinter as ctk
from googletrans import Translator,LANGUAGES 

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.title("Language Translator")

        ctk.set_appearance_mode("System") 
        ctk.set_default_color_theme("dark-blue") 

        # add widgets to app
        label = ctk.CTkLabel(self, text="Translator", font=("Time New Roman" ,32,"bold"))
        label.place(relx=0.5, rely=0.01, anchor=ctk.N)

        # Lable for input box
        lab_txt=ctk.CTkLabel(self,text="Source Text", font=("Time New Roman" ,20,"bold"))
        lab_txt.place(relx=0.32, rely=0.2, anchor=ctk.E)

        # Lable for output box
        lab_txt=ctk.CTkLabel(self,text="Dest Text", font=("Time New Roman" ,20,"bold"))
        lab_txt.place(relx=0.83, rely=0.2, anchor=ctk.E)
        
        # Input TextBox
        self.sorc_txt = ctk.CTkTextbox(self, font=("Roboto" ,14), wrap=ctk.WORD) 
        self.sorc_txt.insert("0.0", "Input")
        self.sorc_txt.place(relx=0.4, rely=0.5, anchor=ctk.E)

        # Output TextBox
        self.dest_txt = ctk.CTkTextbox(self, font=("Roboto" ,14),wrap=ctk.WORD) 
        self.dest_txt.insert("0.0", "Output")
        self.dest_txt.place(relx=0.6, rely=0.5, anchor=ctk.W)

        lang_lst = list(LANGUAGES.values())

        # Input language selection Dropdown
        self.combo_sor = ctk.CTkOptionMenu(self,values=lang_lst, hover=True) 
        self.combo_sor.place(relx=0.4, rely=0.8, anchor=ctk.E) 
        self.combo_sor.set("english")

        # Use CTkButton instead of tkinter Button
        button = ctk.CTkButton(master=self, text="Translate", hover=True, hover_color="green", command=self.change)
        button.place(relx=0.5, rely=0.95, anchor=ctk.S)

        # Output language selection Dropdown
        self.combo_dest = ctk.CTkOptionMenu(self,values=lang_lst, hover=True) 
        self.combo_dest.place(relx=0.6, rely=0.8, anchor=ctk.W) 
        self.combo_dest.set("english")

    def change(self): # Action function for the button
        src = self.combo_sor.get() 
        dest = self.combo_dest.get() 
        msg = self.sorc_txt.get(1.0,ctk.END)

        translator = Translator() 
        translated_txt = translator.translate(msg, dest, src) # translator

        self.dest_txt.delete("0.0",ctk.END) # Delete previous entry of the output box
        self.dest_txt.insert("0.0", translated_txt.text) # Insert New Entry in the input box


if __name__ == "__main__":
    app = App()
    app.mainloop()