import matplotlib.pyplot as plt

# First 5 cubes
x_small = list(range(1, 6))
y_small = [n**3 for n in x_small]

plt.figure()
plt.scatter(x_small, y_small)
plt.title("First 5 Cubic Numbers")
plt.xlabel("n")
plt.ylabel("n^3")
plt.show()

# First 5000 cubes
x_large = list(range(1, 5001))
y_large = [n**3 for n in x_large]

plt.figure()
plt.scatter(x_large, y_large, s=1)
plt.title("First 5000 Cubic Numbers")
plt.xlabel("n")
plt.ylabel("n^3")
plt.show()



# I have done something wrong since its not working.
# Look over why matplotlib isnt working. fix it and then run program! 