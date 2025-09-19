import matplotlib.pyplot as plt
languages = ['Python', 'Java', 'C++', 'JavaScript', 'C#']
popularity = [85, 80, 70, 75, 65]
plt.bar(languages, popularity, color=['blue', 'red', 'green', 'orange', 'purple'])
plt.xlabel("Programming Languages")
plt.ylabel("Popularity (%)")
plt.title("Popularity of Programming Languages")
plt.show()
