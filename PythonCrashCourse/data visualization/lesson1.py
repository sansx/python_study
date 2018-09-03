import matplotlib.pyplot as plt


x_value = list(range(1,1001))
y_value = [x**2 for x in x_value]

plt.scatter(x_value,y_value, edgecolors="none", s=20, c=y_value, cmap=plt.cm.Blues)

plt.title("num test",fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("VV", fontsize = 14)

plt.tick_params(axis="both", which="major", labelsize = 14)


plt.axis([0,1100,0,1100000])

plt.show()