import re
import fake as f

def docToText(filename):
    file = open(filename, "r")
    return file.read()

def snapToText():
    # screenshot of text
    pass

def picToText():
    # photo of text
    pass

def textToAnswers(txt):
    txt = txt.upper()
    answers = txt.split()
    nums = list(range(1,len(answers)+1))
    d = dict((num, answers[num-1]) for num in nums)
    return d

def numberedTextToAnswers(txt):
    txt = txt.upper()
    txt = re.split("[ \\.\\)\\-\\n]+", txt)
    d = dict(zip(txt[::2], txt[1::2]))
    return d

# need to make a function that allows me to distinguish between texts that have only answers and numbered answers
def formatIdentifier():
    pass

def grader(marked, real):
    incorrect = 0
    for k, v in marked.items():
        if(real[k] != v):
            incorrect += 1
    
    print("You got {} wrong".format(incorrect))

if __name__ == "__main__":
    real = docToText("test.txt")
    real = numberedTextToAnswers(real)
    marked = docToText("input.txt")
    marked = numberedTextToAnswers(marked)

    grader(marked, real)

    f.test()
