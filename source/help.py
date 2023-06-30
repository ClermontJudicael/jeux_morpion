import customtkinter as ctk

texte = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris facilisis finibus aliquet. Proin placerat, purus interdum pulvinar tempor, risus velit varius mauris, vel blandit augue massa eget purus. Nam vulputate eleifend odio. Donec et mauris ac elit euismod efficitur. Etiam efficitur gravida vulputate. Pellentesque fringilla nibh non arcu maximus, eget efficitur diam auctor. Duis efficitur, massa eget gravida tempus, purus ligula imperdiet purus, at finibus lorem magna eget lectus. Vestibulum vel porttitor leo, vitae laoreet nunc. Cras mauris lectus, rutrum et mauris at, convallis imperdiet ante. Phasellus posuere dignissim orci egestas maximus. Pellentesque eget luctus leo. Nunc fermentum facilisis lacus vitae malesuada. Duis mattis pellentesque egestas. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas eros eros, tempus a ornare et, feugiat vitae nisl. Maecenas interdum ante id odio tincidunt accumsan."


class MyFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = ctk.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)

        for i in range(4):
            self.frame = ctk.CTkFrame(
                self, border_color="#ffffff", width=500)
            self.frame.grid(row=i, column=20, pady=16)
        self.etiquette = ctk.CTkLabel(self.frame, text=texte)
        self.etiquette.pack()


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.my_frame = MyFrame(master=self, width=1250, height=600)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20)


app = App()
app.mainloop()
