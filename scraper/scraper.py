from bs4 import BeautifulSoup
from shutil import copyfile
import os
import fileinput

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"}
soup = BeautifulSoup(open("index.html"), 'html.parser')

try:
	os.mkdir("./2020")
	os.mkdir("./2020/A")
	os.mkdir("./2020/B")
except:
	print("the directory already exists.. it's okay")

# originally will be A
all_text = [tag for tag in soup.find_all(class_ = "cmty-view-post-item-text")]
print(all_text)

psf = open("2020/A/problemset.html", "w")
copyfile("problemset.html", "2020/A/problemset.html");
copyfile("stylebutwhite.css", "2020/A/stylebutwhite.css");
copyfile("problemset.html", "2020/B/problemset.html");
copyfile("stylebutwhite.css", "2020/B/stylebutwhite.css");

counter = 1
for i in range(1, 26):
	file_name = str(i) + ".html"
	f = open("2020/A/" + file_name, "w")
	f.write("<!DOCTYPE html>")
	f.write("<html>")
	f.write('<head>')
	f.write('\t<link rel="stylesheet" href="stylebutwhite.css">')
	f.write('</head>')
	f.write('<body>')
	f.write('\t<h2><span>Problem '  + str(i) + '</span> <a href="' + file_name + '" target="_blank" rel="noopener noreferrer">View full problem</a></h2>')
	f.write(str(all_text[counter]))
	f.write('</body>')
	f.write('</html>')
	f.close()
	counter += 1
	with fileinput.FileInput("2020/A/" + file_name, inplace=True, backup='.bak') as file:
		for line in file:
			print(line.replace("//", "https://"), end='')

# originally will be B
counter += 1

for i in range(1, 26):
	file_name = str(i) + ".html"
	f = open("2020/B/" + file_name, "w")
	f.write("<!DOCTYPE html>")
	f.write("<html>")
	f.write('<head>')
	f.write('\t<link rel="stylesheet" href="stylebutwhite.css">')
	f.write('</head>')
	f.write('<body>')
	f.write('\t<h2><span>Problem '  + str(i) + '</span> <a href="' + file_name + '" target="_blank" rel="noopener noreferrer">View full problem</a></h2>')
	f.write(str(all_text[counter]))
	f.write('</body>')
	f.write('</html>')
	f.close()
	counter += 1
	with fileinput.FileInput("2020/B/" + file_name, inplace=True, backup='.bak') as file:
		for line in file:
			print(line.replace("//", "https://"), end='')
