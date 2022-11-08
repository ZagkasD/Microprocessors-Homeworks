# Functions for calculating signal probabilities of gates
# 
# Gods forgive me for the code I'm about to write

def signalprobs(input1sp, input2sp, input3sp):
    # Already implemented SP for these gates
    sp2AND(input1sp, input2sp)
    sp2OR(input1sp, input2sp)

    # First Part
    sp2XOR(input1sp, input2sp)
    sp2NAND(input1sp, input2sp)
    sp2NOR(input1sp, input2sp)

    # Second Part
    sp3AND(input1sp, input2sp, input3sp)
    sp3OR(input1sp, input2sp, input3sp)
    sp3XOR(input1sp, input2sp, input3sp)
    sp3NAND(input1sp, input2sp, input3sp)
    sp3NOR(input1sp, input2sp, input3sp)


# ==============================================================================
#                                First part
# ==============================================================================


# 2-input AND gate truth table
# 0 0:0
# 0 1:0
# 1 0:0
# 1 1:1
def sp2AND(input1sp, input2sp):
    print("AND Gate for input probabilities:",input1sp,input2sp)
    s = input1sp*input2sp
    print("Signal Probability =",s)
    Esw = 2*s*(1-s)
    print('Esw =', Esw)
    print("==========================================")

# 2-input OR gate truth table
# 0 0:0
# 0 1:1
# 1 0:1
# 1 1:1
def sp2OR(input1sp, input2sp):
    print("OR Gate for input probabilities:",input1sp,input2sp)
    s = 1-(1-input1sp)*(1-input2sp)
    print("Signal Probability =",s)
    Esw = 2*s*(1-s)
    print('Esw =', Esw)
    print("==========================================")

# 2-input XOR gate truth table
# 0 0:0
# 0 1:1
# 1 0:1
# 1 1:0
def sp2XOR(input1sp, input2sp):
    print("XOR Gate for input probabilities:",input1sp,input2sp)
    s = (1-input1sp)*input2sp+input1sp*(1-input2sp)
    print("Signal Probability =",s)
    Esw = 2*s*(1-s)
    print('Esw =', Esw)
    print("==========================================")

# 2-input NAND gate truth table
# 0 0:1
# 0 1:1
# 1 0:1
# 1 1:0

# Or the NAND gate is complementary to the AND gate, so is the SP.
def sp2NAND(input1sp, input2sp):
    print("NAND Gate for input probabilities:",input1sp,input2sp)
    s = 1-(input1sp*input2sp)
    print("Signal Probability =",s)
    Esw = 2*s*(1-s)
    print('Esw =', Esw)
    print("==========================================")

# 2-input NOR gate truth table
# 0 0:1
# 0 1:0
# 1 0:0
# 1 1:0

# Or the NOR gate is complementary to the OR gate, so is the SP.
def sp2NOR(input1sp, input2sp):
    print("NOR Gate for input probabilities:",input1sp,input2sp)
    s = 1-(1-(1-input1sp)*(1-input2sp))
    print("Signal Probability =",s)
    Esw = 2*s*(1-s)
    print('Esw =', Esw)    
    print("==========================================")
    

# ==============================================================================
#                                Second part
# ==============================================================================


# 3-input AND gate truth table
# 0 0 0:0
# 0 0 1:0
# 0 1 0:0
# 0 1 1:0
# 1 0 0:0
# 1 0 0:0
# 1 1 0:0
# 1 1 1:1
def sp3AND(input1sp, input2sp, input3sp):
    print("AND Gate for input probabilities:",input1sp,input2sp,input3sp)
    s = input1sp*input2sp*input3sp
    print("Signal Probability =",s)
    Esw = 2*s*(1-s)
    print('Esw =', Esw)
    print("==========================================")

# 3-input OR gate truth table
# 0 0 0:0
# 0 0 1:1
# 0 1 0:1
# 0 1 1:1
# 1 0 0:1
# 1 0 0:1
# 1 1 0:1
# 1 1 1:1
def sp3OR(input1sp, input2sp,input3sp):
    print("OR Gate for input probabilities:",input1sp,input2sp,input3sp)
    s = check=7/8
    print("Signal Probability =",s)
    Esw = 2*s*(1-s)
    print('Esw =', Esw)
    print("==========================================")

# 3-input XOR gate truth table
# 0 0 0:0
# 0 0 1:1
# 0 1 0:1
# 0 1 1:1
# 1 0 0:1
# 1 0 0:1
# 1 1 0:1
# 1 1 1:0
def sp3XOR(input1sp, input2sp,input3sp):
    print("XOR Gate for input probabilities:",input1sp,input2sp,input3sp)
    s = check=6/8
    print("Signal Probability =",s)
    Esw = 2*s*(1-s)
    print('Esw =', Esw)
    print("==========================================")

# 3-input NAND gate truth table
# 0 0 0:1
# 0 0 1:1
# 0 1 0:1
# 0 1 1:1
# 1 0 0:1
# 1 0 0:1
# 1 1 0:1
# 1 1 1:0
def sp3NAND(input1sp, input2sp, input3sp):
    print("AND Gate for input probabilities:",input1sp,input2sp,input3sp)
    s = 1-(input1sp*input2sp*input3sp)
    print("Signal Probability =",s)
    Esw = 2*s*(1-s)
    print('Esw =', Esw)
    print("==========================================")

# 3-input NOR gate truth table
# 0 0 0:1
# 0 0 1:0
# 0 1 0:0
# 0 1 1:0
# 1 0 0:0
# 1 0 0:0
# 1 1 0:0
# 1 1 1:0
def sp3NOR(input1sp, input2sp,input3sp):
    print("OR Gate for input probabilities:",input1sp,input2sp,input3sp)
    s = 1-(7/8)
    print("Signal Probability =",s)
    Esw = 2*s*(1-s)
    print('Esw =', Esw)
    print("==========================================")


# ==============================================================================
#                                Third part
# ==============================================================================


# TODO gates with N inputs


def main():
    signalprobs(0.5, 0.5, 0.5)
    #signalprobs(0, 0, 0)
    #signalprobs(1, 1, 1)





main()