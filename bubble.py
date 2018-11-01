s= list(map(int, input("Enter the list: ").split()))

for j  in range(len(s)):
	for i in range(len(s) - j - 1):
		if(s[i] > s[i + 1]):
			s[i], s[i+1] = s[i+1], s[i]

print(s)
