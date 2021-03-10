from bs4 import BeautifulSoup
from shutil import copyfile
import os
import fileinput

soup = BeautifulSoup(open("index.html", encoding='utf-8'), 'html.parser')

def is_int(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

def is_valid_test_name(s):
	if s == "AMC8" or s == "AMC10" or s == "AMC12" or s == "AIME":
		return True
	return False

print("Welcome to the AoPS Scrapper! First, make sure you have created the index.html file.")
print("If you are unsure of what this is, please look at the README.md file.")
try:
	input("Press enter if you are ready.")
except SyntaxError:
	pass

year_str = input("Enter the year: ")
while (not is_int(year_str)):
	print("Invalid year!")
	year_str = input("Enter the year: ")

test_name = input("Enter one of the following: AMC8, AMC10, AMC12, or AIME:")
while(not is_valid_test_name(test_name)):
	print("Invalid test name!")
	test_name = input("Enter one of the following: AMC8, AMC10, AMC12, or AIME:")

try:
	os.mkdir("./" + year_str)
except:
	print("the directory with the name " + year_str + " already exists. that's fine.")

all_text = [tag for tag in soup.find_all(class_ = "cmty-view-post-item-text")]

if(test_name == "AMC8"):
	copyfile("problemsetamc.html", year_str + "/problemset.html");
	copyfile("stylebutwhite.css", year_str + "/stylebutwhite.css");
	skip = input("How many rows before the problems should be skipped? ")
	while (not is_int(skip)):
		print("Invalid number!")
		skip = input("How many rows before the problems should be skipped? ")
		
	counter = int(skip)
	
	for i in range(1, 26):
		file_name = ""
		if 1 <= i and i <= 9:
			file_name = "0" + str(i) + ".html"
		else:
			file_name = str(i) + ".html"
		f = open(year_str + "/" + file_name, "w")
		f.write("<!DOCTYPE html>")
		f.write("<html>")
		f.write('<head>')
		f.write('\t<link rel="stylesheet" href="stylebutwhite.css">')
		f.write('</head>')
		f.write('<body>')
		f.write('\t<h2><span>' + year_str + ' ' + test_name + ' Problem '  + str(i) + '</span> <a href="' + file_name + '" target="_blank" rel="noopener noreferrer">View full problem</a></h2>')
		f.write(str(all_text[counter]))
		f.write('</body>')
		f.write('</html>')
		f.close()
		counter += 1
		with fileinput.FileInput(year_str + "/" + file_name, inplace=True, backup='.bak') as file:
			for line in file:
				print(line.replace("//", "https://"), end='')

elif(test_name == "AMC10" or test_name == "AMC12"):
	try:
		os.mkdir("./" + year_str + "/A")
		os.mkdir("./" + year_str + "/B")
	except:
		print("directories already exist. that's okay")
	copyfile("problemsetamc.html", year_str + "/A/problemset.html");
	copyfile("stylebutwhite.css", year_str + "/A/stylebutwhite.css");
	copyfile("problemsetamc.html", year_str + "/B/problemset.html");
	copyfile("stylebutwhite.css", year_str + "/B/stylebutwhite.css");

	skip = input("How many rows before test A should be skipped? ")
	while (not is_int(skip)):
		print("Invalid number!")
		skip = input("How many rows before test A should be skipped? ")
		
	counter = int(skip)
	
	for i in range(1, 26):
		file_name = ""
		if 1 <= i and i <= 9:
			file_name = "0" + str(i) + ".html"
		else:
			file_name = str(i) + ".html"
		f = open(year_str + "/A/" + file_name, "w")
		f.write("<!DOCTYPE html>")
		f.write("<html>")
		f.write('<head>')
		f.write('\t<link rel="stylesheet" href="stylebutwhite.css">')
		f.write('</head>')
		f.write('<body>')
		f.write('\t<h2><span>' + year_str + ' ' + test_name + 'A Problem '  + str(i) + '</span> <a href="' + file_name + '" target="_blank" rel="noopener noreferrer">View full problem</a></h2>')
		f.write(str(all_text[counter]))
		f.write('</body>')
		f.write('</html>')
		f.close()
		counter += 1
		with fileinput.FileInput(year_str + "/A/" + file_name, inplace=True, backup='.bak') as file:
			for line in file:
				print(line.replace("//", "https://"), end='')

	skip = input("How many rows before test B should be skipped? ")
	while (not is_int(skip)):
		print("Invalid number!")
		skip = input("How many rows before test B should be skipped? ")
		
	counter += int(skip)

	for i in range(1, 26):
		file_name = ""
		if 1 <= i and i <= 9:
			file_name = "0" + str(i) + ".html"
		else:
			file_name = str(i) + ".html"
		f = open(year_str + "/B/" + file_name, "w")
		f.write("<!DOCTYPE html>")
		f.write("<html>")
		f.write('<head>')
		f.write('\t<link rel="stylesheet" href="stylebutwhite.css">')
		f.write('</head>')
		f.write('<body>')
		f.write('\t<h2><span>' + year_str + ' ' + test_name + 'B Problem '  + str(i) + '</span> <a href="' + file_name + '" target="_blank" rel="noopener noreferrer">View full problem</a></h2>')
		f.write(str(all_text[counter]))
		f.write('</body>')
		f.write('</html>')
		f.close()
		counter += 1
		with fileinput.FileInput(year_str + "/B/" + file_name, inplace=True, backup='.bak') as file:
			for line in file:
				print(line.replace("//", "https://"), end='')

elif(test_name == "AIME"):
	try:
		os.mkdir("./" + year_str + "/I")
		os.mkdir("./" + year_str + "/II")
	except:
		print("directories already exist. that's okay")
	copyfile("problemsetaime.html", year_str + "/I/problemset.html");
	copyfile("stylebutwhite.css", year_str + "/I/stylebutwhite.css");
	copyfile("problemsetaime.html", year_str + "/II/problemset.html");
	copyfile("stylebutwhite.css", year_str + "/II/stylebutwhite.css");

	skip = input("How many rows before test I should be skipped? ")
	while (not is_int(skip)):
		print("Invalid number!")
		skip = input("How many rows before test I should be skipped? ")
		
	counter = int(skip)
	
	for i in range(1, 16):
		file_name = ""
		if 1 <= i and i <= 9:
			file_name = "0" + str(i) + ".html"
		else:
			file_name = str(i) + ".html"
		f = open(year_str + "/I/" + file_name, "w")
		f.write("<!DOCTYPE html>")
		f.write("<html>")
		f.write('<head>')
		f.write('\t<link rel="stylesheet" href="stylebutwhite.css">')
		f.write('</head>')
		f.write('<body>')
		f.write('\t<h2><span>' + year_str + ' ' + test_name + ' I Problem '  + str(i) + '</span> <a href="' + file_name + '" target="_blank" rel="noopener noreferrer">View full problem</a></h2>')
		f.write(str(all_text[counter]))
		f.write('</body>')
		f.write('</html>')
		f.close()
		counter += 1
		with fileinput.FileInput(year_str + "/I/" + file_name, inplace=True, backup='.bak') as file:
			for line in file:
				print(line.replace("//", "https://"), end='')

	skip = input("How many rows before test II should be skipped? ")
	while (not is_int(skip)):
		print("Invalid number!")
		skip = input("How many rows before test II should be skipped? ")
		
	counter += int(skip)

	for i in range(1, 16):
		file_name = ""
		if 1 <= i and i <= 9:
			file_name = "0" + str(i) + ".html"
		else:
			file_name = str(i) + ".html"
		f = open(year_str + "/II/" + file_name, "w")
		f.write("<!DOCTYPE html>")
		f.write("<html>")
		f.write('<head>')
		f.write('\t<link rel="stylesheet" href="stylebutwhite.css">')
		f.write('</head>')
		f.write('<body>')
		f.write('\t<h2><span>' + year_str + ' ' + test_name + ' II Problem '  + str(i) + '</span> <a href="' + file_name + '" target="_blank" rel="noopener noreferrer">View full problem</a></h2>')
		f.write(str(all_text[counter]))
		f.write('</body>')
		f.write('</html>')
		f.close()
		counter += 1
		with fileinput.FileInput(year_str + "/II/" + file_name, inplace=True, backup='.bak') as file:
			for line in file:
				print(line.replace("//", "https://"), end='')
