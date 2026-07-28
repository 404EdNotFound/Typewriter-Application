# Importing Tkinter Modules
from tkinter import *
from tkinter import filedialog, messagebox

# Class Created for creating a textbox
class Textbox():
    # Initialising the attributes of the class
    def __init__(self):
        self.text = ""
        self.characterCount = self.wordCount = 0
    
    # Retrieves teh text
    def getText(self):
        self.text = textBox.get("1.0", END).strip()
        return self.text
    
    # Deletes the Text
    def clearText(self):
        textBox.delete("1.0", END)
    
    # Save the text
    def saveFile(self):
        global filepath

        retrievedText = ""        
        temp_file = filedialog.asksaveasfilename(defaultextension = "txt", filetypes=[("All Files", "*.*"), ("Text File", ".txt")])
        
        if not temp_file: return
        
        filepath = temp_file
        with open(filepath, "w") as file:
            retrievedText = textBoxObject.getText()
            file.write(retrievedText)
        
        textBoxObject.clearText()
    
    # Loads the Text
    def loadFile(self):
        global filepath
        
        retrievedText = ""
        temp_file = filedialog.askopenfilename(defaultextension = "txt", filetypes=[("All Files", "*.*"), ("Text File", ".txt")])
                
        if not temp_file: return
        
        filepath = temp_file
        
        with open(filepath, "r") as file:
            retrievedText = file.read()
            textBox.insert(END, retrievedText)
    
    # Calculates Word Count
    def calculateWordCount(self):
        self.text = self.getText()
        self.wordCount = len(self.text.split(" "))
    
    # Calculates Character Count
    def calculateCharacterCount(self):
        self.text = self.getText()
        self.characterCount = len(self.text)

# Updating the Word and Character count every second which is necessary
def updateStat(event):
    textBoxObject.calculateCharacterCount()
    textBoxObject.calculateWordCount()
    statsLabel.config(text = f"Words: {textBoxObject.wordCount}, Characters: {textBoxObject.characterCount}")

# Main Interface Page
def mainPage():
    global textBox, statsLabel
    
    text_box_window = Tk()
    text_box_window.title("Online TypeWriter")

    title = Label(text_box_window, text = "Online Typewriter!", foreground = "Black", font = ("Impact", "40", "bold", "underline"))
    textBox = Text(text_box_window)
    
    wordCharFrame = Frame(text_box_window, background = "Black")
    statsLabel = Label(wordCharFrame, text = f"Words: , Characters: ")
    
    buttonFrame = Frame(text_box_window, background = "Black", highlightbackground = "Black", highlightthickness = 2)
    clearButton = Button(buttonFrame, text = "Clear!", command = textBoxObject.clearText)
    saveButton = Button(buttonFrame, text = "Save Text", command = textBoxObject.saveFile)
    loadButton = Button(buttonFrame, text = "Load Text", command = textBoxObject.loadFile)

    title.pack()
    textBox.pack()
    
    wordCharFrame.pack()
    statsLabel.pack()

    buttonFrame.pack()
    clearButton.pack()
    saveButton.pack()
    loadButton.pack()
        
    return text_box_window

textBoxObject = Textbox()

textBoxScreen = mainPage()
textBoxScreen.bind('<Key>', updateStat)
textBoxScreen.mainloop()