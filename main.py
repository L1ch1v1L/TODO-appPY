import os

import json

global DIR 
DIR = "Tasks/"

class Task(object):
	# Easier to create task.
	def add_example_file(self,name):
		# add_example_file
		data = {
		
			"name" : "Example_name",
			"description" : "Example_description",
			"finished" : False

		}
		print("Creating example.")
		try:
			with open(DIR+name+".json","w+") as write_file:
				json.dump(data, write_file)
		except:
			os.mkdir(DIR)
		finally:
			with open(DIR+name+".json","w+") as write_file:
				json.dump(data, write_file)

	def change_file(self,name,description,finished,file):
		data = {
			"name" : name,
			"description" : description,
			"finished" : finished
		}
		with open(DIR+file, "w") as write_file:
   			json.dump(data, write_file)
	def __init__(self, name, description, finished):
		# init task
		self.name = name
		self.description = description
		self.finished = finished
	
		

def main():
	while True:
		print("Hello! This is console-app TODO.")
		print("You can moderate your tasks.")
		print("\n")
		print("1. Check task. 2. Delete task. 3. Change task. 4. Make a example task. 5. QUIT")
		print("\n")
		choose = input("> ")
		try:
			if int(choose) == 1:
				print("\n\nYou want to check your tasks.")
				print("Your tasks:\n")
				print_tasks()
			elif int(choose) == 2:
				print("\n\nYou want to delete your tasks.")
				print("Your tasks:")
				delete_tasks()
			elif int(choose) == 3:
				print("\n\nYou want to change your tasks.")
				print("Your tasks:")
				change_tasks()
			elif int(choose) == 4:
				print("\n")
				task = Task("example","","")
				task.add_example_file(task.name)
				print("\n")
			elif int(choose) == 5:
				print("QUIT!")
				exit()
		except ValueError:
			print("\n\nI said input number.")

def print_tasks():
	path = DIR
	try:
		directories = os.listdir(path)
	except:
		os.mkdir(DIR)
	finally:
		directories = os.listdir(path)
	# print of the files in current path and has format .json
	for file in directories:
		if file.endswith(".json"):
			f = open(DIR+file,)
			data = json.load(f)
			data_name = data["name"]
			print(data_name,"\n")
	print("Enter a name of your task to see.")
	name = input("> ")
	for file in directories:
			if file.endswith(".json"):
				filee = open(DIR+file,'r')
				# i did for debug
				# print(filee.read())
				f = open(DIR+file,)
				data = json.load(f)
				data_name = data["name"]
				data_description = data["description"]
				data_finished = data["finished"]
				return print_current_task(data_name,data_description,data_finished)
	print("\nERROR")
	try:
		print('With name "',name,'" task is not exist.\n\n')
	except NameError:
		print('With name "NOT FOUND" task is not exist.\n\n')

def print_current_task(name, description, finished):
	print("\n\n")
	print("Name: ", str(name))
	print("\n")
	print("Description: ", str(description))
	print("\n")
	print("Finished: ", str(finished))
	print("\n\n")

def delete_tasks():
	flag = 0
	path = DIR
	try:
		directories = os.listdir(path)
	except:
		os.mkdir(DIR)
	finally:
		directories = os.listdir(path)
	# print of the files in current path and has format .json
	for file in directories:
		if file.endswith(".json"):
			f = open(DIR+file,)
			data = json.load(f)
			data_name = data["name"]
			print(data_name,"\n")
	print("Enter a name of your task to delete. \n(IF YOU WANNA DELETE ALL FILES IN DIR WRITE 'deletingall'")
	name = input("> ")
	if name != "deletingall":
		# Check if format .json and name then print else "error"
		for file in directories:
			if file.endswith(".json"):
				f = open(DIR+file,)
				data = json.load(f)
				data_name = data["name"]
				if name == data_name:
					print("\n")
					print("DELETE!")
					print("\n")
					return os.remove(DIR+file)
	elif name == "deletingall":
		flag = 1
		print("\n")
		# CHECK if format .json and name then print else "error"
		for file in directories:
			if file.endswith(".json"):
					print("DELETE FILE: ",file,"!")
					os.remove(DIR+file)
					print("\n")
	if flag == 1:
		pass 
	else: 
		print("\nERROR")
		try:
			print('With name "',name,'" task is not exist.\n\n')
		except NameError:
			print('With name "NOT FOUND" task is not exist.\n\n')

def change_tasks():
	print("\n")
	path = DIR
	try:
		directories = os.listdir(path)
	except:
		os.mkdir(DIR)
	finally:
		directories = os.listdir(path)
	# print of the files in current path and has format .json
	for file in directories:
		if file.endswith(".json"):
			f = open(DIR+file,)
			data = json.load(f)
			data_name = data["name"]
			print(data_name,"\n")
	print("Enter a name of your task to change.")
	name = input("> ")
	# Check if format .json and name then print else "error"
	for file in directories:
		if file.endswith(".json"):
			f = open(DIR+file,)
			data = json.load(f)
			data_name = data["name"]
			if name == data_name:
				data_description = data["description"]
				data_finished = data["finished"]
				print("\n")
				return change_current_task(data_name, data_description, data_finished,file)

	print("\nERROR")
	try:
		print('With name "',name,'" task is not exist.\n\n')
	except NameError:
		print('With name "NOT FOUND" task is not exist.\n\n')

def change_current_task(name, description, finished,file):
	os.remove(DIR+file)
	task = Task("","",False)
	print("Enter a name:")
	name = input("> ")
	task.name = name
	print("\n")
	print("Enter a description:")
	description = input("> ")
	task.description = description
	print("\n")
	print("Enter a finished or not(1 - finished, 0 - not finished):")
	finished = input("> ")
	try:
		if int(finished) == 1:
			finished = True

		elif int(finished) == 2:
			finished = False
	except ValueError:
		print("\n")
		print("Do example thing. \nFalse.\n")
		finished = False
	task.finished = finished
	print("Enter a name of file (without format):")
	new_file = input("> ")
	print("\n")
	task.change_file(task.name,task.description,task.finished,new_file+".json")


if __name__ == '__main__':
	main()
