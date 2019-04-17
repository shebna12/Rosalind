sample_string = "AACTTCCGTTCCACGT"
sample_string_copy = sample_string.copy()
a_count,c_count,g_count,t_count = 0,0,0,0
for index, char in enumerate(sample_string):
	if char == "T":
		print(sample_string[index])
		sample_string_copy[index] = "U"


print(sample_string)
	