from operations import *

while True:
    user_input = input('>>> ')
    if user_input == 'quit' or user_input == 'exit':
        break
    print(reply(user_input))
