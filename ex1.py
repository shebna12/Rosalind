sample_string = "AACTTCCGTTCCACGT"
# initialize
a_count,c_count,g_count,t_count = 0,0,0,0
for char in sample_string:
	if char == "A":
		a_count += 1
	elif char == "C":
		c_count += 1
	elif char == "G":
		g_count += 1
	else:
		t_count += 1

print("{} {} {} {}".format(a_count,c_count,g_count,t_count))