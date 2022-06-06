import sys, os

index = 1

file = sys.argv[1]

hexString = ""

def FindPNG(index, hexString):
    offset = hexString.find("89504e47")  # find png header "‰PNG"

    if offset != -1:  # if found
        hexStringFixed = hexString[offset:]

        offset = hexStringFixed.find("49454e44ae426082")  # find png end "IEND®B`‚"

        hexStringFixed = hexStringFixed[:offset+16]  # removes everything after the png end

        hexArray = [hexStringFixed[i:i + 2] for i in range(0, len(hexStringFixed), 2)]  # this converts the hex string into hex list

        newFileName = os.path.basename(file)[:-4] + str(index) + ".png"

        with open(newFileName, "wb") as w:
            for i in hexArray:
                w.write(bytes.fromhex(i))

        restOfString = hexString[offset + 16:]
        rtrnTuple = (restOfString, index + 1)
        return rtrnTuple

    else:  # not found
        print(f"file does not seem to include png's")
        return("we're done here")



with open(file, "rb") as f:
    while (byte := f.read(1)):
        hexString = hexString + byte.hex()

while(True):
    result = FindPNG(index, hexString)
    if type(result) is tuple:
        hexString, index = result
    else:
        print(result)
        break
