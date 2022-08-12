#Creating a Notepad:

from tkinter import *
import os
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename


def newFile():
    global file #Now, whenever we will call this function the value of "file" will be modified from this function.
    root.title("Untitled - Notepad") 
    file = None
    TextArea.delete(1.0, END) #delete() is the function of TextArea widget.



def openFile():
    global file
    file = askopenfilename(defaultextension = "txt", filetypes = [("All File", "*.*"), ("Text Documents")]) #File can be of any type and defualt extension of the file is ".txt". This function will help us in opening the files from the system.
    #So what will happen above is file will be selected and that file will be assigned to the variable "file" that means all the content of the file will now be stored in the variable "file".

    if file == "": #In case there is not file to open, that means we clicked on open but didn't selected any file to open, in that case file will again become "None" that means nothing is there.
        file = None
    else:
        root.title(os.path.basename(file) + "- Notepad") #It will help us in getting the name of the file only and trimming the path of file and it will replace the title of notepad "untitled - Notepad" with "Name Of File -Notepad" while opening the file.
        TextArea.delete(1.0, END) #It will delete all the existing content in the TextArea.
        f = open(file, "r") #Open the file
        TextArea.insert(1.0, f.read()) #Read the file starting from character 1 which is 1.0 to end of the file and insert that into the TextArea.
        f.close()
        


def saveFile():
    global file #This askesaveasfilename() method opens the dialog box in which we can save the file.
    if file == None: #If it's a new file hence it isn't saved earlier hence "file = None", So now we will save it as a new file.
        file= asksaveasfilename(initialfile = "Untitled.txt",
        defaultextension = ".txt", 
        filetypes = [("All Files", "*.*"), ("Text Documnets", "*.txt")]) #In case we don't provide any file name so "Untitle -Notepad" will be the default name of the file to save the file.
         
        if file == "": #If we haven't selected any file to save.
            file = None #It means there is no file.
        else:
            #Save as a new file.
            f = open(file, "w")
            f.write(TextArea(1.0, END))
            f.close()

            root.title(os.path.basename(file)+ " - Notepad") #Name of the file will be updated.
            print("File Saved Successfully!")

    else:
        #Save the file.
        f = open(file, "w")
        f.write(TextArea.get(1.0, END)) #Replace all the existing content of the file with the current contenct written in TextArea.
        f.close()


def rename():
    global file
    file= asksaveasfilename(initialfile = file,
                                          defaultextension = ".txt", 
                                          filetypes = [("All Files", "*.*"), ("Text Documnets", "*.txt")])
    root.title(os.path.basename(file)+ " - Notepad")


def quitApp():
    root.destroy() #It will close the app.

def cut():
    TextArea.event_generate(("<<Cut>>")) #It will handle the cut event, That means we don't have to write anything for performing the cut operation this method will handle the cut operation.

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("NOtepad", "Notepad by Deepak")

if __name__ == '__main__':
    root = Tk()
    root.title("Untititle - Notepad")
    root.wm_iconbitmap("notepad_icon.ico")
    root.geometry("650x750")
    
    #Adding text area in notepad where we will add text.
    TextArea = Text(root, font = "lucida 13") #It will create an area we will write the text.
    file = None #It means we haven't opened any file iin notepad yet.
    TextArea.pack(expand = True, fill = BOTH) #Packing the TextArea widget to place the Text area into my root gui window, So we can write in notepad. 
    #Expand = True, It will expand the TextArea in the whole gui window except the menu bar.

    #Creating menus in menu bars.
    #File Menu Starts.
    menubar = Menu(root) #packing menu in root gui window. It will create a menu bar.
    FileMenu= Menu(menubar, tearoff = 0)

    #To open a new file.
    FileMenu.add_command(label = "New", command = newFile) #It's a dropdown of File which will appear in menu bar.

    #To open an existing file.
    FileMenu.add_command(label = "Open", command = openFile)

    #To rename a file.
    FileMenu.add_command(label = "Rename", command = rename)

    #To save the current file.
    FileMenu.add_command(label = "Save", command = saveFile)
    FileMenu.add_separator() #Adding a separator. It will add a horizontal line between sub menu "save" and "exit".
    #To close the notepad.
    FileMenu.add_command(label = "Exit", command = quitApp) #It will close the notepad app.
    
    #Adding a cascade.
    menubar.add_cascade(label = "File", menu = FileMenu) #All the sub-menu options for the File menu in menu bar will come under this File menu.
    #File Menu Ends.

    #Edit Menu.
    #Edit Menu Starts.
    EditMenu = Menu(menubar, tearoff= 0) #Creating a menu and fitting it in the same menubar which we created earlier name "menubar".

    #To give a feature of cut, copy and paste.
    EditMenu.add_command(label ="Cut", command = cut) #When you will click on "Cut" sub menu it will call the function named "cut".
    EditMenu.add_command(label ="Copy", command = copy)
    EditMenu.add_command(label ="Paste", command = paste)

    menubar.add_cascade(label = "Edit", menu = EditMenu) #It will add the "Edit" menubar in our "menubar object" which we created earlier. So menubar object will simply create a menu bar and this menu "Edit" will be added there.
    #Edit Menu Ends.

    #Help menu Starts:
    HelpMenu = Menu(menubar, tearoff = 0) #Creating a menu and fitting it in the same menubar which we created earlier named as "menubar".
    HelpMenu.add_command(label = "About Notepad", command = about)
    menubar.add_cascade(label= "Help", menu = HelpMenu) #It will place the menu "Help" in the menu bar and it will contain about as it's dropdown/submenu.
    #Help menu ends.

    root.config(menu = menubar) #It will create the menu bar and place it according to out defined configuration. That's why it's used in the end only once.


    #Adding Scrollbar in our Notepad:
    Scroll = Scrollbar(TextArea) #Connecting our text area with scroll bar.
    Scroll.pack(side = RIGHT, fill = Y)
    Scroll.config(command = TextArea.yview) #Configuring vertical scroll bar, So we move scrollbar vertically.
    TextArea.config(yscrollcommand = Scroll.set) #Configuring the scrollbar for the TextArea in vertical position because "Scroll.set" will insert/set/place/attach the Scrollbar object "Scroll" which we have created for our TextArea.

    root.mainloop()