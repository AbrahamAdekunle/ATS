import string

vowels = ['a', 'e', 'i', 'o', 'u']
v_char = ['#', '$', '%', '&', '*']
alpha_char = string.ascii_lowercase
reversed_alpha_char = alpha_char [::-1]
alpha_char_u = string.ascii_uppercase
spec_char = string.punctuation
digits = string.digits

def encode(enc:str):
    encrypt =[]

    for s in enc:
        if s in vowels:
            encrypt.append(v_char[vowels.index(s)])
        elif s in spec_char:
            encrypt.append("|" + s)
        elif s in alpha_char + alpha_char_u:
            encrypt.append(s.swapcase())
        elif s in digits:
            encrypt.append("^" + reversed_alpha_char[digits.index(s)])
        elif s in spec_char:
            encrypt.append("^" + s)
    return "".join(encrypt)




word = input("kindly input the word you want to encrypt ")

print(encode(word))



def decode (decr:str):
    decrypt = []
    dec = list(decr)
    for item in range(0, len(dec)):
        if dec[item] in v_char:
            decrypt.append(vowels[v_char.index(dec[item])])
        elif dec[item] == '^':
            decrypt.append(reversed_alpha_char.index(dec[item + 1]))
            # decrypt.append(digits(reverse_alpha_char.index(dec[item + 1])))
            dec.pop(dec[item + 1])
        elif dec[item] == "|":
            decrypt.append(dec[item + 1])
            dec.pop(dec[item + 1])
        elif dec[item] in alpha_char_u + alpha_char:
            decrypt.append(dec[item].swapcase())


    return "".join(decrypt)



word = input("kindly input the word you want to decrypt ")

print(decode(word))











# def decoded(decr: str):
#     decrypt = []
#
#     for x in decr:
#         if x in v_char:
#             decrypt.append(vowels[v_char.index(x)])
#         elif x == '^':
#             decrypt.append(reversed_alpha_char.index[(x)+ 1])
#             # decrypt.append(digits(reverse_alpha_char.index(x + 1)))
#             x.pop((x) + 1)
#         elif x == "|":
#             decrypt.append (decr.index[(x) + 1])
#             x.pop((x) + 1)
#         elif x in alpha_char_u + alpha_char:
#             decrypt.append (x.swapcase())
#
#         return "".join(decrypt)
#
#
# word = input("kindly input the word you want to decrypt ")
#
# print(decoded(word))