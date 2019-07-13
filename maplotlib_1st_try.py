import matplotlib.pyplot as plt

if __name__ == "__main__":
	x_values = range(1, 1001)
	y_values = [x**2 for x in x_values]

	plt.style.use('seaborn')
	fig, ax = plt.subplots()
	# ax.plot(input_values, squares, linewidth = 3)
	ax.scatter(x_values, y_values, s=1, c=y_values, cmap=plt.cm.tab20b)

	# Set chart title and label axes.
	ax.set_title("Square Numbers", fontsize=24)
	ax.set_xlabel("Value", fontsize=14)
	ax.set_ylabel("Square of Value", fontsize=14)

	# Set size of tick labels.
	ax.tick_params(axis="both", labelsize=14)

	# Set the range of each axis.
	ax.axis([1, 1100, 1, 1_100_000])

	# plt.show()
	plt.savefig('C:/Users/Victor/Desktop/test_plot.png', bbox_inches='tight')