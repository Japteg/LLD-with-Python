import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from cache.factories.cache_factory import CacheFactory


#################################
# **** Hardcoded Driver *****
#################################
'''
cache = CacheFactory.default_cache(capacity=5)
cache.put('1', 'ABC')
cache.put('2', 'XYZ')
cache.put('3', 'PQR')
cache.put('4', 'MNO')
cache.put('5', 'IJK')
cache.put('6', 'EFG')
cache.get('2')
cache.get('6')
cache.get('7')
cache.get('1')
'''

###################################
# **** Command Line Driver *****
###################################

print('*******Welcome********')
cache_capacity = int(input('Please enter size of cache you would like to initialize: '))
cache = CacheFactory.default_cache(cache_capacity)
print(f'\nCache of capacity {cache_capacity} created!')

print("#####################")
print("Instructions:")
print("Enter command: `put <key> <value>` to add an item in cache")
print("Enter command: `get <key>` to element from cache")
print("Enter command: `exit` to quit application")
print("#####################")

while True:
    command = input()
    command = command.lower().split(' ')
    action = command[0]
    if action == 'put':
        key = command[1]
        value = command[2]
        cache.put(key, value)
    elif action == 'get':
        key = command[1]
        cache.get(key)
    elif action == 'exit':
        break
    else:
        print('Please enter a valid command')

'''
###sample input for command line driver###
5
put 1 Jhon
put 2 Abhi
put 3 Priya
put 4 Mihika
get 2
put 5 Raghav
get 1
get 4
put 6 Abhinav
put 7 Jatin
exit
'''
