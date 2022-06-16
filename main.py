my_text = 'some text'
my_number = 5
my_float = 3.2
my_bol = False
# True
# My comment
"""
another 
comment
"""

my_num = 2
if my_num == 1:  # ha
    print('my number 2')
elif my_num == 3:  # azonban ha
    print('my number 3')
else:  ## barmikor maskor
    print('another number')

print('end')
print('helo')

# user_input = input("adj meg egy számot:")
# print(type(user_input))
# print(user_input)

user_input = int(input("adj meg egy számot:"))
print(user_input)
print(type(user_input))

flag = True
counter = 0
while flag:
    print('1')
    counter += 1
    if counter == 5:
        flag = False
