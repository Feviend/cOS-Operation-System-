from os import*
from time import*
from random import*
from colorama import*
from PC_Game import*
init(autoreset=True)
errors = ["SYSTEM ERROR!!", "Reloading...", "Aaaaaaaa", "Main core is broken!"]

def intc(num):
	if num < 10:
		return "000" + str(num)
	elif num < 100:
		return "00" + str(num)
	elif num < 1000:
		return "0" + str(num)
	else:
		return str(num)
def kill():
	while True:
		index = "0x" + intc(randint(0, 9999)) + ": "
		print(Fore.RED + index + choice(errors))
		sleep(0.1)

version = 1.0
m = "/main/"
print("cOS " + str(version) + " version")
locate = "/main/"
lang = "eng"
tools = []
not_error = False
#error_names
syn = Fore.RED + "Syntax error!"
syn2 = Fore.RED + "Синтаксическая ошибка"
nam = Fore.RED + "Name error!"
nam2 = Fore.RED + "Именная ошибка!"
zero = Fore.RED + "Error - divison by zero!"
zero2 = Fore.RED + "Ошибка - деление на ноль!"
id = Fore.RED + "Identation error!"
tab = Fore.RED + "Tab error!"
inc = Fore.RED + "Incorrect name!"
inc2 = Fore.RED + "Неправильное имя!"

def printlocate():
	print(Fore.YELLOW + locate)
varloc = "var/"
diskloc = "disk/"
inputname = "Name: "
inputvalue = "Value: "

def add_tool():
	name = input("Name: ")
	code = ""
	while True:
			c = input()
			if c == "end":
				break
			if c == "clear" or c == "*":
				code = ""
				system('clear')
				print(Fore.YELLOW + locate)
				print("tool")
			else:
				code += c
	tools.append([name, code])
def use_tool():
	for d in tools:
		if i == d[0]:
			not_error = True
			try:
				exec(d[1])
			except SyntaxError:
				if lang == "eng":
					print(syn)
				else:
					print(syn2)
			except NameError:
				if lang == "eng":
					print(nam)
				else:
					print(nam2)
			except ZeroDivisionError:
				if lang == "eng":
					print(zero)
				else:
					print(zero2)
			except IdentationError:
				print(id)
			except TabError:
				print(tab)
def game():
	cash = 0
	max = 20
	level = 1
	while True:
		o = input()
		if o == "end":
			break
		if randint(0, 50) == 0:
			minus = cash / 4
			cash -= minus
			print(Fore.RED + "-" + str(minus) + "$")
		if o == "up":
			if cash > level * 200 - 1:
				cash -= level * 200
				max *= 2
				level *= 2
			else:
				print(Fore.RED + "money is not enough!")
		if cash < 0:
			cash *= 1.25
		cash += randint(5, max)
		print(str(cash) + "$")
while True:
	not_error = False
	printlocate()
	i = input()
	if(locate == m + varloc):
		locate = m + varloc
		if lang == "eng":
			name = input(inputname)
			value = input(inputvalue)
		else:
			name = input("Имя: ")
			value = input("Значение: ")
		try:
			exec(name + " = " + str(value))
		except IndentationError:
			pass
		except NameError:
			if lang == "eng":
				print(inc)
			else:
				print(inc2)
		except SyntaxError:
			if lang == "eng":
				print(inc)
			else:
				print(inc2)
	if(i == "disk" or i == "диск"):
		locate = m + diskloc
	elif(i == "back" or i == "назад"):
		locate = m
	elif(i == "lang=rus"):
		lang = "rus"
		print("язык переключён на русский")
	elif(i == "lang=eng"):
		lang = "eng"
		print("language = english")
	elif(i == "var"):
		locate = m + "var/"
		if lang == "eng":
			name = input(inputname)
			value = input(inputvalue)
		else:
			name = input("Имя: ")
			value = input("Значение: ")
		try:
			exec(name + " = " + str(value))
		except IndentationError:
			pass
		except NameError:
			if lang == "eng":
				print(inc)
			else:
				print(inc2)
		except SyntaxError:
			if lang == "eng":
				print(inc)
			else:
				print(inc2)
	elif(i == "getvar"):
		if lang == "eng":
			name = input(inputname)
		else:
			name = input("Имя: ")
		try:
			exec("print(" + name + ")")
		except NameError:
			if lang == "eng":
				print("variable " + name + " is not defined!")
			else:
				print("переменной " + name + " не существует")
	elif(i == "clear" or i == "*" or i == "cleat"):
		system('clear')
	elif(i == "run" or i == "rum" or i == "rub"):
		code = ""
		while True:
			c = input()
			if c == "end":
				break
			if c == "clear" or c == "*":
				code = ""
				system('clear')
				print(Fore.YELLOW + locate)
				print("run")
			else:
				code += c + "\n"
		try:
			exec(code)
		except SyntaxError:
			if lang == "eng":
				print(syn)
			else:
				print(syn2)
		except NameError:
			if lang == "eng":
				print(nam)
			else:
				print(nam2)
		except ZeroDivisionError:
			if lang == "eng":
				print(zero)
			else:
				print(zero2)
		except TabError:
			print(tab)
		except IdentationError:
			print(id)
	elif(i == "kill"):
		kill()
	elif(i == "random"):
		if lang == "eng":
			min = input("Min: ")
			max = input("Max: ")
		else:
			min = input("Минимум: ")
			max = input("Максимум: ")
		print(randint(int(min), int(max)))
	elif(i == "tool"):
		add_tool()
	elif(i == "game"):
		game()
        elif(i == "pc game"):
                box_game()
	else:
		use_tool()
		if not_error == False:
			if lang == "eng":
				print(Fore.RED + "command " + str(i) + " is not defined!")
			else:
				print(Fore.RED + "команды " + str(i) + " не существует")
