#Dependencies
import os 
import csv
import numpy

#Join CSV Path 
csvpath = os.path.join('Resources', 'budget_data.csv')
     
#Store Data in A List 
months_years =[]
profit_loss =[]
     
# Read in the CSV file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

#Loop through rows in CSV and store data into list    
    for row in csvreader: 
        months_years.append(row[0])
        profit_loss.append(int(row[1]))
        total_months = len(months_years)
        

        net_total=int()
        for i in range(0,len(profit_loss)):
            profit_loss[i] = int(profit_loss[i])
            net_total += profit_loss[i]
        
        average_change = (net_total)/(total_months) 

        max_increase = max(profit_loss)
        min_decrease = min(profit_loss)

        
    print("  Financial Analysis\n---------------------------- ")
# * The total number of months included in the dataset   
    print(f"Total Months: {str(total_months)}")
#* The net total amount of "Profit/Losses" over the entire period
    print(f"Net_Total:${float(net_total)}") 
#* The average of the changes in "Profit/Losses" over the entire period
    print (f"Average  Change: $"+ str(average_change))
# * The greatest increase in profits (date and amount) over the entire period
    print("Greatest Increase in Profits: " + str(max_increase) )
 #* The greatest decrease in losses (date and amount) over the entire period
    print("Greatest Decrease in Profits: " + str(min_decrease))

# Specify the file to write to
#text_path = os.path.join('Resources', 'budget_data.txt')
#with open(text_path, "w") as text_file:
 #   text_file.write(
  #      f"Financial Analysis: \n"
   #     f"----------------------------\n"
    #     f"Total Months: {str(total_months)}\n"
     #           f"Net_Total:${float(net_total)}\n"
      #          f"Average  Change: $ + {str(average_change)}\n"
       #         f"Greatest Increase in Revenue: {str{max_increase}}\n"
        #        f"Greatest Decrease in Revenue: {str{min_increase}} \n"
  #)