import wikipedia
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from collections import defaultdict
from operator import itemgetter
file = open("Featured.txt", "r")
file2 = open("Featued_list.txt", "w")
stop_words = set(stopwords.words("english"))
porter = PorterStemmer()
for line in file.readlines():
    print (line.rstrip())
    A = wikipedia.summary(line)
    A = A.replace(",", "")
    A = A.replace("(", "")
    A = A.replace('"', "")
    A = A.replace(")", "")
    A = A.replace("/", "")
    A = A.replace("@", "")
    A = A.replace("'", "")
    A = A.replace(".", "")
    A = A.replace("-", "")
    A = A.replace(":", "")
    A = A.replace(";", "")
    A = A.replace("$", "")
    A = A.replace("*", "")
    print (A)
    file2.write(" " + "\n" + A)
file3 = open("Featued_list.txt", "r")
file4 = open("Featured_ProcessedWords.txt", "w")
for line in file3.readlines():
    words = line.split()
    for word in words:
        if word not in stop_words:
            B = porter.stem(word)
            print(B)
            file4.write(" " + "\n" + B)
#Processing of Negative dataset, Category: Lost Films
Nile = open("Non_Featured.txt", "r")
Nile2 = open("Non_Featured_list.txt", "w")
stop_words = set(stopwords.words("english"))
porter = PorterStemmer()
for line in Nile.readlines():
    print (line.rstrip())
    C = wikipedia.summary(line)
    C = C.replace(",", "")
    C = C.replace("(", "")
    C = C.replace('"', "")
    C = C.replace(")", "")
    C = C.replace("/", "")
    C = C.replace("@", "")
    C = C.replace("'", "")
    C = C.replace(".", "")
    C = C.replace("-", "")
    C = C.replace(":", "")
    C = C.replace(";", "")
    C = C.replace("$", "")
    C = C.replace("*", "")
    print (C)
    Nile2.write(" " + "\n" + C)
Nile3 = open("Non_Featured_list.txt", "r")
Nile4 = open("Non_Featured_list_ProcessedWords.txt", "w")
for line in Nile3.readlines():
    words2 = line.split()
    for word in words2:
        if word not in stop_words:
            D = porter.stem(word)
            print(D)
            Nile4.write(" " + "\n" + D)
#Processing of Negative dataset, Category: American Theater Hall of Fame inductees
Bile = open("Non_Featured2.txt", "r")
Bile2 = open("Non_Featured2_list.txt", "w")
stop_words = set(stopwords.words("english"))
porter = PorterStemmer()
for line in Bile.readlines():
    print (line.rstrip())
    E = wikipedia.summary(line)
    E = E.replace(",", "")
    E = E.replace("(", "")
    E = E.replace('"', "")
    E = E.replace(")", "")
    E = E.replace("/", "")
    E = E.replace("@", "")
    E = E.replace("'", "")
    E = E.replace(".", "")
    E = E.replace("-", "")
    E = E.replace(":", "")
    E = E.replace(";", "")
    E = E.replace("$", "")
    E = E.replace("*", "")
    print (E)
    Bile2.write(" " + "\n" + E)
Bile3 = open("Non_Featured2_list.txt", "r")
Bile4 = open("Non_Featured2_list_ProcessedWords.txt", "w")
for line in Bile3.readlines():
    words3 = line.split()
    for word in words3:
        if word not in stop_words:
            F = porter.stem(word)
            print(F)
            Bile4.write(" " + "\n" + F)

