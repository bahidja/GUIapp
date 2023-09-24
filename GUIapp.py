import tkinter as tk 
import PyPDF2
from PIL import Image , ImageTk
from tkinter.filedialog import askopenfile


root = tk.Tk()

Canves = tk.Canvas(root,width=600,height=300 )
Canves.grid(columnspan=3)

#logo 
logo = Image.open('logo(1).png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1,row=0)




instruction = tk.Label(root,text="Select a PDF faile on your comuter to extracte all its text " ,font = "Raleway" )
instruction.grid( columnspan=3,column=0,row=1)



def open_file():
   browse_text.set("Louding...")
   file = askopenfile(parent=root , mode='rb' ,title='choose a file' , filetypes=[("PDF file",".pdf")])
   if file :
        road_pdf = PyPDF2.PdfReader(file)
        page = road_pdf.pages[0]
        page_c = page.extract_text()
        print(page_c)
        
        #text airea 
        text_box = tk.Text(root, height=10, width= 50 , padx=15, pady=15,)   
        text_box.insert(1.1, page_c)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1,row=3)
        
        browse_text.set("Browse")
    


browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text,command=lambda:open_file(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)

browse_text.set("Browse")
browse_btn.grid(column=1, row=2)


#browse button
# browse_text = tk.StringVar()
# browse_btn = tk.Button(root, textvariable=browse_text, font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
# browse_text.set("Browse")
# browse_btn.grid(column=1, row=2)


Canves = tk.Canvas(root,width=600,height=300 )
Canves.grid(columnspan=3)


root.mainloop()


