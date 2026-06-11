
import matplotlib.pyplot as plt

x_values = range(1, 6)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)
ax.set_title("First 5 Cubic Numbers")
ax.set_xlabel("n")
ax.set_ylabel("n³")

plt.show()


x_large = list(range(1, 5001))
y_large = [y**3 for y in x_large]

plt.style.use('seaborn-v0_8')
fix, ax = plt.subplots()
# Added colormap to this one
ax.scatter(x_large, y_large, c=y_large, cmap=plt.cm.Blues, s=10)
ax.set_title("First 5000 Cubic Numbers")
ax.set_xlabel("n")
ax.set_ylabel("n³")

plt.show()








