import re
import fake as f

def docToText(filename):
    # use with/as to close file resource after using it
    with open(filename, "r") as f:
        file = f.read()
        return file

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

# need to account for decimal and fraction answers. split() should not split up those answers
def numberedTextToAnswers(txt):
    txt = txt.upper()
    # using python lookarounds
    txt = re.sub("(?<=[0-9])(\\.)(?=[0-9])", "+", txt)
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
    
    return incorrect

def createTextFile(count):
    createFile = open("count_incorrect.txt", "w+")
    createFile.write("You got {} wrong".format(count))



if __name__ == "__main__":
    real = docToText("test.txt")
    real = numberedTextToAnswers(real)
    marked = docToText("input.txt")
    marked = numberedTextToAnswers(marked)

    count = grader(marked, real)
    createTextFile(count)

    # f.test()
