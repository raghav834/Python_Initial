#3
expense_list = [2340, 2500, 2100, 3100, 2980]
month=['january','febraury','march','april','may']

expense = int(input("Enter the expense in rupees : "))

if  expense in expense_list:
   index= expense_list.index(expense)
   print('This is the expense of '+month[index])
else:
    print(f"{expense} is not the expense of any month")