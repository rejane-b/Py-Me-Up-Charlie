import csv

# Declaring variables
list_month = []
list_amount = []
list_change = []

# Read and assign data
with open('Resources/budget_data.csv', newline='') as file:
    reader = csv.reader(file)
    data = list(reader)
    data.pop(0)
    for item in data:
        list_amount.append(int(item[1]))
        list_month.append(item[0])

# Initialize variables
index_increase=0
increase=0
index_decrease=0
decrease=0

# Find the greatest increase and decrese in profits over the entire period
for index in range(len(list_amount)-1):
    value = list_amount[index+1]-list_amount[index]
    if value >= increase:
        increase=value
        index_increase=index+1
    if value <= decrease:
        decrease=value
        index_decrease = index+1
    list_change.append(value)


print("Financial Analysis")
print("----------------------------")
print("Total Months:",len(list_month))
print("Total:",f"${sum(list_amount)}")
print("Average Change:", f"${round(sum(list_change)/len(list_change),2)}")
print("Greatest Increase in Profits:", list_month[index_increase], f"(${increase})")
print("Greatest Decrease in Profits:", list_month[index_decrease], f"(${decrease})")