import os #os path  
import csv #csv file

csvpath = os.path.join("PyPoll/Resources/election_data.csv")
csvtextpath = os.path.join("Analysis/PyRoll.txt")
#declare variables
WIN_V = 0
V = 0
TOT_can = 0
MAX_V = ["", 0]
CAN_opt = []
CANV= {}

#My header
print("Election Results")

#Finding candidates results
with open(csvpath) as csvfile:
    csvReader = csv.DictReader(csvfile)

    for row in csvReader:
        V = V + 1
        TOT_can = row["Candidate"]        

        if row["Candidate"] not in CAN_opt:
            
            CAN_opt.append(row["Candidate"])

            CANV[row["Candidate"]] = 1
            
        else:
            CANV[row["Candidate"]] = CANV[row["Candidate"]] + 1

    #loop for the WINNER:
    if (V > WIN_V):
        MAX_V[1] = CANV
        MAX_V[0] = row["Candidate"]
    
    #PRINT NAMES
    
    print("-------------------------------------")
    print("Total Votes " + str(V))
    print("-------------------------------------")

#Calculate the winner
    for CANDIDATE in CANV:
        print(CANDIDATE + " " + str(round(((CANV[CANDIDATE]/V)*100))) + "%" + " (" + str(CANV[CANDIDATE]) + ")") 
        CANR = (CANDIDATE + " " + str(round(((CANV[CANDIDATE]/V)*100))) + "%" + " (" + str(CANV[CANDIDATE]) + ")") 
    
CANV

THE_WINNER =sorted(CANV)

print("-------------------------------------")
print("Winner: "+ str(THE_WINNER[1]))
print("-------------------------------------")

with open(csvtextpath, "w") as txt_file:  
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Total Votes " + str(V))
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write(CANDIDATE + " " + str(round(((CANV[CANDIDATE]/V)*100))) + "%" + " (" + str(CANV[CANDIDATE]) + ")") 
    CANR = (CANDIDATE + " " + str(round(((CANV[CANDIDATE]/V)*100))) + "%" + " (" + str(CANV[CANDIDATE]) + ")") 
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: " + str(THE_WINNER[1]))
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")