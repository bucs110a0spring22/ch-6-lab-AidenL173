import turtle

def seq3np1(n):
  count = 0
  while(n != 1):
    count = count + 1
    if(n % 2) == 0:        # n is even
      n = n // 2
    else:                 # n is odd
      n = n * 3 + 1
  return(count)

def main():
  start = int(input("Upper Bound? "))
  if (start <= 0):
    exit()
  for i in range(1,(start + 1)):   
    iterations = seq3np1(i)
    print("N value is", i, "and number of iterations is",  iterations)
main()

def graphData(mywindow=None, myturtle=None, writer=None, upperbound=None):
  if (upperbound <= 0):
    exit()
  mywindow = turtle.Screen()
  myturtle = turtle.Turtle()
  writer = turtle.Turtle()
  mywindow.setworldcoordinates(0, 0, 10, 10)
  max_so_far = 0
  for i in range(1,(upperbound + 1)):   
    result = seq3np1(i)
    if (result > max_so_far):
      max_so_far = result 