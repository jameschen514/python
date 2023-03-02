import threading

def func1():
    buffet = ("Crispy Tofu", "Pho", "Pad Thai", "Green curry", "Pa Kim Mao")
    for food in buffet:
    	print(food)

#buffet[0] = "Carbonated beverages"
    
print()		



def func2():
    buffet = ("Tom yum", "Crispy duck", "Pad Thai", "Green curry", "Pa Kim Mao")
    for food in buffet:     
    	print(food)

thread1 = threading.Thread(target=func1)
thread2 = threading.Thread(target=func2)


thread1.start()
thread2.start()

thread1.join()
thread2.join()