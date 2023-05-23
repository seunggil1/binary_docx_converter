import os
import json

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
                        json[dir] = b''.join(f.readlines())
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
            result[dir] =  vsixToText(VSIXDIR + "/" + dir)


if __name__ == '__main__':
    converter()