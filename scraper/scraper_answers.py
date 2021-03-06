from bs4 import BeautifulSoup
from shutil import copyfile
import os
import fileinput
import requests

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

print("Welcome to the AoPS Scrapper to scrape answers!")
# print("If you are unsure of what this is, please look at the README.md file.")
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

if(test_name == "AMC8"):
	# format: https://artofproblemsolving.com/wiki/index.php/2020_AMC_8_Answer_Key
	url = "https://artofproblemsolving.com/wiki/index.php/" + year_str + "_AMC_8_Answer_Key"
	req = requests.get(url)
	soup = BeautifulSoup(req.text, 'html.parser')
	answers_div = soup.find(class_="mw-parser-output")
	answers_div = answers_div.ol
	answers_div = answers_div.li
	out = open("../amc8/" + year_str + "/answers.txt", 'w')
	
	for i in range(0, 25):
		out.write(str(answers_div.text))
		out.write('\n')
		if(i != 24):
			answers_div = answers_div.next_sibling
			answers_div = answers_div.next_sibling

elif(test_name == "AMC10"):
	url = "https://artofproblemsolving.com/wiki/index.php/" + year_str + "_AMC_10A_Answer_Key"
	req = requests.get(url)
	soup = BeautifulSoup(req.text, 'html.parser')
	answers_div = soup.find(class_="mw-parser-output")
	answers_div = answers_div.ol
	answers_div = answers_div.li
	out = open("../amc10/" + year_str + "/A/answers.txt", 'w')
	
	for i in range(0, 25):
		out.write(str(answers_div.text))
		out.write('\n')
		if(i != 24):
			answers_div = answers_div.next_sibling
			answers_div = answers_div.next_sibling
	
	url = "https://artofproblemsolving.com/wiki/index.php/" + year_str + "_AMC_10B_Answer_Key"
	req = requests.get(url)
	soup = BeautifulSoup(req.text, 'html.parser')
	answers_div = soup.find(class_="mw-parser-output")
	answers_div = answers_div.ol
	answers_div = answers_div.li
	out = open("../amc10/" + year_str + "/B/answers.txt", 'w')
	
	for i in range(0, 25):
		out.write(str(answers_div.text))
		out.write('\n')
		if(i != 24):
			answers_div = answers_div.next_sibling
			answers_div = answers_div.next_sibling

elif(test_name == "AMC12"):
	url = "https://artofproblemsolving.com/wiki/index.php/" + year_str + "_AMC_12A_Answer_Key"
	req = requests.get(url)
	soup = BeautifulSoup(req.text, 'html.parser')
	answers_div = soup.find(class_="mw-parser-output")
	answers_div = answers_div.ol
	answers_div = answers_div.li
	out = open("../amc12/" + year_str + "/A/answers.txt", 'w')
	
	for i in range(0, 25):
		out.write(str(answers_div.text))
		out.write('\n')
		if(i != 24):
			answers_div = answers_div.next_sibling
			answers_div = answers_div.next_sibling
	
	url = "https://artofproblemsolving.com/wiki/index.php/" + year_str + "_AMC_12B_Answer_Key"
	req = requests.get(url)
	soup = BeautifulSoup(req.text, 'html.parser')
	answers_div = soup.find(class_="mw-parser-output")
	answers_div = answers_div.ol
	answers_div = answers_div.li
	out = open("../amc12/" + year_str + "/B/answers.txt", 'w')
	
	for i in range(0, 25):
		out.write(str(answers_div.text))
		out.write('\n')
		if(i != 24):
			answers_div = answers_div.next_sibling
			answers_div = answers_div.next_sibling

elif(test_name == "AIME"):
	url = "https://artofproblemsolving.com/wiki/index.php/" + year_str + "_AIME_I_Answer_Key"
	req = requests.get(url)
	soup = BeautifulSoup(req.text, 'html.parser')
	answers_div = soup.find(class_="mw-parser-output")
	answers_div = answers_div.ol
	answers_div = answers_div.li
	out = open("../aime/" + year_str + "/I/answers.txt", 'w')
	
	for i in range(0, 15):
		out.write(str(answers_div.text))
		out.write('\n')
		if(i != 14):
			answers_div = answers_div.next_sibling
			answers_div = answers_div.next_sibling
	
	url = "https://artofproblemsolving.com/wiki/index.php/" + year_str + "_AIME_II_Answer_Key"
	req = requests.get(url)
	soup = BeautifulSoup(req.text, 'html.parser')
	answers_div = soup.find(class_="mw-parser-output")
	answers_div = answers_div.ol
	answers_div = answers_div.li
	out = open("../aime/" + year_str + "/II/answers.txt", 'w')
	
	for i in range(0, 15):
		out.write(str(answers_div.text))
		out.write('\n')
		if(i != 14):
			answers_div = answers_div.next_sibling
			answers_div = answers_div.next_sibling
