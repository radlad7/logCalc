# Another way of explaining log2 8 is:
# if we kept dividing 8 by 2 until we ended up with 1,
# how many 2s would we have in our equation?

def logCount(base, number):
	result = number // base
	count = 0

	print("\n\nlog of {} to base {}".format(number, base)
			+ "\n*************************"
			+ "\n{}/{} = {}".format(number, base, result))
	count +=1

	while result != 1:
		resultTemp = result
		result = result // base
		print("{}/{} = {}".format(resultTemp, base, result))
		count +=1
		
		if result <= 1:
			print("\n     Final Result: \n\nlog base ({}) of {} = \n\n\t>> {} <<".format(base, number, count)
			+ "\n*************************")
			break

			
# Base 2 Table for Pre-Filled Example - WIP
def baseTwoExample():
	i = 2
	result = 0
	while result <= 2048:
		result = i * 2
		i = i * 2
		logCount(2, result)

		
# Log Calc Prompt
print("\n********************\nWelcome to Ray's Log Calc.\n\nThis tool can help calculate common (base 10) and binary (base 2) logarithms.\n\nCurrently fractions, negative numbers and bases outside of 2 and 10 are not supported.\n********************\n")

choice = int(input("You may choose from:\n(1) an example of logarithms calculated in base 2\nor\n(2) a prompt to enter your own base and log numbers for calculation."))
if choice == 1:
	baseTwoExample()
elif choice == 2:
	baseNum = int(input("Please enter a base number: "))
	logOfNum = int(input("Now enter the desired logarithm of x to base {}: ".format(baseNum)))
	logCount(baseNum, logOfNum)
else:
	print("Please select a valid choice: 1 or 2.")
	choice

# Testing Log Calc in Base 2, 10 and 5.
'''
logCount(2,8)
logCount(2, 16)
logCount(2, 32)
logCount(2, 64)
logCount(2, 128)
logCount(2, 256)
logCount(2, 512)
logCount(2, 1024)
logCount(2, 2048)

logCount(10, 100)
logCount(2, 24)
logCount(5, 625)
'''