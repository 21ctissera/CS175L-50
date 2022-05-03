#Chrishen Tissera
#Program: Stocks

commrate = float(input('what was the commision rate? '))
shares = int(input('How many shares did you purchase? '))
purchase = float(input('what was the purchase price? '))
selling = float(input('what was the selling price? '))
#inputs

amount = purchase*shares
commpaidpre = amount*commrate
sold = selling*shares
commpaidpost = sold*commrate
totalcomm = commpaidpre + commpaidpost
profit = sold-amount-totalcomm
#calculate

print(f'Amount paid for stock: ${amount:.1f}')
print(f'Commision paid on tyhe purchase: ${commpaidpre:.1f}')
print(f'Amount the stock sold for: ${sold:.1f}')
print(f'Commision paid on the sale: ${commpaidpost:.1f}')
print(f'Total commision paid: ${totalcomm:.1f}')
print(f'Profit (positive or negative): ${profit:.1f}')
#statements
