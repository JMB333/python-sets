##problem one, set one, paying the minimum
#client inputs:
i1 = input('Enter the outstanding balance on your credit card:')
i1 = float(i1)
i2 = input('Enter the annual credit card interest rate as a decimal:')
i2 = float(i2)
i3 = input('Enter the minimum monthly payment rate as a decimal:')
i3 = float(i3)
# initialize state variables
total = 0
##outputs: the month, minimum monthly payment, principle paid, remaining balance
## translate to code samples:
##mMPayment = i3 * i1, 
####interestPaid = (i2 / 12) * i1
##pPaid = mMPayment - interestPaid
##Balance = i1 - pPaid
##create algorithm to calculate the balance after one year only paying the minimum
x = 1 ## initiate month
for x in range(12):
	print('Month: ', int(x + 1))
	mMPayment = round(i3, 2) * i1
	total += mMPayment	
	print('Minimum monthly payment: ', round(mMPayment, 2))
	interestPaid = (i2 / 12) * i1
	pPaid = mMPayment - interestPaid
	print('Principle paid: ', round(pPaid, 2))
	rBalance = i1 - pPaid
	print('Remaining balance: ', round(rBalance, 2))
	i1 = rBalance
if x == 11:
	print('RESULT')
	print('Total amount paid', round(total, 2)) #ALERT test case one cent higher
	print('Remaining balance:', round(rBalance, 2)) 
x += 1

