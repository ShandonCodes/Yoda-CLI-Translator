import requests as req
import sys

def readInput():
    text = ''
    for word in sys.argv[1:]:
        text += f' {word}'

    return text

def translate():
    text = readInput()

    if text == '':
        return

    res = req.get(f'https://api.funtranslations.com/translate/yoda.json?text={text}')

    originalText = res.json()['contents']['text']
    translatedText = res.json()['contents']['translated']

    print(f'Original: {originalText}\nTranslated: {translatedText}')

if __name__ == '__main__':
    translate()
