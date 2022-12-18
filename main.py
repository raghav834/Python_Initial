#exercise 2[sugar level detector]
sugar_level=int(input('Enter Your sugar level : '))

if sugar_level >= 80 and sugar_level <= 100:
    print('Your Sugar is normal')
elif sugar_level<80:
    print('Your Sugar is low')
else:
    print('Your Sugar is high')

