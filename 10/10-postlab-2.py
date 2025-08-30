import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]    # x^2
y2 = [1, 8, 27, 64, 125]  # x^3
plt.plot(x, y1, label="x squared", color="blue")
plt.plot(x, y2, label="x cubed", color="red")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Multiple Line Plot")
plt.legend()
plt.show()
