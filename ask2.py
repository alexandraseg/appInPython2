import sys

if len(sys.argv)!=3:
	print("error")
	exit(-1)

fileName1=sys.argv[1]
fileName2=sys.argv[2]
file1=open(fileName1, "r")
file2=open(fileName2, "r")

terms1=[] 
terms2=[]

file1lines=file1.readlines()
file2lines=file2.readlines()

for line in file1lines:
	wordslist=line.split(" ")
	for word in wordslist:
		print(word)
		terms1.append(word)

for line in file2lines:
        wordslist=line.split(" ")
        for word in wordslist:
                print(word)
                terms2.append(word)

wordCount1={} 

for term in terms1:
	if term in wordCount1:
		c=wordCount1[term]
		c=c+1
		wordCount1[term]=c
	else:
		wordCount1[term]=1

wordCount2={}
for term in terms2:
        if term in wordCount2:
                c=wordCount2[term]
                c=c+1
                wordCount2[term]=c
        else:
                wordCount2[term]=1

file1out=open(fileName1+".csv", "w") 

for term in wordCount1:
	c=wordCount1[term]
	file1out.write("%s, %d \n"%(term, c)) 
file1out.close()


file2out=open(fileName2+".csv", "w")

for term in wordCount2:
        c=wordCount2[term]
        file2out.write("%s, %d \n"%(term, c)) 
file2out.close()

count=0
for term in wordCount1:
	if term in wordCount2:
		count=count+1


similarity=count/float(len(wordCount1))

print("Similarity: %f"%(similarity))
