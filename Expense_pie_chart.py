#Chrishen Tissera
#Expense Pie Chart
#CS175L-50


import matplotlib.pyplot as plt 
txt.file = open('expenses.txt', 'r')
sizes = f.read().splitlines()
f.close()
labels = ['gas', 'rent', 'car payment', 'Clothing','misc', 'food']
sizes = x
colors = ['blue', 'red', 'green', 'orange','purple','brown']
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()

