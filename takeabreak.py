import time
import tkMessageBox
import webbrowser

total = 4
count = 1
print ("The program has started on" + time.ctime())
vid = raw_input("Enter link for break time (Enter without https or www):	")

while(count < total+1) :
	remain = total - count
	time.sleep(7200)
	tkMessageBox.showinfo("Break Alert", "Time to take a little break.")
	webbrowser.open("https://www." + vid)
	print "Break(s) left:", remain
	count+= 1
