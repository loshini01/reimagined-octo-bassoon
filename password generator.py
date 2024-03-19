'''
      PASSWORD GENERATOR
'''
import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_characters = "@#$%&_*?+-^!"

combination = lowercase + uppercase + numbers + special_characters
Password_length = int(input("Enter the length of the Password : "))
Password = "".join(random.sample(combination, Password_length))
print("The Generated Password is :", Password)
