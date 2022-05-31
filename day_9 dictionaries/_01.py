from replit import clear

loop = True
dict_name = {}

while loop:
    name = input('What is your name?')
    bid = input('What is your bid?')
    dict_name[name] = int(bid)
    Last_q = input('Are there any others bidders? Type y or n\n')
    if Last_q == 'y':
        clear()
    else:
        max_val = max(dict_name.values())
        name_max_val = max(dict_name, key=dict_name.get)
        print(f'The winner are {name_max_val} with bid of {max_val}')
        loop = False
