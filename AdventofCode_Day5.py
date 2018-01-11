##import hashlib
##import random
##index = 0
##password = 'abc'
##while 1:
##    m = hashlib.md5()
##    m.update(('ugkcyxxp'+str(index)).encode('utf-8'))
##    hex_m = m.hexdigest()
##    if hex_m[0:5] == '00000':
##        password_pos = int(hex_m[5], 16)
##        if password_pos < 8:
##            password_dig = int(hex_m[6], 16)
##            if password[password_pos] == '_':
##                password = password[:password_pos] + hex(password_dig)[-1] + password[password_pos + 1:]
##                print(password)
##    if index % 30000 == 0:
##        for char in password:
##            if char == '_':
##                print(str(random.random())[-1], end='')
##            else:
##                print(char, end='')
##        print('\r', end='')
##    index += 1

from __future__ import print_function 
import hashlib 
 
 
import os 
 
 
def solve(data): 
    secret_key = data 
    starts_with = '00000' 
    start = 0 
    password1 = '' 
    password2 = [None] * 8 
    print('secret', secret_key) 
    digest = hashlib.md5() 
    digest.update(secret_key.encode('utf8')) 
    while True: 
        m = digest.copy() 
        m.update(str(start).encode('utf8')) 
        if m.hexdigest().startswith(starts_with): 
            #print('found hex', m.hexdigest()) 
 
 
            # Part 1 
            if len(password1) < 8: 
                password1 += m.hexdigest()[5] 
                print('password1', password1, len(password1)) 
## 
 
            # Part 2 
            index = int(m.hexdigest()[5], 16) 
            value = m.hexdigest()[6] 
            print('idx', index, 'val', value) 
            if index < 8 and password2[index] is None: 
                password2[index] = value 
                print('password2', password2) 

 
            if len(password2) >= 9:
                return password1

 
        start += 1 

 
    print('total hashes', start) 
    return password1, ''.join(password2) 

data = 'cxdnnyjw'
solve(data)
 
##if __name__ == '__main__': 
##    this_dir = os.path.dirname(__file__) 
##    with open(os.path.join(this_dir, 'day5.input')) as f: 
##        data = f.read().strip() 
##
## 
##    password1, password2 = solve(data) 
##    print('The first password is', password1) 
##    print('The second password is', password2) 
##
