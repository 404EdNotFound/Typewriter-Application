# Importing Tkinter Modules
from tkinter import *
from tkinter import filedialog, messagebox

# Class Created for creating a textbox
class Textbox():
    # Initialising the attributes of the class
    def __init__(self):
        self.text = ""
        self.letterSet = []
        self.characterCount = self.wordCount = 0
    
    # Retrieves the text
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
        
        textBoxObject.clearText() #Deletes the text from the textbox
    
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
            retrievedText = textBoxObject.getText() #assigns the text to the retrieved text
        
        # Uploading the word count and calculating methods (not the best idea -> Uses Repetition)
        self.calculateCharacterCount()
        self.calculateWordCount()
        statsLabel.config(text = f"Words: {self.wordCount}, Characters: {self.characterCount}")
    
    # Calculates Word Count
    def calculateWordCount(self):
        self.text = self.getText()
        self.letterSet = self.text.split(" ")
        self.letterSet = [item for item in self.letterSet if item != ''] #Separates the spaces
        self.wordCount = len(self.letterSet)
    
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
    
    wordCharFrame = Frame(text_box_window, background = "Black", highlightbackground = "Black")
    statsLabel = Label(wordCharFrame, text = f"Words: , Characters: ", font = ("Impact", "40", "bold", "underline"))
    
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