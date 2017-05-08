import codecs
file=codecs.open("FeaturedProcessed.txt","r",'utf-8-sig')
file_text=file.read()
wordsarray=[]
wordsarray.append(file_text)
file2=codecs.open("NonFeaturedProcessed1.txt","r",'utf-8-sig')
file_text2=file2.read()
wordsarray.append(file_text2)
file3=codecs.open("NonFeaturedProcessed2.txt","r",'utf-8-sig')
file_text3=file3.read()
wordsarray.append(file_text3)
wordsarray

wordsarray2=[]
for w in wordsarray:
	wordsarray2.append(w.rstrip())
wordsarray2


wordsarray3=[]
for w in wordsarray2:
	if w not in wordsarray3:
		wordsarray3.append(w)
wordsarray3

filenew=codecs.open("combined.txt","w",'utf-8-sig')
for w in wordsarray5:
    filenew.write(w)
    filenew.write(",")

wordsarray4.append("CLASS")
wordsarray4


file=codecs.open("combined.txt","r",'utf-8-sig')
text=file.read()
tokensarray=[]
for w in text.split(","):
	tokensarray.append(w)


newfile=codecs.open("combined.txt","a",'utf-8-sig')
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
 


z=codecs.open("NonFeaturedlinks.txt","r",'utf-8-sig')
newfile=codecs.open("combined.txt","a",'utf-8-sig')
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


