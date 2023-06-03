from tkinter import *

Characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
              "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z", "w",
              "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", ",", ":",
              ";", "?", "'", '"', "!", "/", "(", ")", "=", "+", "-", "_", "@"]
Morse_Characters = ["._", "_...", "_._.", "_..", ".", ".._.", "__.", "....", "..",
                    ".___", "_._", "._..", "__", "_.", "___", ".__.", "__._", "._.",
                    "...", "_", ".._", "..._", "_.._", "_.__", "__..",
                    ".____", "..___", "...__", "...._", ".....", "_....", "__...", "___..", "____.", "_____",
                    "......", "._._._", "___...", "_._._.", "..__..", ".____.", "._.._.", "_._.__", "_.._.",
                    "_.__.", "_.__._", "_..._", "._._.", "_...._", "..__._", ".__._."]


def button_got_clicked():
    t1_convert = str(input1.get())
    t2_convert = t1_convert.lower()
    to_convert = t2_convert.replace(" ", "")
    to_convert_letters = [*to_convert]
    for letter in to_convert_letters:
        morse_equivalent = Morse_Characters[Characters.index(letter)]
        morse_ready = f"{morse_equivalent} >/ "
        x = to_convert_letters.index(letter)
        to_convert_letters.pop(x)
        to_convert_letters.insert(x, morse_ready)

    converted_ptype = "".join(to_convert_letters)
    c_list = converted_ptype.split('>')
    c_list.pop(-1)
    converted = "".join(c_list)
    morse_label.config(text=converted)


def copy_button_got_clicked():
    to_copy = morse_label["text"]
    window.clipboard_clear()
    window.clipboard_append(to_copy)


window = Tk()
window.title("Morse Converter")
window.minsize(width=400, height=500)
window.config(padx=20, pady=20)

info_label = Label(text="Morse Converter", font=("Ariel", 16,))
info_label.grid(row=0, column=3, padx=5, pady=5)

copy_button = Button(text="Copy", command=copy_button_got_clicked, font=("Ariel", 16,))
copy_button.grid(row=5, column=4, padx=5, pady=5)

convert_button = Button(text="Convert", command=button_got_clicked, font=("Ariel", 16,))
convert_button.grid(row=1, column=4, padx=5, pady=5)

input1 = Entry(width=50, font=("Ariel", 16,))
input1.grid(row=1, column=3, padx=5, pady=5)

morse_label = Label(text="", font=("Ariel", 16,), width=50, wraplength=500)
morse_label.grid(row=4, column=3, padx=5, pady=5)


window.mainloop()
