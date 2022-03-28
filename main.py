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

def graphdata(upperbound=None):
  max_so_far = 0
  mywindow = turtle.Screen()
  grapher = turtle.Turtle()
  writer = turtle.Turtle()
  mywindow.setworldcoordinates(0, 0, 10, 10)
  grapher.up()
  for i in range(1,(upperbound + 1)):
    result = seq3np1(i)
    grapher.goto(i, result)
    grapher.down()
    if (result > max_so_far):
      max_so_far = result
      mywindow.setworldcoordinates(0, 0, (i + 10), (max_so_far + 10))
      writer.clear()
      writer.up()
      writer.goto(0, max_so_far)
      writer.down()
      writer.write("Maximum so far: " + str(i) + ", " + str(max_so_far), False, align="left")
  mywindow.exitonclick()

graphdata(upperbound=12)