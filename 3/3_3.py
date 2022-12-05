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
def testbench(elementsTable, signalsTable, truth_table, top_inputs, inputs_flag):
    print("\n==================Testing=======================\n")

    if inputs_flag == "N":
        print('\nUsing truth table for inputs.\n')
        # Apply inputs from the truth table
        for row in range(len(truth_table)):
            column = 0
            # Give inputs from truth table
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
    else:
        # Important!
        # If the inputs are not in the truth table
        # The simulation will automatically result is success
        # Simulate each element/gate
            for k in range(len(elementsTable)):
                process(elementsTable[k], signalsTable)
            
            print(signalsTable)

            # Check which input was given from the truth table
            for row in range(len(truth_table)):
                # This is every column in truth table from the top inputs
                for p in range(len(top_inputs)):
                    if list(signalsTable.values())[p] != truth_table[row][p]:
                        # Break to the new line of truth table
                        break
                    elif p == len(top_inputs): 
                        # We found the input from the truth table
                        for o in range(len(top_inputs),len(signalsTable)):
                            if list(signalsTable.values())[o] != truth_table[row][o]:
                                print("\nTestbench failed.\n")
                                exit()            
                    else:
                        print("\nTestbench successful.\n")
                        exit()
            # for p in range(len(top_inputs),len(signalsTable)):
            #     #if signalsTable[3] == truth_table[row][3] and signalsTable[4] == truth_table[row][4] and signalsTable[5] == truth_table[row][5]:
            #     if list(signalsTable.values())[p] == truth_table[row][p]:
            #         continue
            #     else:
            #         print("Testbench failed.") 
            #         exit()
            # truth table of model

    print("\nTestbench successful.\n")
    exit()
    
    
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

def insertInputs(signals_table,top_inputs,inputs_flag):
    
    while True:
        try:
            inputs_flag = str(input("Do you want to manually enter inputs? Y/N: "))
            if inputs_flag != 'Y' and inputs_flag != 'N':
                raise ValueError
            break
        except ValueError:
            print("Invalid input.")
        # inputs_flag = str(input("Do you want to manually enter inputs? Y/N: "))
        # if inputs_flag == 'Y' or inputs_flag == 'N':
        #     break
        # print("Invalid input.")


    if inputs_flag == 'Y':
        # for i in range(len(top_inputs),len(signals_table)):
        #     x = input("Give input for signal: ")
        #     #list(signals_table.values())[i] = x
        #     signals_table.values()[i] = x
        #     #list(signalsTable.values())[p]
        # Bad implementation
        # For runs more times than necessary
        for key in signals_table:
            if key in top_inputs:
                while True:
                    try:
                        x = float(input("Input value for signal '"+str(key)+"' in range [0,1]: "))
                        if x < 0 or x > 1:
                            raise ValueError
                        signals_table[key] = x
                        break
                    except ValueError:
                        print("Invalid input.")
    print('\nSignals:')  
    print(signals_table)
    return inputs_flag


def sort_elements(top_inputs, elements_table, elements_table_sorted):
    marked_signals = top_inputs.copy()
    elements_unsorted = elements_table.copy()
    appended_elements = []

    while len(elements_unsorted) != 0:

        for element in elements_unsorted:
            flag = 0
            for input in element.inputs:
                if input in marked_signals:
                    # if flag == 2:
                    if flag == len(element.inputs) - 1:
                        elements_table_sorted.append(element)
                        appended_elements.append(element)
                        # list comprehension
                        elements_unsorted = [element for element in elements_unsorted if element not in elements_table_sorted] 
                    else:
                        flag += 1
                        continue
                else:
                    break

        #Mark the outputs of the sorted elements
        for element in appended_elements:
            marked_signals.append(element.output)
        appended_elements.clear()
    


# TODO implement n input gates

def main():
    input_file = open("inputfile.txt","r")
    elementTypes = ['NOT','AND','OR','XOR','NAND','NOR','XNOR']
    elements_table = [] # list of elements
    elements_table_sorted = []
    signals_table = {}
    inputs_flag = 'N'   # Check for manual input of top inputs
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

    sort_elements(top_inputs, elements_table, elements_table_sorted)

    inputs_flag = insertInputs(signals_table,top_inputs,inputs_flag)

    testbench(elements_table, signals_table, truth_table, top_inputs,inputs_flag)
    
main()