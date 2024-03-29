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

# This is the simulation of the circuit
def process(Element, signalsTable):
    if (Element.type == 'AND'):
        #signalsTable[Element.output] = signalsTable[Element.inputs[0]] and signalsTable[Element.inputs[1]]
        signalsTable[Element.output] = sp2AND(signalsTable[Element.inputs[0]],signalsTable[Element.inputs[1]])

    elif (Element.type == 'NOT'):
        #signalsTable[Element.output] = 1 - signalsTable[Element.inputs]
        signalsTable[Element.output] = NOT(signalsTable[Element.inputs])

def testbench(elementsTable, signalsTable, truth_table):
    # Apply truth table and check for mistakes
    print(" a  b  c  e  f  d")
    # Apply inputs from the truth table
    for i in range(len(truth_table)):
        signalsTable[0] = truth_table[i][0]
        signalsTable[1] = truth_table[i][1]
        signalsTable[2] = truth_table[i][2]
        # Simulate each element/gate
        for k in range(len(elementsTable)):
            process(elementsTable[k], signalsTable)
        
        print(signalsTable)
        # Check if the simulation was correct
        if signalsTable[3] == truth_table[i][3] and signalsTable[4] == truth_table[i][4] and signalsTable[5] == truth_table[i][5]:
            continue
        else:
            print("Testbench failed.") 
            exit(1)
    print("\nTestbench successful")

def main():
    elementTypes = ['NOT','AND','OR','XOR','NAND','NOR','XNOR']
    signalsTable = [0,0,0,0,0,0] # starting values for all signals
    # First three values in signals table are the inputs
    
    
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
    
    truth_table =   [[0,0,0,0,1,0],
                    [0,0,1,0,0,0],
                    [0,1,0,0,1,0],
                    [0,1,1,0,0,0],
                    [1,0,0,0,1,0],
                    [1,0,1,0,0,0],
                    [1,1,0,1,1,1],
                    [1,1,1,1,0,0]]

    E1 = Element('AND', [0,1], 3)
    E2 = Element('NOT', 2, 4)
    E3 = Element('AND', [3,4], 5)

    elementsTable = [E1,E2,E3] # elements in model, sorted
    testbench(elementsTable,signalsTable,truth_table)



main()
