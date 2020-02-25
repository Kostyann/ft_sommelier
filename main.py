import os
import sys
import csv
import matplotlib as mpl
import matplotlib.pyplot as plt

def save(name='', fmt='png'):
	pwd = os.getcwd()
	iPath = './plots'
	if not os.path.exists(iPath):
		os.mkdir(iPath)
	os.chdir(iPath)
	plt.savefig(f"{name}.{fmt}")
	os.chdir(pwd)


# plt.close()


def plot_scatter_matrix(wine_data, good_threshold, bad_threshold, save_plot=False):

	keys = list(wine_data.keys())
	fig = plt.figure(figsize=(21, 15), constrained_layout=False)

	# gridspec inside gridspec
	outer_grid = fig.add_gridspec(11, 11, wspace=0.0, hspace=0.0)

	for i in range(121):
		ax = fig.add_subplot(outer_grid[i])
		if i // 11 == i % 11:
			ax.text(0.5, 0.5, keys[i // 11], horizontalalignment='center', verticalalignment='center')
		else:
			colors = ['red' if i >= good_threshold else 'blue' if i <= bad_threshold else '#ffffff00' for i in wine_data['quality']]
			ax.scatter(wine_data[keys[i // 11]], wine_data[keys[i % 11]], s=1, c=colors)
		ax.set_xticks([])
		ax.set_yticks([])

	plt.tight_layout()

#if save_plot:
		#       save('tada')
#	plt.savefig("plot.png")

	plt.show()

def main():
	if len(sys.argv) != 2:
		print("The script takes one argument")
		exit(1)

	file_read = os.path.abspath(sys.argv[1])
	if not os.path.exists(file_read):
		print("file does not exist.")
		exit(1)

	with open(file_read, "r", errors='ignore') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=';')
		d = {name: [] for name in reader.fieldnames}
		for row in reader:
			for name in reader.fieldnames:
				d[name].append(float(row[name]))

	plot_scatter_matrix(d, 8, 3, True)


if __name__ == '__main__':
	main()
