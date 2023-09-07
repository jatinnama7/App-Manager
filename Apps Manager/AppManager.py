import simple_colors as color

import os
import time
import sys
import simple_colors as color
from plyer import notification

# Record the start time
start_time = time.time()

print(color.red('WELCOME TO JATINS PORTAL !!\nWhat would  you like to access--> '))
time.sleep(2)
options = ["1. Browser", "2. Live Stream", "3. Notepad", "4. OS apps", "5. Drives","6. Fetch URL"]

for i in options:
    print(color.blue(i))

opt = int(input(color.green("\nSelect your option:\n")))

# --------------------------------------- BROWSERS -------------------------------------------
if opt == 1:
    print(color.red(f"Select the browser: "))
    browsers = ["1.Chrome" , "2.Microsoft Edge"]
    for i in browsers:
        print(color.magenta(i))

    opt1 = int(input("\n Select your option:\n"))
    if(opt1==1):
        a = float(input(color.blue("Enter the time in minutes for closing chrome: ")))
        b = a*60
        notification.notify(
        title="Notifications:",
        message="Opening Chrome",
        timeout=2,
        app_icon="gc1.ico") # Provide your directory
        time.sleep(2)
        os.system("Start chrome")
        time.sleep(b)
        os.system(f"taskkill /f /im chrome.exe")
        
    elif(opt1==2):
        a = float(input(color.blue("Enter the time in minutes for closing edge: ")))      
        b = a*60
        notification.notify(
        title="Notifications:",
        message="Opening Edge",
        timeout=2,
        app_icon="eb.ico") # Provide your directory
        time.sleep(2)
        os.system("Start msedge")
        time.sleep(b)
        os.system("taskkill /f /im msedge.exe")

# --------------------------------------- LIVE STREAM -------------------------------------------
elif opt == 2:
    print(color.red(f"Select the Live stream app:"))
    print(color.magenta("(LIVE STREAM APPS):\n"),color.red("1.Loco\n 2.Vimeo"))
    opt2 = int(input("\n Select your option:\n"))
    if(opt2==1):
        a = float(input(color.blue("Enter the time in minutes for closing loco: ")))       
        b = a*60
        notification.notify(
        title="Notifications:",
        message="Opening Loco",
        timeout=2,
        app_icon="l.ico") # Provide your directory
        time.sleep(2)
        os.system("Start chrome https://loco.gg")
        time.sleep(b)
        os.system("taskkill /f /im chrome.exe ")

    elif(opt2==2):
        a = float(input(color.blue("Enter the time in minutes for closing vimeo: ")))        
        b = a*60
        notification.notify(
        title="Notifications:",
        message="Opening Vimeo",
        timeout=2,
        app_icon="vm.ico")
        time.sleep(2)
        os.system("Start chrome https://livestream.com")
        time.sleep()
        os.system("taskkill /f /im chrome.exe ")

# --------------------------------------- NOTEPAD -------------------------------------------
elif opt == 3:

    a = float(input(color.blue("Enter the time in minutes for closing notepad: ")))
    b = a*60
    notification.notify(
        title="Notifications:",
        message="Opening Notepad",
        timeout=2,
        app_icon="np.ico")
    time.sleep(2)
    os.system("start notepad")
        
    time.sleep(b)
    os.system("taskkill /f /im notepad.exe")

# --------------------------------------- OS APPS -------------------------------------------
elif opt == 4:
    print(color.red(f"Select the app: "))
    print(color.magenta("(APPS):\n"),color.red("1.PAINT\n 2.Microsoft calculator"))
    opt1 = int(input("\n Select your option:\n"))
    if(opt1==1):
        a = float(input(color.blue("Enter the time in minutes for closing paint: ")))       
        b = a*60
        notification.notify(
        title="Notifications:",
        message="Opening Paint",
        timeout=2,
        app_icon="pt.ico")
        time.sleep(2)
        os.system("Start mspaint")
        time.sleep(b)
        os.system(f"taskkill /f /im mspaint.exe")

    elif(opt1==2):
        a = float(input(color.blue("Enter the time in minutes for closing calculator: ")))
        b = a*60
        notification.notify(
        title="Notifications:",
        message="Opening Calculator",
        timeout=2,
        app_icon="cal.ico")
        time.sleep(2)
        os.system("Start Calculator.exe")
        time.sleep(b)
        os.system("taskkill /f /im Calculator.exe")


# --------------------------------------- DRIVES -------------------------------------------   
elif opt == 5:
    print(color.red(f"Select the Drive: "))
    print(color.magenta("(DRIVES):\n"),color.red("1.C-DRIVE \n 2.D-DRIVE"))
    opt1 = int(input("\n Select your option:\n"))
    if(opt1==1):
        a = float(input(color.blue("Enter the time in minutes for closing C-Drive: ")))
        b = a*60
        print(color.green("C-DRIVE will open now...."))
        time.sleep(2)
        os.startfile("C:")
        time.sleep(b)
        os.system(f"taskkill /f /im C:")
    elif(opt1==2):
        a = float(input(color.blue("Enter the time in minutes for closing D-Drive: ")))
        b = a*60
        print(color.green("D- DRIVE will open now...."))
        time.sleep(2)
        os.startfile("D:")
        time.sleep(b)
        os.system(f"taskkill /f /im D:")

 # --------------------------------------- URL -------------------------------------------   
elif opt == 6:

    url = input(color.blue("Enter the url you want to fetch:"))
    a = float(input(color.blue("Enter the time in minutes for closing url: ")))
    b = a*60
    time.sleep(2)
    os.system(f"start chrome {url}")
    notification.notify(
        title="Notifications:",
        message="Opening Url",
        timeout=2,
        app_icon="url.ico")
    time.sleep(b)
    os.system(f"taskkill /f /im chrome.exe")

else:
    print("The option is not present")

# Calculate and display the running time
end_time = time.time()
running_time = end_time - start_time
notification.notify(
        title="Notification ",
        message=f"Running Time:{running_time:.2f}",
        timeout=5,
        app_icon ="not.ico")
        
print(f"Running time: {running_time:.2f} seconds")


