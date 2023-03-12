import random
import tkinter as tk
#proměnjící
velka_pismena = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mala_pismena = "abcdefghijklmnopqrstuvwxyz"
cisla = "0123456789"
znaky = "().-,_:!ˇ%-*/"
length = 12
#nahodny password
use = velka_pismena + mala_pismena + cisla + znaky
passwd = "".join(random.choice(use) for i in range(length))

#vykreslovaní okna
window = tk.Tk()
window.title("Password Generator")
#nadpis
label = tk.Label(text="<--------->")
label.pack()

#přidání tlačítka
def button_clicked():
    label.configure(text=passwd)
button = tk.Button(text="Získej heslo", command=button_clicked)
button.pack() 

# hlavní loop
window.mainloop()
