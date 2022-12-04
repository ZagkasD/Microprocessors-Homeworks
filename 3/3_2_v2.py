# Gods forgive me for the code I'm about to write


class Element:
    def __init__(self, type, inputs, output):
        self.type = type        # value from elementType
        self.inputs = inputs    # indexes in signalsTable
        self.output = output    # index in signalsTable

# 2-input AND gate
def sp2AND(inputAsp, inputBsp):
    s = inputAsp*inputBsp   # Signal probability
    Esw = 2*s*(1-s)         # Switching activity
    return s

# NOT gate
def NOT(inputCsp):
    s = 1-inputCsp  # Signal probability
    Esw = 2*s*(1-s) # Switching activity
    return s

def process(Element, signalsTable):
    if (Element.type == 'AND'):
        signalsTable[Element.output] = sp2AND(signalsTable[Element.inputs[0]],signalsTable[Element.inputs[1]])
        
    elif (Element.type == 'NOT'):
        signalsTable[Element.output] = NOT(signalsTable[Element.inputs[0]])
    
# truth table of model
# a b c | e f | d
# 0 0 0 | 0 1 | 0
# 0 0 1 | 0 0 | 0
# 0 1 0 | 0 1 | 0
# 0 1 1 | 0 0 | 0
# 1 0 0 | 0 1 | 0
# 1 0 1 | 0 0 | 0
# 1 1 0 | 1 1 | 1
# 1 1 1 | 1 0 | 0

# Apply truth table and check for mistakes
def testbench(elementsTable, signalsTable, truth_table, top_inputs):
    print("Signals")
    # Apply inputs from the truth table
    for row in range(len(truth_table)):
        column = 0
        for k in top_inputs:
            signalsTable[k] = truth_table[row][column]
            column += 1
        # Simulate each element/gate
        for k in range(len(elementsTable)):
            process(elementsTable[k], signalsTable)
        
        print(signalsTable)

        # Check if the simulation was correct
        for p in range(len(top_inputs),len(signalsTable)):
            #if signalsTable[3] == truth_table[row][3] and signalsTable[4] == truth_table[row][4] and signalsTable[5] == truth_table[row][5]:
            if list(signalsTable.values())[p] == truth_table[row][p]:
                continue
            else:
                print("Testbench failed.") 
                exit()
    print("\nTestbench successful")
    
    
def readfile(input_file, elementTypes, elements_table,top_inputs,signals_table):
    flag_top_inputs = 0 # If there're top inputs, set flag = 1
    line_number = 0 # For keeping track the line in the file
                    # which corresponds to each element in the elements list
    
    # Every line contains one element with each signals
    for line in input_file:
        word_counter = 0    # The first word in each line is the element type
                            # The second word is the output
                            # The rest of the words are the inputs
        # The first line might be the inputs declaration
        # line.split()[0] turns the line into a matrix and returns the first value
        if line.split()[0] == 'TLPINPUTS':
            flag_top_inputs = 1
            # Go through each input
            for i in range (len(line.split())-1):
                top_inputs.append(line.split()[i+1]) # just for the length
                signals_table.update({line.split()[i+1]:0})
            line_number += 1
            continue    # Jump the first line if it has the inputs declaration
        # Really important!
        # Need to make a new empty element before append
        # Because without it, each time you append, you insert the same object
        e = Element(None, [], None)
        elements_table.append(e)
        for word in line.split():
            # First word of every line is the element type
            if word_counter == 0:
                if flag_top_inputs == 0:
                    elements_table[line_number].type = word
                    word_counter += 1
                else:
                    elements_table[line_number-1].type = word
                    word_counter += 1
            else:
                if word_counter == 1:   # Second word is the output
                    signals_table.update({word:0})  # Add the other signals (not top signals) to the signals table
                    if flag_top_inputs == 0:
                        elements_table[line_number].output = word
                        word_counter += 1
                    else:
                        elements_table[line_number-1].output = word
                        word_counter += 1
                else:   # The rest of the words are inputs
                    if flag_top_inputs == 0:
                        elements_table[line_number].inputs.append(word)
                        word_counter += 1
                    else:
                        elements_table[line_number-1].inputs.append(word)
                        word_counter += 1
        line_number += 1 
        print(signals_table)


def main():
    input_file = open("inputfile.txt","r")
    elementTypes = ['NOT','AND','OR','XOR','NAND','NOR','XNOR']
    elements_table = [] # list of elements
    signals_table = {}
    truth_table =  [[0,0,0,0,1,0],
                    [0,0,1,0,0,0],
                    [0,1,0,0,1,0],
                    [0,1,1,0,0,0],
                    [1,0,0,0,1,0],
                    [1,0,1,0,0,0],
                    [1,1,0,1,1,1],
                    [1,1,1,1,0,0]]
    top_inputs = [] # the inputs of the circuit, incase they're declared in the input file
    
    readfile(input_file, elementTypes, elements_table, top_inputs, signals_table)
    #signalsTable = top_inputs 
    testbench(elements_table, signals_table, truth_table, top_inputs)
    
main()