import customtkinter
import tkinter
import webbrowser

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

url = []
page = customtkinter.StringVar()
addedPages = customtkinter.StringVar()

def saveURL():

    new_page = page.get()
    if new_page:
        print("Hmdl")
        #print(page.get())
        url.append(page.get())
        addedPages.set("\n".join(url))
        page.set("")

def open():
    for entry in url:
        webbrowser.open(entry)
   


frame = customtkinter.CTkScrollableFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Mr. Friend", font=("Roboto", 24))
label.pack(pady=12, padx =10)


entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Website", textvariable=page)
entry1.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Add Page to Setup", command=saveURL)
button.pack(pady=12, padx=10)




entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Number of Page you want to delete", textvariable=page)
entry1.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Delete", command=saveURL)
button.pack(pady=12, padx=10)



label = customtkinter.CTkLabel(master=frame, text="Added Websites", font=("Roboto", 24))
label.pack(pady=12, padx =10)


entry1 = customtkinter.CTkLabel(master=frame, textvariable=addedPages)
entry1.pack(pady=12, padx=10)





button = customtkinter.CTkButton(master=frame, text="Start",command=open)
button.pack(pady=12, padx=10)

root.mainloop()