#program to check given string is palindrome or not:

s=input('enter the string: ')
if s==s[::-1]:
    print('it is palindrome')
else:
    print('its not palindrome')