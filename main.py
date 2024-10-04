import customtkinter
import webbrowser
import json
import os

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")


url = {}  
config_file = "urls.json"

page = customtkinter.StringVar()  
addedPages = customtkinter.StringVar()  
idOfPage = customtkinter.StringVar()  


def loadURLs():
    global id
    if os.path.exists(config_file):
        with open(config_file, "r") as file:
            url.update(json.load(file))  
            id = str(int(max(url.keys(), default="0")) + 1) 
            formatted_pages = [f"{key}: {value}" for key, value in url.items()]
            addedPages.set("\n".join(formatted_pages))  



def saveURLs():
    with open(config_file, "w") as file:
        json.dump(url, file)  


def saveURL():
    global id
    new_page = page.get()
    if new_page:
        url[id] = new_page 
        saveURLs()  
        formatted_pages = [f"{key}: {value}" for key, value in url.items()]
        addedPages.set("\n".join(formatted_pages)) 
        page.set("") 
        id = str(int(id) + 1)  


def openURLs():
    for entry in url.values():  
        webbrowser.open(entry)


def deleteURL():
    toDelete = idOfPage.get()  
    if toDelete in url:
        del url[toDelete] 
        saveURLs() 
        formatted_pages = [f"{key}: {value}" for key, value in url.items()]
        addedPages.set("\n".join(formatted_pages))  
        print(f"Seite mit ID {toDelete} gelöscht.")
    else:
        print(f"Keine Seite mit ID {toDelete} gefunden.")


frame = customtkinter.CTkScrollableFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Mr. Friend", font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Website", textvariable=page)
entry1.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Add Page to Setup", command=saveURL)
button.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="ID der Seite, die gelöscht werden soll", textvariable=idOfPage)
entry2.pack(pady=12, padx=10)

button_delete = customtkinter.CTkButton(master=frame, text="Delete", command=deleteURL)
button_delete.pack(pady=12, padx=10)

label = customtkinter.CTkLabel(master=frame, text="Added Websites", font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry3 = customtkinter.CTkLabel(master=frame, textvariable=addedPages)
entry3.pack(pady=12, padx=10)

button_start = customtkinter.CTkButton(master=frame, text="Start", command=openURLs)
button_start.pack(pady=12, padx=10)


loadURLs()

root.mainloop()
