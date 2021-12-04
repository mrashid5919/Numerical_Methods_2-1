def reverse(sentence):
	sentence=sentence.split(" ")
	ara=[]
	for word in sentence:
		ara.append(word)
	for i in range(len(ara)):
		print(ara[len(ara)-i-1],end=" ")
		
reverse("Hello World")