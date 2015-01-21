
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
		return [count, avg / count]

if __name__ == '__main__':
	d = Delayparser()

	util = [10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 98]

	for u in util:
		f = "outputs/qt_" + str(u) + ".txt"
		ret = d.parse(f)
		print "{:.0f}% utilization: {:.0f} packets, {:.6f} average queue delay.".format(u, ret[0], ret[1])

	# print "10% utilization: " + str(d.parse("outputs/qt_10.txt"))
	# print "20% utilization: " + str(d.parse("outputs/qt_20.txt"))
	# print "30% utilization: " + str(d.parse("outputs/qt_30.txt"))
	# print "40% utilization: " + str(d.parse("outputs/qt_40.txt"))
	# print "50% utilization: " + str(d.parse("outputs/qt_50.txt"))
	# print "60% utilization: " + str(d.parse("outputs/qt_60.txt"))
	# print "70% utilization: " + str(d.parse("outputs/qt_70.txt"))
	# print "80% utilization: " + str(d.parse("outputs/qt_80.txt"))
	# print "90% utilization: " + str(d.parse("outputs/qt_90.txt"))
	# print "95% utilization: " + str(d.parse("outputs/qt_95.txt"))
	# print "98% utilization: " + str(d.parse("outputs/qt_98.txt"))