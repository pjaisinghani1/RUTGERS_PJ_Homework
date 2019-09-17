import os 
import csv

print("Hello World")
csvpath = os.path.join('Resources', 'budget_data.csv')

# Read in the CSV file
with open(csvpath, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    budgetdate=list(csvreader)
    #print(budgetdate)
    #print(len(budgetdate))

    print(max(budgetdate[1])



    #for row in csvreader:
     #   print(row)

    #def net_total():
     #   date = str(csvfile[0])
      #  profit_loss = int(csvfile[1])
       # return net_total = ['profit_loss'].sum()

    
        #average_change = ['profit_loss'].average()
        #print(f"Total Months: {int(total_months)}")
        #print(f"Net_Total: {float(net_total)}")
        #print(f"Average Change: {float(average_change)}")


    
 # * The total number of months included in the dataset

  #* The net total amount of "Profit/Losses" over the entire period

  #* The average of the changes in "Profit/Losses" over the entire period

 # * The greatest increase in profits (date and amount) over the entire period

  #* The greatest decrease in losses (date and amount) over the entire period
