import os
import json
import base64

VSIXDIR = "./vsix"
TEXTDIR = "./text"
def vsixToText(fileLocation, fileName):
    global VSIXDIR
    global TEXTDIR

    with open(fileLocation, 'rb') as f:
        binaryData = b''.join(f.readlines())
        res = str(base64.b64encode(binaryData), encoding='UTF-8')
        with open(TEXTDIR + "/" + fileName + '.txt', 'w') as g:
            g.write(res)

def textToVsix(fileLocation, fileName):
    global VSIXDIR
    global TEXTDIR
    with open(fileLocation, 'r') as f:
        data = ''.join(f.readlines())
        res = bytes(data, encoding='UTF-8')
        res = base64.b64decode(res)
        with open(VSIXDIR + "/" + fileName + '.vsix', 'wb') as g:
            g.write(res)

def converter():
    for dir in os.listdir(VSIXDIR):
        if os.path.isfile(dir) :
            print("convert vsix to text :", dir)
            vsixToText(VSIXDIR + "/" + dir)
    
    for dir in os.listdir(TEXTDIR):
        # if os.path.isfile(dir) :
            print("convert text to visx :", dir)
            textToVsix(TEXTDIR + "/" + dir)

if __name__ == '__main__':
    converter()