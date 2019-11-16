import socket
import webbrowser
import time
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def open_google_dorks(url, search_google, time_delay):
    webbrowser.open_new_tab(search_google + url + " -www")
    time.sleep(time_delay)
    webbrowser.open_new_tab(search_google + url + " intitle:\"test\" -support")
    time.sleep(time_delay)
    webbrowser.open_new_tab(search_google + url + " ext:php|ext:html")
    time.sleep(time_delay)
    webbrowser.open_new_tab(search_google + url + " inurl:auth")
    time.sleep(time_delay)
    webbrowser.open_new_tab(search_google + url + " inurl:dev")

    print("test")


print("Hello Saby")

os.system("masscan 52.17.227.174 -p80,81-8000 > tmp")
print("IP Address - " + socket.gethostbyname("netflix.com"))
search_google = "www.google.com/search?q=site:"
time_delay = 5
f = open("/hack/recon/scratch.txt", "r")
for url in f:
    print("test")
    #open_google_dorks(url, search_google, time_delay)

f.close()