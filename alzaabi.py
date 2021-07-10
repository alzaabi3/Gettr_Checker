import requests

# ADD 'list.txt' !
# ADD 'Available.txt' !

k = open('list.txt', 'r').read().splitlines()

print('''
  ____        _    _
 / ___|  ___ | |_ | |_  _ __
| |  _  / _ \| __|| __|| '__|
| |_| ||  __/| |_ | |_ | |
 \____| \___| \__| \__||_|
                [+] By: @6ah .
                ''')
start = input('[ ? ] Start Checking [Y/N]: ')

if start == 'Y' or 'y':
    for user in k:
            attempts = 0
            available = 0
            used = 0
            error = 0
            for user in k:
                url = f'https://api.gettr.com/s/uinf/{user}'
                headers = {
                    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
                }
                r = requests.get(url, headers=headers)
                if r.status_code == 400:
                    attempts += 1
                    available += 1
                    with open('Available.txt', 'a') as x:
                        x.write(user + '\n')
                    print(f'\r[ + ] Attempts: {attempts} , [ + ] Available: {available} , [ x ] Used: {used} , [ x ] Error: {error}', end='')
                elif r.status_code == 200: 
                    attempts += 1 
                    used += 1 
                    print(f'\r[ + ] Attempts: {attempts} , [ + ] Available: {available} , [ x ] Used: {used} , [ x ] Error: {error}', end='')
                else: 
                    attempts += 1 
                    error += 1 
                    print(f'\r[ + ] Attempts: {attempts} , [ + ] Available: {available} , [ x ] Used: {used} , [ x ] Error: {error}', end='')
            print('Finished Checking!')
            input('Enter Any Key To Exit: ')

if start == 'N' or 'n':
    print('Ok Bye :(')
    input('Enter Any Key To Exit: ')

else:
    print('Please Enter Y or N !!')
    input('Enter Any Key To Exit: ')