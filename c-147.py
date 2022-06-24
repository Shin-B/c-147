from tkinter import *
root=Tk()
root.geometry("400x300")
root.title("ASCII")

inputbox=Entry(root)
inputbox.place(relx=0.5,rely=0.3,anchor=CENTER)

outputLabel=Label(root)
outputencrypt=Label(root)

def ascii():
    output=""
    encrypt_output=""
    name=inputbox.get()
    for k in name:
        asciivalue=ord(k)
        previous=chr(asciivalue-1)
        encrypt_output=encrypt_output + " " + previous
        output=output +" "+ str(asciivalue)
    outputLabel['text']="ASCII CODE IS : " + output
    outputLabel.place(relx=0.5,rely=0.7,anchor=CENTER)
    outputencrypt['text']="Encrypted code is : " + encrypt_output
    outputencrypt.place(relx=0.5,rely=0.8,anchor=CENTER)
    
    
btn=Button(root,text="CONVERT TO ASCII",bg="lightblue",command=ascii)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
        



root.mainloop()
