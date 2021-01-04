from googlesearch import search
import time
import threading
import queue
import ftplib
FTP_USER = "anonymous"
FTP_PASS = ""
list_of_websites  = queue.Queue()
print_lock = threading.Lock()
#Create a list of FTP Sites and put it in a queue
query = "inurl:ftp -inurl:(http|https)"
print("Websites we are going to check are :")
for i in search(query,tld="com",num=20,stop=20,pause=2):
    list_of_websites.put(i)
    print(i)

#This is the function that will read websites and split accordingly
def list_website_root_directory(value,x,print_lock):
    index1= value.index("//")
    first_value=value[index1+2:]
    index2=first_value.index("/")
    second_value=first_value[0:index2]
    ftp = ftplib.FTP(second_value,FTP_USER,FTP_PASS)
    ftp.encoding = "utf-8"
    print_lock.acquire()
    print("Website name is :",second_value)
    print("We are now in thread number : ",x)
    print("The Root directory of this file is for:",second_value)
    ftp.dir()
    ftp.quit()
    print()
    print_lock.release()
thread_list = []
Number_of_threads=3
while (list_of_websites.empty()!=True):
    t = threading.Thread(target=list_website_root_directory,  args=[list_of_websites.get(),1,print_lock])
    t1 = threading.Thread(target=list_website_root_directory, args=[list_of_websites.get(),2,print_lock])
    t2 = threading.Thread(target=list_website_root_directory, args=[list_of_websites.get(),3,print_lock])
    t3 = threading.Thread(target=list_website_root_directory, args=[list_of_websites.get(),4,print_lock])
    print("FIRST THREAD STARTS :")
    t.start()
    print("SECOND THREAD STARTS :")
    t1.start()
    print("THIRD THREAD STARTS :")
    t2.start()
    print("FOURTH THREAD STARTS :")
    t3.start()
    t.join()
    print("FIRST THREAD IS OVER ")
    t1.join()
    print("Second THREAD IS OVER ")
    t2.join()
    print("Third THREAD IS OVER ")
    t3.join()
    print("FOURTH THREAD IS OVER")
    




