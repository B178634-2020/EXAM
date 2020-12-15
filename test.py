#!/usr/bin/python3
# shebang on the first line
# written by B178634
import os, sys, subprocess

#======MAKEBLASTDB======
#show current path and create a new dir
workingdir = os.getcwd()
print("you're now working at" + workingdir)
os.mkdir(workingdir + '/blast')
os.chdir(workingdir + '/blast')

#=======First, input query sequence
query = input("please input the sequence that you want to blast")
#这里可以有多种防出错机制

#=======Second, input fasta file to search against and make a blast searchable database
dbornot = input("Do you want to make your own database to search for sequences against? (yes/no") 
if dbornot.upper() == "YES" or dbornot.upper() == "Y":
	#Running BLAST locally
	dbfilepath = input("please input the path of local fasta file (including full name)")
	# step 1 makeblastdb
	#原：os.system("makeblastdb -in sequence.fasta -dbtype prot -out blastpdb")

	os.system("makeblastdb -in " + dbfilepath + " -dbtype prot -out blastpdb")

	# Dealing with error : try
	# IN CASE that users input wrong filename or path
	try:
		res = subprocess.check_call("makeblastdb -in " + dbfilepath + " -dbtype prot -out blastpdb")
		print('res:', res)
	except subprocess.CalledProcessError:
		print("Error. Please check that the path and filename is correct.")
	#这里应该产生一个和上次类似的循环结构，不成功就一直继续下去

#=======Thirdly, which blast to do: blastn/blastp/tblastn/tblastx/... against database

	# step 2 blast
	blasttype = input("which kind of blast are you going to do? (blastn/blastp/tblastn/tblastx)")
	if blasttype.lower() != "blastn" or blasttype.lower() != "blastp" or blasttype.lower() != "tblastn" or blasttype.lower() != "tblastx":
		print("please input the right type")
	os.system('rm -f blastoutput.out')
	os.system(blasttype + " -db blastpdb -query input.fasta -outfmt 7 > blastoutput.out ")

	# step 3 processing: show the blast analysis result
	more blastoutput.out

else: #Running BLAST over the Internet
