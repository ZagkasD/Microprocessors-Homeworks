# Simulation of a circuit

# Gods forgive me for the code I'm about to write


import random
    
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

# Add extra columns in the workload
def increase_workload(N, workload):
    workload += [[random.randint(0,1) for k in range(3)] for i in range(N)]

def calculate_switches(switchesNumber, vectorsNumber, workload, Output):
    for i in range(vectorsNumber):
        # Checking the output of the OR gate for each input from the workload
        newGateOutput = ((workload[i][0] and workload[i][1]) and (not (workload[i][2])))
       
        if (Output == newGateOutput): # No switching
            continue
        else:   # Switching
            Output = newGateOutput
            switchesNumber += 1    
    return switchesNumber

def main():

    workload = [] # Basic workload
    N = 4359 # Number of extra columns for input in the workload
    increase_workload(N, workload)

    vectorsNumber = len(workload) # Number of columns, or different inputs in the OR gate
    Output = ((0 and 0) and (not(0))) # The starting output

    switchesNumber = 0 
    switchesNumber = calculate_switches(switchesNumber, vectorsNumber, workload, Output)

    switchingActivity = switchesNumber/vectorsNumber

    print('switchesNumber =',switchesNumber)
    print('vectorsNumber =',vectorsNumber)
    print('switchingActivity = ',switchingActivity)

    # Switching activity approximation = 0.22 with MC
    # 0.30 with SP

    


main()