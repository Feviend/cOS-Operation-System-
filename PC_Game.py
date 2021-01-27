from random import*
from colorama import*
#PC Game
init(autoreset=True)
i3 = "intel core i3"
i5 = Fore.GREEN + "intel core i5"
i7 = Fore.CYAN + "intel core i7"
i9 = Fore.RED + "intel core i9"
gtx_1660 = Fore.YELLOW + "GTX 1660"
rtx_2060 = Fore.YELLOW + "RTX 2060"
ryzen_3 = "AMD ryzen 3"
ryzen_5 = Fore.GREEN + "AMD ryzen 5"
ryzen_7 = Fore.CYAN + "AMD ryzen 7"
ryzen_9 = Fore.RED + "AMD ryzen 9"

items = []

def paste(item, count):
	for x in range(0, count):
		items.append(item)
		
paste(i3, 18)
paste(ryzen_3, 20)
paste(i5, 14)
paste(ryzen_5, 16)
paste(gtx_1660, 17)
paste(rtx_2060, 13)
paste(ryzen_7, 10)
paste(i7, 6)
paste(ryzen_9, 3)
paste(i9, 2)

def box_game():
	while True:
		a = input()
		print(choice(items))
