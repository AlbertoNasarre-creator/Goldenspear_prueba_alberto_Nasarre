import crcmod
from functools import reduce
import enchant
from enchant.checker import SpellChecker
#convert string to hex
def toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0'+hv
        lst.append(hv)
    
    return reduce(lambda x,y:x+y, lst)


def calculate_crc(string):

    
    hexnumber = toHex(string)

    crc32_func = crcmod.predefined.mkCrcFun('crc-8')
    data = bytearray.fromhex(str(hexnumber))
    data_final = hex(crc32_func(data))

    i = int(data_final, 16)
    return i


def encrypt_cesar(text,s):
   result = ""
   # transverse the plain text
   for i in range(len(text)):
      char = text[i]

      if char.isalpha()==False:

         result += char
      # Encrypt uppercase characters in plain text
      
      elif (char.isupper()):
          result += chr((ord(char) + s-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
      else:
          result += chr((ord(char) + s - 97) % 26 + 97)
   return result



def orthographic_corrector(string):

    chkr = enchant.checker.SpellChecker("en_GB")
    chkr.set_text(string)
    for err in chkr:
        sug = err.suggest()[0]
        err.replace(sug)

    result = chkr.get_text()
    return (result)