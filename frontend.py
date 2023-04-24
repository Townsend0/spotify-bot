import tkinter
from backend import Send
import tkinter.messagebox 
COLOR = "#3A4F7A"

class Gui(Send):
        
    def screen(self):
        
        self.window = tkinter.Tk()
        self.window.title("Musicy")
        self.window.geometry("400x400")
        self.window.config(bg = COLOR)
        
        
    def entries(self):
        
        self.eday = tkinter.Entry(width = 2, border = 0, highlightthickness = 0)
        self.eday.place(x = 80, y = 300)
        self.emonth = tkinter.Entry(width = 2, border = 0, highlightthickness = 0)
        self.emonth.place(x = 210, y = 300)
        self.eyear = tkinter.Entry(width = 4, border = 0, highlightthickness = 0)
        self.eyear.place(x = 320, y = 300)
        self.e_ig = tkinter.Entry(border = 0, highlightthickness = 0, width = 24)
        self.e_ig.place(x = 100, y = 250)
        
        
    def labels(self):
        
        self.l_ig = tkinter.Label(text = "E-mail:", bg = COLOR).place( x = 25, y = 250)
        self.lday = tkinter.Label(text = "Day:", bg = COLOR).place(x = 25, y = 300)
        self.lmonth = tkinter.Label(text = "Month:", bg = COLOR).place(x = 130, y = 300)
        self.lyear = tkinter.Label(text = "Year:", bg = COLOR).place(x = 260, y = 300)
        
        
    def imgs(self):
        
        self.img = tkinter.PhotoImage(file = "music-150x150.png")
        self.canvas = tkinter.Canvas(width = 200, height = 200, bg = COLOR, highlightthickness = 0)
        self.canvas.pack(pady = 25)
        self.canvas.create_image(100, 100, image = self.img)
        
        
    def buttons(self):
        
        self.sendimg = tkinter.PhotoImage( file = "direct-30x30.png")
        self.send = tkinter.Button(image = self.sendimg, bg = COLOR, highlightthickness = 0, border = 0)
        self.send.pack(side = "bottom", pady = 15)
        
        def send_mail():
            
            if self.eday.get() == "" or self.emonth.get() == "" or self.e_ig.get() == "" or self.eyear.get() == "":
                tkinter.messagebox.showerror("Error", "Dont leave any of the data fields empty")
                
            else:
                self.get_info()
                self.get_songs()
                self.create_spotify_list()
                self.add_songs_to_list()
                self.send_via_mail()
                    
        self.send.config(command = send_mail)
    
    