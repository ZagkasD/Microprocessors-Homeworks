# Simulation of a circuit

# Gods forgive me for the code I'm about to write


def signalprobs(inputAsp, inputBsp, inputCsp):
    pass
    
# 2-input AND gate truth table
# 0 0:0
# 0 1:0
# 1 0:0
# 1 1:1
def sp2AND(inputAsp, inputBsp):
    #print("AND Gate for input probabilities:",inputAsp,inputBsp)
    s = inputAsp*inputBsp
    #print("Signal Probability =",s)
    Esw = 2*s*(1-s)
    #print('Esw =', Esw)
    #print("==========================================")
    return Esw

# NOT gate truth table
# 0:1
# 1:0
def NOT(inputCsp):
    # print("NOT Gate for input probabilities:",inputCsp)
    s = 1-inputCsp
    # print("Signal Probability =",s)
    Esw = 2*s*(1-s)
    # print('Esw =', Esw)
    # print("==========================================")
    return Esw

def main():
    # Truth table of the circuit
    # a b c|e|f D
    # 0 0 0|0|1:0
    # 0 0 1|0|0:0
    # 0 1 0|0|1:0
    # 0 1 1|0|0:0
    # 1 0 0|0|1:0
    # 1 0 1|0|0:0
    # 1 1 0|1|1:1
    # 1 1 1|1|0:0
    a=0.5
    b=0.5
    c=0.5
    print('Pina = ',a,'\nPinb = ',b,'\nPinc = ',c)
    #circuit = sp2AND(sp2AND(a,b),NOT(c))
    #print('Circuit output: ',circuit)
    
    # 2.2 Switching activity for every output (e,f included) using signal probabilities
    
    print('Esw(a,b) = ',sp2AND(a,b))
    print('Esw(c) = ',NOT(c))
    print('Esw(e,f) = ',sp2AND(sp2AND(a,b),NOT(c)))



    
    


main()