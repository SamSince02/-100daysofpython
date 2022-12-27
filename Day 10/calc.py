from art import logo
#Add
def add(n1,n2):
  return n1 + n2

#Subtract
def sub(n1,n2):
  return n1 - n2

#Multiply
def mul(n1,n2):
  return n1*n2

#Division 
def div(n1,n2):
  return n1/n2

Operations = {"+": add,
              "-": sub,
              "*": mul,
              "/": div
}
def calculator():
  print(logo)


  num1 =float(input("Enter the number 1 : "))
  
  for operator in Operations:
    print(operator)
  
  
  should_continue = True
  while should_continue:
    op = input("Pick any of the operator mentioned above :")
    num2 = float(input("Enter the number 2 : "))
    calculation_function = Operations[op]
    answer = calculation_function(num1,num2)
  
    print(f"{num1} {op} {num2} = {answer}")
  
    if input("Type 'y' if you wanna continue or 'n' to start from beginning")=="y":
      num1 = answer
    else:
      should_continue=False
      calculator()

calculator()