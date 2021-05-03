#!/usr/bin/env python3

fd = open("out.txt", "r")
output = list()
for char in fd:
    output.append(char)

for idx, ele in enumerate(output):
    output[idx] = ele.replace(' \n', '')
    output[idx] = chr(int(output[idx]))

print("".join(output))
fd.close()
