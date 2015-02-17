with open("outputs/output2-5.txt") as f:
	prev = 0
	count = 0
	time = 0
	alltimes = []
	for line in f:
		tokens = line.split()
		if (len(tokens) >= 4 and tokens[3] == "retransmission"):
			time += float(tokens[0]) - prev
			count += 1
			alltimes.append(float(tokens[0]) - prev)
		if (len(tokens) > 0):
			try:
				prev = float(tokens[0])
			except:
				pass
	print "Average time: " + str(time/count)
	print "Count: " + str(count)
	# print "all: " + str(alltimes)