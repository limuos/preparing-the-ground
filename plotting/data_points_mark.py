import matplotlib.pyplot as plt

main_data = [[45, 23, 13, 4, 5, 66], [33, 23, 4, 23, 5, 56]]
highlight = [[46, 42], [34, 10]]
plt.plot(*main_data)
plt.scatter(*highlight, marker='v', color='r')