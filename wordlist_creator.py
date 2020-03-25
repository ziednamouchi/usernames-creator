#!/usr/bin/env python3
###############################################################################################################################################################
#
#Original Author : Zied Namouchi AKA zpycho
#Twitter : https://twitter.com/zpYcho
#Inspired from HTB Box Sauna
#Description: This scripts reads lines from users.txt as First_name[space]Last_name and then outputs a wordlist based on diffrent naming conventions
#users.txt contains some example of names (related to sauna htb machine)
#Exmaple with Joe Doe
#1-  joe
#2-  doe
#3-  joedoe
#4-  doejoe
#5-  joe.doe
#6-  doe.joe
#7-  jdoe
#8-  j.doe
#9-  j_doe
#10- doej
#11- doe.j
#12- doe_j
#13- djoe
#14- d.joe
#15- d_joe
#16- joed
#17- joe.d
#18- joe_d
#
################################################################################################################################################################



def first(name):
	return name[0].lower()


def last(name):
	return name[1].lower()


def first_last(name):
	return (''.join(name)).lower()


def last_first(name):
	return (''.join(name[::-1])).lower()


def first_dot_last(name):
	return ('.'.join(name)).lower()


def last_dot_first(name):
	return ('.'.join(name[::-1])).lower()


def f_last(name):
	return (name[0][:1]+name[1]).lower()


def f_dot_last(name):
	return (name[0][:1]+'.'+name[1]).lower()


def f_underscore_last(name):
	return (name[0][:1]+'_'+name[1]).lower()

def last_f(name):
	return (name[0][:1]+name[1]).lower()


def last_dot_f(name):
	return (name[0][:1]+'.'+name[1]).lower()


def last_underscore_f(name):
	return (name[0][:1]+'_'+name[1]).lower()

def l_first(name):
	return (name[1][:1]+name[0]).lower()


def l_dot_first(name):
	return (name[1][:1]+'.'+name[0]).lower()	


def l_underscore_first(name):
	return (name[1][:1]+'_'+name[0]).lower()

def first_l(name):
	return (name[1][:1]+name[0]).lower()


def first_dot_l(name):
	return (name[1][:1]+'.'+name[0]).lower()	


def first_underscore_l(name):
	return (name[1][:1]+'_'+name[0]).lower()


with open("users.txt","r") as f:
	for line in f:
		stripped_line = line.strip()
		name = stripped_line.split(' ')
		with open("wordlist.txt","a") as fw:
			fw.write(first(name)+"\n")
			fw.write(last(name)+"\n")
			fw.write(first_last(name)+"\n")
			fw.write(last_first(name)+"\n")
			fw.write(first_dot_last(name)+"\n")
			fw.write(last_dot_first(name)+"\n")
			fw.write(f_last(name)+"\n")
			fw.write(f_dot_last(name)+"\n")
			fw.write(f_underscore_last(name)+"\n")
			fw.write(last_f(name)+"\n")
			fw.write(last_dot_f(name)+"\n")
			fw.write(last_underscore_f(name)+"\n")
			fw.write(l_first(name)+"\n")
			fw.write(l_dot_first(name)+"\n")
			fw.write(l_underscore_first(name)+"\n")
			fw.write(first_l(name)+"\n")
			fw.write(first_dot_l(name)+"\n")
			fw.write(first_underscore_l(name)+"\n")
