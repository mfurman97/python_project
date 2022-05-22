from logging import root
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk



root = tk.Tk()


root.geometry("800x500")  # Size of the window 
root.title('VAR')
my_font1=('times', 18, 'bold')


b1 = tk.Button(root, text='Upload Photo', 
   width=20,command = lambda:upload_photo())
b1.grid(row=2,column=1) 


b2 = tk.Button(root, text='Upload Video', 
   width=20,command = lambda:upload_video())
b2.grid(row=2,column=2) 



def upload_photo():
    global img
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(multiple=True,filetypes=f_types)
    img = ImageTk.PhotoImage(file=filename)
    b2 =tk.Button(root,image=img) # using Button 
    b2.grid(row=3,column=1)
    col=1 # start from column 1
    row=3 # start from row 3 
    for f in filename:
        img=Image.open(f) # read the image file
        img=img.resize((100,100)) # new width & height
        img=ImageTk.PhotoImage(img)
        e1 =tk.Label(my_w)
        e1.grid(row=row,column=col)
        e1.image = img
        e1['image']=img # garbage collection 
        if(col==3): # start new line after third column
            row=row+1# start wtih next row
            col=1    # start with first column
        else:       # within the same row 
            col=col+1 # increase to next column   

def upload_video():
    global img
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = ImageTk.PhotoImage(file=filename)
    b2 =tk.Button(root,image=img) # using Button 
    b2.grid(row=3,column=1)




root.mainloop()  # Keep the window open