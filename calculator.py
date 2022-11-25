from art import logo

def add(a,b):
  return a+b
def subtract(a,b):
  return a-b
def multiply(a,b):
  return a*b
def division(a,b):
  return a/b


dictionary={
  '+':add,
  '-':subtract,
  '*':multiply,
  '/':division,
}

print(logo)
def calculator():
  first_num=float(input('enter the first number '))
  print('\n')
  for opp in dictionary:
    print(opp)

  n=True
  while(n):
    choice= input('\nenter any opperation ')
    second_num=float(input('\nenter the next number '))

    for opp in dictionary:
      if(choice==opp):
        output=dictionary[opp](first_num,second_num)

    print(f'{first_num} {choice} {second_num} = {output}')
    
    next=input(f'\nenter y to continue with {output} or enter n to  exit the calculation ').lower()
    
    if next=='y':
      first_num=output
    else :
      n=False
      print(f'\nthe result = {output}\n\n')
      calculator()



calculator()
