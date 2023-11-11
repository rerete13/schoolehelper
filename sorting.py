from detection import get_text
import re
import string

x = get_text('2.png')


letters = list(string.ascii_uppercase)

def formatting(text:str):
    text = text.splitlines()
    data = []
    for i in text:
        if len(i) < 5:
            continue
        else:
            data.append(i)
        
    question = data[0]
    res = ''
    res += question + '\n'
    lenth_text = len(data)
    for i in range(0, lenth_text-1):
        res += f'{letters[i]}. ' + data[1:][i] + '\n'

    
    return res


print(formatting(x))