import csv

list_month = []
list_amount = []
list_change = []

with open('Resources/budget_data.csv', newline= '') as file:
  reader = csv.reader(file)
  data = list(reader)
  data.pop(0)
  for item in data:
    list_amount.append(int(item[1]))
    list_month.append(item[0])

index_increase=0
increase=0
index_decrease=0
decrease=0
for index in range(len(list_amount)-1):
  value = list_amount[index+1]-list_amount[index]
  if value >= increase:
    increase=value
    index_increase=index
  if value <= decrease:
    decrease=value
    index_decrease = index
  list_change.append(value)

list_test = list_amount[0:43]

print(sum(list_test))

print ("Financial Analysis")
print("----------------------------")
print("Total Months:", len(list_month))
print("Total:", sum(list_amount))
print("Average Change:", round(sum(list_change)/len(list_change),2))
print("Greatest Increase in Profits:", list_month[index_increase], f"(${increase})")
print("Greatest Decrease in Profits:", list_month[index_decrease], f"(${decrease})")
