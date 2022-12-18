#ex 1 part b
india=['mumbai','banglore','chennai','delhi']
pakistan=['lahore','karachi','islamabad']
bangladesh=['dhaka','khulna','rangpur']

city1=input('Enter Name of city1 : ')
city2=input('Enter name of city2 : ')


if city1 in india and city2 in india:
    print(f'{city1} and {city2} are in india' )
elif city1 in india and city2 in pakistan:
    print(f'{city1} and {city2} are in pakistan' )
elif city1 in india and city2 in bangladesh:
    print(f'{city1} and {city2} are in bangladesh')
else:
    print(f'{city1} and {city2} are either not in same country or one or both of them are not in any country')