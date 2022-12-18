#1
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

num_heads=0
for i in result:
    if i=='heads':
        num_heads+=1
    else:
        continue

print(f'No of heads is : {num_heads}')