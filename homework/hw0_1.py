import sys

words_dic={}
words_num={}
num = 0;
with open('words.txt','rb') as inf:
	words = str(inf.read().strip()).split(' ')
	for word in words:
		word.strip('\r')
		if word in words_dic:
			words_dic[word] +=1
		else:
			num +=1
			words_num[num] = word
			words_dic[word] = 1

with open('q1.txt','wb') as outf:
	for num in sorted(words_num.keys()):
		word = words_num[num]
		outf.writelines(word + ' '+ str(num)+' '+ str(words_dic[word])+'\n')
	
