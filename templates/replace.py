# Program to replace problemset.html and stylebutwhite.css files with the files in this directory

import os
from shutil import copyfile

# https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory

for directory in os.listdir("../amc8"):
	print(directory)
	print("../amc8/" + directory + "/problemset.html")
	copyfile("problemsetamc.html", "../amc8/" + directory + "/problemset.html")
	print("../amc8/" + directory + "/stylebutwhite.css")
	copyfile("stylebutwhite.css", "../amc8/" + directory + "/stylebutwhite.css")

for directory in os.listdir("../amc10"):
	print(directory)
	print("../amc10/" + directory + "/A/problemset.html")
	copyfile("problemsetamc.html", "../amc10/" + directory + "/A/problemset.html")
	print("../amc10/" + directory + "/A/stylebutwhite.css")
	copyfile("stylebutwhite.css", "../amc10/" + directory + "/A/stylebutwhite.css")
	print("../amc10/" + directory + "/B/problemset.html")
	copyfile("problemsetamc.html", "../amc10/" + directory + "/B/problemset.html")
	print("../amc10/" + directory + "/B/stylebutwhite.css")
	copyfile("stylebutwhite.css", "../amc10/" + directory + "/B/stylebutwhite.css")

for directory in os.listdir("../amc12"):
	print(directory)
	print("../amc12/" + directory + "/A/problemset.html")
	copyfile("problemsetamc.html", "../amc12/" + directory + "/A/problemset.html")
	print("../amc12/" + directory + "/A/stylebutwhite.css")
	copyfile("stylebutwhite.css", "../amc12/" + directory + "/A/stylebutwhite.css")
	print("../amc12/" + directory + "/B/problemset.html")
	copyfile("problemsetamc.html", "../amc12/" + directory + "/B/problemset.html")
	print("../amc12/" + directory + "/B/stylebutwhite.css")
	copyfile("stylebutwhite.css", "../amc12/" + directory + "/B/stylebutwhite.css")

for directory in os.listdir("../aime"):
	print(directory)
	print("../aime/" + directory + "/I/problemset.html")
	copyfile("problemsetaime.html", "../aime/" + directory + "/I/problemset.html")
	print("../aime/" + directory + "/I/stylebutwhite.css")
	copyfile("stylebutwhite.css", "../aime/" + directory + "/I/stylebutwhite.css")
	print("../aime/" + directory + "/II/problemset.html")
	copyfile("problemsetaime.html", "../aime/" + directory + "/II/problemset.html")
	print("../aime/" + directory + "/II/stylebutwhite.css")
	copyfile("stylebutwhite.css", "../aime/" + directory + "/II/stylebutwhite.css")

copyfile("problemsetaime.html", "../scraper/problemsetaime.html")
copyfile("problemsetamc.html", "../scraper/problemsetamc.html")
copyfile("stylebutwhite.css", "../scraper/stylebutwhite.css")
