import matplotlib.pyplot as plt

if __name__ == "__main__":
	squares = [1, 4, 9, 16, 25, 36, 49]

	fig, ax = plt.subplots()
	ax.plot(squares)

	plt.show()