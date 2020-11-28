import time

# starting time
start = time.time()

def fibonacci2(n):
	fibNumbers = [0,1]  #list of first two Fibonacci numbers
	# now append the sum of the two previous numbers to the list    
	for i in range(2, n+1):
  		fibNumbers.append(fibNumbers[i-1] + fibNumbers[i-2])
 	return fibNumbers[n]  

def fibonacci(n):
    if n == 0:
    return 0
    if n == 1:
    return 1    
    return fibonacci(n-1) + fibonacci(n-2)

fibonacci(10)

end = time.time()
print (end-start)
