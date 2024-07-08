from tkinter import *
from tkinter import messagebox
import base64

# Encryption function
def encrypt():
    global screen
    global code
    global text1
    
    password = code.get()
    message = text1.get(1.0, END).strip()  # Get text from text box and remove trailing newline
    
    if password == "":
        messagebox.showerror("Encryption", "Please enter a password")
        return
    
    if password == "1234":
        try:
            # Encode message to bytes and then base64 encoding
            encode_message = message.encode("utf-8")
            base64_bytes = base64.b64encode(encode_message)
            encrypt_text = base64_bytes.decode("utf-8")
            
            # Create a new window for displaying encrypted text
            screen1 = Toplevel(screen)
            screen1.title("Encryption")
            screen1.geometry("400x250")
            screen1.configure(bg="#ed3833")
            
            # Display labels and encrypted text
            Label(screen1, text="ENCRYPTED TEXT", font=("Arial", 14, "bold"), fg="white", bg="#ed3833").pack(pady=10)
            encrypted_text = Text(screen1, font=("Roboto", 12), bg="white", relief=GROOVE, wrap=WORD, bd=0)
            encrypted_text.insert(END, encrypt_text)
            encrypted_text.pack(padx=20, pady=10, fill=BOTH, expand=True)
        
        except Exception as e:
            messagebox.showerror("Encryption Error", f"Error: {str(e)}")
    
    else:
        messagebox.showerror("Encryption", "Invalid Password")

# Decryption function
def decrypt():
    global screen
    global code
    global text1
    
    password = code.get()
    message = text1.get(1.0, END).strip()  # Get text from text box and remove trailing newline
    
    if password == "":
        messagebox.showerror("Decryption", "Please enter a password")
        return
    
    if password == "1234":
        try:
            # Decode base64 encoded message
            decode_message = base64.b64decode(message)
            decrypt_text = decode_message.decode("utf-8")
            
            # Create a new window for displaying decrypted text
            screen2 = Toplevel(screen)
            screen2.title("Decryption")
            screen2.geometry("400x250")
            screen2.configure(bg="#00bd56")
            
            # Display labels and decrypted text
            Label(screen2, text="DECRYPTED TEXT", font=("Arial", 14, "bold"), fg="white", bg="#00bd56").pack(pady=10)
            decrypted_text = Text(screen2, font=("Roboto", 12), bg="white", relief=GROOVE, wrap=WORD, bd=0)
            decrypted_text.insert(END, decrypt_text)
            decrypted_text.pack(padx=20, pady=10, fill=BOTH, expand=True)
        
        except Exception as e:
            messagebox.showerror("Decryption Error", f"Error: {str(e)}")
    
    else:
        messagebox.showerror("Decryption", "Invalid Password")

# Reset function to clear inputs
def reset():
    global code
    global text1
    
    code.set("")
    text1.delete(1.0, END)

# Main screen function
def main_screen():
    global screen
    global code
    global text1
    
    screen = Tk()
    screen.geometry("400x400")
    screen.title("Encryption and Decryption App - Developed by @thepasswordspoiler")
    screen.configure(bg="#f0f0f0")
    
    # Icon
    image_icon = PhotoImage(file="keys.png")
    screen.iconphoto(False, image_icon)
    
    # Labels and text entry
    Label(screen, text="Enter Text:", fg="black", font=("Arial", 12)).place(x=20, y=20)
    text1 = Text(screen, font=("Roboto", 12), bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=20, y=50, width=360, height=100)
    
    Label(screen, text="Enter Password:", fg="black", font=("Arial", 12)).place(x=20, y=170)
    code = StringVar()
    Entry(screen, textvariable=code, width=20, bd=1, font=("Arial", 12), show="*").place(x=20, y=200)
    
    # Buttons for encryption, decryption, and reset
    Button(screen, text="ENCRYPT", width=15, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=20, y=250)
    Button(screen, text="DECRYPT", width=15, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=160, y=250)
    Button(screen, text="RESET", width=15, bg="#1089ff", fg="white", bd=0, command=reset).place(x=300, y=250)
    
    # Developed by label
    Label(screen, text="Developed by @thepasswordspoiler", fg="#666666", font=("Arial", 10)).place(x=20, y=380)

    screen.mainloop()

# Call the main_screen function to start the application
if __name__ == "__main__":
    main_screen()
