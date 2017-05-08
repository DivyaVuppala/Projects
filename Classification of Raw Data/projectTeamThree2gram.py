import codecs
file1=codecs.open("FeaturedProcessed2grams.txt","r",'utf-8-sig')
file_text1=file1.read()
file2=codecs.open("NonFeaturedProcessedone2grams.txt","r",'utf-8-sig')
file_text2=file2.read()
file3=codecs.open("NonFeaturedProcessedtwo2grams.txt","r",'utf-8-sig')
file_text3=file3.read()
wordsarray=[]
for w in file_text1.split("\n"):
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

filenew=codecs.open("combined2grams.txt","w",'utf-8-sig')
for w in wordsarray2:
	filenew.write(w)
	filenew.write(",")
filenew.write("CLASS")
wordsarray2.append("CLASS")
wordsarray2

file=codecs.open("combined2grams.txt","r",'utf-8-sig')
text=file.read()
tokensarray=[]
for w in text.split(","):
	tokensarray.append(w)


newfile=codecs.open("combined2grams.txt","a",'utf-8-sig')
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


newfile=codecs.open("combined2grams.txt","a",'utf-8-sig')
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

