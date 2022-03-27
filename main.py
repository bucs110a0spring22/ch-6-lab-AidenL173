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