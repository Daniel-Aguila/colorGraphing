import csv


m = ["blue", "red", "green", "yellow"]  # Colors
nva = 0  # counts number of times an initial color assigned to a variable or color assignted ot a variable is changed
stateNames = []
result = {} #dictionary for format result
with open('AustraliaCSV.csv') as file:
    reader = csv.reader(file)
    stateNames = next(reader)
    lines = list(reader)

stateNames = stateNames[1:] #We have the state names
vertices = 0 #Number of vertices
for i in stateNames:
    vertices += 1

#Fill Empty states
for state in stateNames:
    result[state] = ""

def check(color, state):
    checkingCol = ""
    for i in range(1,vertices+1):
        if lines[state][i] == str(1):
                checkingCol = result[stateNames[i-1]]
                if color == checkingCol:
                    return False
    return True

def color(state):
    for col in m:
        if check(col, state):
            return col
def main():
    x = 0
    currentState = stateNames[0]
    for state in stateNames:
            result[state] = color(x)
            x += 1
    with open('output.txt','w',encoding="utf-8") as w:
        w.write(currentState + ":" + str(result[currentState] + "->")),
        del result[currentState];
        w.write(str(result))

if __name__ == '__main__':
   main()
