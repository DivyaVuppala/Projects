import codecs
file1=codecs.open("FeaturedProcessed3grams.txt","r",'utf-8-sig')
file_text=file1.read()
file2=codecs.open("NonFeaturedProcessedone3grams.txt","r",'utf-8-sig')
file_text2=file2.read()
file3=codecs.open("NonFeaturedProcessedtwo3grams.txt","r",'utf-8-sig')
file_text3=file3.read()
wordsarray=[]
for w in file_text.split("\n"):
	wordsarray.append(w)

for w in file_text2.split("\n"):
    wordsarray.append(w)
 
for w in file_text3.split("\n"):
    wordsarray.append(w) 
wordsarray

wordsarray2=[]
for w in wordsarray:
	if w not in wordsarray2:
		wordsarray2.append(w)
wordsarray2


filenew=codecs.open("combined3grams.txt","w",'utf-8-sig')
for w in wordsarray2:
	filenew.write(w)
    filenew.write(",")
wordsarray2.append("CLASS")


file=codecs.open("combined3grams.txt","r",'utf-8-sig')
text=file.read()
tokensarray=[]
for w in text.split(","):
	tokensarray.append(w)
tokensarray

import wikipedia
newfile=codecs.open("combined3grams.txt","a",'utf-8-sig')
y=codecs.open("Featuredlinks.txt","r",'utf-8-sig')
for line in y.readlines():
	a=wikipedia.summary(line)
    for w in tokensarray:
    	if w in a:
    		newfile.write("1")
            newfile.write(",")
        elif w=="CLASS":
            newfile.write("Featured")
            newfile.write("\n")
        elif w not in a:
            newfile.write("0")
            newfile.write(",")


newfile=codecs.open("combined3grams.txt","a",'utf-8-sig')
z=codecs.open("NonFeaturedlinks.txt","r",'utf-8-sig')
for line in z.readlines():
	a=wikipedia.summary(line)
	for w in tokensarray:
		if w in a:
			newfile.write("1")
            newfile.write(",")
        elif w=="CLASS":
            newfile.write("NonFeatured")
            newfile.write("\n")
        elif w not in a:
        	newfile.write("0")
        	newfile.write(",")