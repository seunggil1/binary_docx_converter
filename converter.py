import os
import json
import base64

def vsixToText(parentDirectory):
    json = dict()
    for dir in os.listdir(parentDirectory):
        nowDirectory = parentDirectory + "/" + dir
        if os.path.isfile(nowDirectory) :
            failed = False
            with open(nowDirectory, 'r', encoding="utf-8") as f:
                try :
                    json[dir] = ''.join(f.readlines())
                except Exception as e:
                    failed = True
            if failed: # 인코딩 ANSI로 시도
                with open(nowDirectory, 'rb') as f:
                    print(nowDirectory, "is opened as binary")
                    try :
                        binaryData = b''.join(f.readlines())
                        json[dir] = str(base64.b64encode(binaryData), encoding='UTF-8')
                    except Exception as e:
                        json[dir] = ''
                        print("Error", dir, ":", e)
        else:
            json[dir] = vsixToText(nowDirectory)
    return json

def textToVsix(fileName):
    pass


def converter():
    VSIXDIR = "./vsix"
    TEXTDIR = "./text"

    result = dict()
    for dir in os.listdir(VSIXDIR):
        if not os.path.isfile(dir) :
            print("convert vsix to json :", dir)
            result[dir] =  vsixToText(VSIXDIR + "/" + dir)
        with open('./text/' + dir +'.json', 'w') as fp:
            json.dump(result, fp)

if __name__ == '__main__':
    converter()