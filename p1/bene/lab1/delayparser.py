
class Delayparser(object):
	def __init__(self):
		pass

	def parse(self, filename):
		f = open(filename, "r")

		avg = 0.0
		count = 0.0
		# skip the first line
		for line in f.readlines():
			if (line[0] != 'R' and line[0] != '\n'):
				avg += float(line.split(' ')[6].split('\n')[0])
				count += 1
		return avg / count

if __name__ == '__main__':
	d = Delayparser()

	print d.parse("outputs/qt_test.txt")
