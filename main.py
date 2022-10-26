from art import logo, vs
from game_data import data
import random


check = False
given_data = data
length = len(given_data)
result = ""
flag = 0


def compareA(given_list, side, flag):
  
  if side == 'a':
    print(f"Compare A: {given_list['name']}, {given_list['description']}, from {given_list['country']}")
  if side == 'b':
    print(f"Compare B: {given_list['name']}, {given_list['description']}, from {given_list['country']}")

def calculator(a,b,user_input):
  global result
  check = 0
  if a['follower_count'] > b['follower_count']:
    result = "a"
  if a['follower_count'] < b['follower_count']:
    result = "b"

  if result == user_input.lower():
    check += 1
    return check
  else:
    check = 0
    return check
    
while not check:
  print(logo)

  aValue = random.randint(0, length - 1)

  if flag > 0:
    print(f"your score is {flag}")
  
  compareA(given_data[aValue],'a',flag)

  print(vs)

  bValue = random.randint(0, length - 1)
  compareA(given_data[bValue],'b',flag)

  user_input = input("Who has more followers? Type 'A' or 'B' : ")

  flag += calculator(given_data[aValue], given_data[bValue], user_input)

  if flag == 0:
    print("wrong")
    check = True
    
  
