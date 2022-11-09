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
    return s
    #print("Signal Probability =",s)
    #Esw = 2*s*(1-s)
    #print('Esw =', Esw)
    #print("==========================================")

# NOT gate truth table
# 0:1
# 1:0
def NOT(inputCsp):
    # print("NOT Gate for input probabilities:",inputCsp)
    s = 1-inputCsp
    return s
    # print("Signal Probability =",s)
    # Esw = 2*s*(1-s)
    # print('Esw =', Esw)
    # print("==========================================")

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

    a=1
    b=1
    c=1
    print('a = ',a,'\nb = ',b,'\nc = ',c)
    # Simulation of the circuit with gates
    circuit = sp2AND(sp2AND(a,b),NOT(c))
    print('Circuit output: ',circuit)

    pass

main()