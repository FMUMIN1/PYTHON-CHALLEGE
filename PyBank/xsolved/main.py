import os #file path
import csv #csv path

print("Financial Analysis")
print("-------------------------------")
csvpath = os.path.join("PyBank/Resources/budget_data.csv")
csvtextpath = os.path.join("Analysis/PyBank.txt")

#declare variables
TOT_months = 0
TOT_P_loss = 0
LAST_P_loss = 0
PROF_L_change = 0
MAX_inc = ["",0]
MAX_dec = ["",999999999999]
PROF_L_changes = []
with open(csvpath) as csvfile:
    csvReader = csv.DictReader(csvfile)

#total months
    for row in csvReader:
        TOT_months = TOT_months + 1
        TOT_P_loss = TOT_P_loss + int(row["Profit/Losses"])
        print(row)

#Finging total changes
        PROF_L_change = int(row['Profit/Losses']) - LAST_P_loss
        print(PROF_L_change)

        LAST_P_loss =int(row['Profit/Losses'])
        print(LAST_P_loss)

#Max & Min
        if (PROF_L_change > MAX_inc[1]):
            MAX_inc[1]=PROF_L_change
            MAX_inc[0]=row['Date']

        if(PROF_L_change < MAX_dec[1]):
            MAX_dec[1] = PROF_L_change
            MAX_dec[0] = row['Date']
        
#Add to the profit_loss_changes list
PROF_L_changes.append(int(row['Profit/Losses']))

#Finding the average
avg_PRO_loss = sum(PROF_L_changes)/len(PROF_L_changes)

#printed 
print("Total Months: " + str(TOT_months))
print("Total: " + "$" + str(TOT_P_loss))
print("Average Change: "+  str(round(avg_PRO_loss, 2))+'%')
print("Greatest Increase: " + str(MAX_inc[0]) + " ($" +  str(MAX_inc[1]) + ")")
print("Greatest Decrease: " + str(MAX_dec[0]) + " ($" + str(MAX_dec[1]) + ")")

#text file
with open(csvtextpath, "w") as txt_file:  
    txt_file.write("Financial Analysis")
    txt_file.write("\n")
    txt_file.write("-------------------------------")
    txt_file.write("\n")
    txt_file.write("Total Months: " + str(TOT_months))
    txt_file.write("\n")
    txt_file.write("Total: " + "$" + str(TOT_P_loss))
    txt_file.write("\n")
    txt_file.write("Average Change: "+  str(round(avg_PRO_loss, 2))+'%')
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(MAX_inc[0]) + " ($" +  str(MAX_inc[1]) + ")")
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(MAX_dec[0]) + " ($" + str(MAX_dec[1]) + ")")