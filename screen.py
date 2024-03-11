import pyscreenshot
import socket 
import threading 
import time
from datetime import datetime
from tkinter import *




def screen_shot():
	while True:
		image = pyscreenshot.grab()
		cur_time = datetime.now().strftime('%b-%d-Time-%I-%M-%S')
		
		filename = cur_time + '.png'
		image.save('/root/Desktop/PROJECTS/ScreenShot_python/IMG/' +filename)
		
		time.sleep(5)
def port_1():
	while True:
		def scan_port(port): 
			try: 
				host = "localhost"
				host_ip = socket.gethostbyname(host) 
				status = False

				# create instance of socket 
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

				# connecting the host ip address and port 
				s.connect((host_ip, port)) 
				try: 
					banner = s.recv(1024).decode() 
					print("port {} is open with banner {}".format(port, banner)) 

				except: 
					print("port {} is open ".format(port)) 

			except: 
				pass


		start_time = time.time() 

		for i in range(0, 100000): 
			thread = threading.Thread(target=scan_port, args=[i]) 
			thread.start() 

		end_time = time.time() 
		print("To scan all ports it took {} seconds".format(end_time-start_time)) 


sp =Tk()
sp.title("Hacking Tool")
sp.geometry("300x300")
sp.config(bg="cyan")

	
button = Button(sp,text="Screen Shot",font=("Time New Roman",10,"bold"),relief=RAISED ,command=screen_shot)
button.place(x=60,y=100)	
button = Button(sp,text="Port Scan",font=("Time New Roman",10,"bold"),relief=RAISED ,command=port_1)
button.place(x=60,y=5)

sp.mainloop()
screen_shot()
port_1()
