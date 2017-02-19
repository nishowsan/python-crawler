# the modules to be used
import requests
import tkinter.messagebox
from tkinter import *
from bs4 import BeautifulSoup
# the main window variable
root = Tk()

# function built for exiting
def exit_sys():
    root.quit()
# the about at main menu
def about():
    tkinter.messagebox.showinfo('crawler' ,"a crawler that crawls stack over flow ,by adib")
# the help at main menu
def help():
    tkinter.messagebox.showinfo('crawler' ,"just press the crawl button & see the magic")
# the main function
# the crawler's start point
url_s = input('enter url : ')
url = str(url_s)
def Crawl():
    print("1 = title")
    print("2 = href")
    print("href means links")
    choice = input('enter what do want to crawl :')
    if choice is '1':
        x = 'title'
    elif choice is '2':
        x = 'href'
    else:
        print("invalid option")
    request = requests.get(url)
    plain_text = request.text
    soup = BeautifulSoup(plain_text ,'html.parser')
    for link in soup.find_all('a'):
        title = link.get(x)
        print(title)
# the main menu
menu = Menu(root)
root.config(menu=menu)
submenu = Menu(menu)
menu.add_cascade(menu=submenu ,label='file')
submenu.add_command(label='about' ,command=about)
submenu.add_command(label='help' ,command=help)
submenu.add_separator()
submenu.add_command(label='exit' ,command=exit_sys)
# the label of the main window
label = Label(root ,text='this is py crawler GUI' ,bg='green' ,fg='black')
label.pack(side=TOP ,fill=X)
# the buttons functions
button1 = Button(root ,text='crawl' ,command=Crawl)
button1.pack(padx=2 ,pady=2)
button2 = Button(root ,text='exit' ,command=exit_sys)
button2.pack(padx=2 ,pady=2)
# the final program
root.mainloop()
# end of coding