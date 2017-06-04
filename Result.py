import urllib
from bs4 import BeautifulSoup


 #<-------------------------------------------------------------------------------------only code for IT branch, followinng the same logic , will work on other branches as well



for i in range(15601,15658):
	url = "http://knit.ac.in/coe/ODD_2016/btreg16xcdaz.asp?rollno="+str(i)
	print url
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	count = 0
	for tag in soup.find_all('tr'):
		count = count + 1
		if count == 33:
			entry = 0
			for num in tag.find_all('td'):
				entry = entry + 1
				if entry == 2:
					#print (num.contents[0])
					fh = open('result-file.txt','a')
					fh.write(num.contents[0]+"\t")
					fh.write(str(i)+"\n")

print "sorted data is"
list_h = []
handle = open("result-file.txt")
for line in handle:
	print line
	list_h.append((line[0:4],line[10:15]))
list_h.sort()
rank = 15657
print "This code snippet prints the result of IT branch only"
for i in list_h:
	print i," rank is",rank
	rank = rank - 1

