#chrishen Tissera
#Averagefrom input file
txtfile = open("numbers.txt").read()
numbers = txtfile.split()
sum = 0
for N in range(len(numbers)):
    numbers[N] = int(numbers[N])
    sum += numbers[N]
average = sum/len(numbers)
print("Average:",average)
