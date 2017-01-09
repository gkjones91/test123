name=input('What is your name?')
print('Hello, '+name+"!")
month=input('What is your birth month? ')
day = input('What day were you born on? ')
year = input('What year were you born in? ')
correct_date=input(name+", You were born on "+day+" "+month+" "+year+", correct? (Y/N)")
if correct_date == 'y' or 'Y':
    print('Great!')
elif correct_date == 'n' or 'N':
    print("Oh crap")

print(correct_date)    
            
