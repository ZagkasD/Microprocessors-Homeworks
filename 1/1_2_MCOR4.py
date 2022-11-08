# Monte Carlo algorithm for calculating Esw (switching activity) of a 4 input OR gate
#
# Gods forgive me for the code I'm about to write

import random

# Add extra columns in the workload
def increase_workload(N, workload):
    workload += [[random.randint(0,1) for k in range(4)] for i in range(N)]

def calculate_switches(switchesNumber, vectorsNumber, workload, gateOutput):
    for i in range(vectorsNumber):
        # Checking the output of the OR gate for each input from the workload
        newGateOutput = workload[i][0] or workload[i][1] or workload[i][2] or workload[i][3]
       
        if (gateOutput == newGateOutput): # No switching
            continue
        else:   # Switching
            gateOutput = newGateOutput
            switchesNumber += 1    
    return switchesNumber
            

def main():
    workload = [[0,0,0,0],[1,1,1,1],[0,0,0,1],[0,1,0,1]] # Basic workload
    N = 4359 # Number of extra columns for input in the workload
    increase_workload(N, workload)
    
    vectorsNumber = len(workload) # Number of columns, or different inputs in the OR gate
    gateInputsNumber = len(workload[0]) # Number of rows, the size of the OR gate (inputs)
    gateOutput = 0 or 0 or 0 or 0 # The starting output of the OR gate for the first input from the workload

    switchesNumber = 0 
    switchesNumber = calculate_switches(switchesNumber, vectorsNumber, workload, gateOutput)
    
    switchingActivity = switchesNumber/vectorsNumber

    print('switchesNumber ='+str(switchesNumber))
    print('vectorsNumber ='+str(vectorsNumber))
    print('switchingActivity = '+str(switchingActivity))
      
    
main()