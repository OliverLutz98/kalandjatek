my_text = 'some text'

my_num= 2
if my_num == 1:
    print('My num is 1')
elif my_num == 3:
    print('my num is 3')
else:
    print('another number')

print('end')

# user_input = input('adj meg valami adatot: ')
# print(user_input)

# user_input = input('number: ')
# num_user_input = int(user_input)
# print(type(num_user_input))

flag = True
counter = 0
while flag:
    print(counter)
    counter += 1
    if counter == 5:
        flag = False