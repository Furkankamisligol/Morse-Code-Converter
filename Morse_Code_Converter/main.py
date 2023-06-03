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

t1_convert = input("What sentence you want to converted to Morse Code\n")
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
print(converted)
