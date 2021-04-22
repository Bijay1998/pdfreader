import pyttsx3
import PyPDF2
#opeanng book
b = open('oracle.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(b)
pages = pdfReader.numPages

print(pages)
#speaker  initialize
speaker = pyttsx3.init()
#rate
rate = speaker.getProperty('rate') #getting rate
print(rate)
speaker.setProperty('rate', 150) #setting new voice rate

#getting details of current voice
voices = speaker.getProperty('voices')
print(voices)
#changing index, changes voice, 1 for male and 0 for female
speaker.setProperty('voice', voices[1].id)

for num in range(7, pages):
    page = pdfReader.getPage(7)
    text = page.extractText()
    #make it speak
    speaker.say(text)
    speaker.runAndWait()GIR

#Saving Voice to a file
speaker.save_to_file('hello world', 'test.mp3')
speaker.runAndWait()
