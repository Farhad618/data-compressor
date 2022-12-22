# code = input("enter the code: ")
# div = int(input("Enter the division: "))
code = "1234113562340006500"
div = 7
length = len(code)
def catch_char(c, startfrom):
	# print("c:"+c+" startfrom:"+str(startfrom))
	i=0
	out_char=""
	for x in range(startfrom, length):
		if i < div:
			if code[x] == c:
				out_char+="1"
				i+=1
			elif (int(code[x])>int(c)) or (code[x]=="0"):
				out_char+="0"
				i+=1
		else:
			break
	while len(out_char)<div:
		out_char+="0"
	print(out_char)

i=1
for x in range(length):
	# print("x:"+x)
	if i==int(code[x]):
		catch_char(code[x], x)
		i+=1	
			

