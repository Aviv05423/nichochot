from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sched, time
# from pynput.mouse import Controller as Mouse_control
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.common.exceptions import NoSuchElementException
# import chromedriver_autoinstaller
import tkinter as tk
from time import sleep
import os
from tkinter import *
import tkinter.ttk as ttk
# chromedriver_autoinstaller.install()
#
root = tk.Tk()
root.configure(background="#106030")
root.title('משו"ב אוטומטי')
root.iconbitmap(r'C:\Users\avivv\Desktop\mashov killer\mashovKiler.ico')  # לא בטוח למה צריך את הr

saveInputId = []  # list
saveInputPass = []

if os.path.isfile("saveInputId.txt"):
    with open("saveInputId.txt", "r") as f:  # f is the text file
        userIdInsert = f.read()
else:
    userIdInsert = ":תעודת זהות"

if os.path.isfile("saveInputPass.txt"):
    with open("saveInputPass.txt", "r") as f:  # f is the text file
        userInputPass = f.read()
else:
    userInputPass = ":סיסמא למשוב"

canvas = tk.Canvas(root, height=700, width=600, bg="#106030", highlightbackground="#106030")
canvas.pack()

idFrame = tk.Frame(root, bg="#106030")
idFrame.place(relx=0.14, rely=0.12, height=300, width=200)  # relwidth=0.5, relheight=0.06, relx=0.34, rely=0.1

userId = Entry(idFrame, width=20, bg="white", fg="black", font=("arial", 13,))
userId.pack()
userId.insert(0, userIdInsert)  # ":תעודת זהות"


def idCheker():
    inputId = Label(idFrame, text=userId.get(), bg="#106030", fg="white")
    inputId.pack()
    saveInputId.clear()
    saveInputId.append(userId.get())
    print(userId.get())
    idToMashov = userId.get()


printId = tk.Button(idFrame, text='לחץ לסיום כתיבת תעודת זהות', padx=30, pady=15, fg="white", bg="#1c4f2b",
                    command=idCheker)  # picture="C:\Users\avivv\Downloads\logo_students.png", command=masov()
printId.pack()

passFrame = tk.Frame(root, bg="#106030")
passFrame.place(relx=0.54, rely=0.12, height=300, width=200)

userPass = Entry(passFrame, width=20, bg="white", fg="black", font=("arial", 13))
userPass.pack()
userPass.insert(0, userInputPass)  # ":סיסמא למשוב"


def passCheker():
    inputPass = Label(passFrame, text=userPass.get(), bg="#106030", fg="white")
    inputPass.pack()
    saveInputPass.clear()
    saveInputPass.append(userPass.get())
    print(userPass.get())


printPass = tk.Button(passFrame, text='לחץ לסיום כתיבת סיסמא', padx=30, pady=15, fg="white", bg="#1c4f2b",
                      command=passCheker)  # picture="C:\Users\avivv\Downloads\logo_students.png", command=masov()
printPass.pack()


# userId=Label(root, text="תעודת זהות")
# entryUserId=Entry(root)
def minemasov():
    # option = webdriver.ChromeOptions();
    # option.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    # options = webdriver.ChromeOptions()  # פיתחת כרום דרך משתמש רגיל
    # options.add_argument("user-data-dir=C:\\Users\\avivv\\AppData\\Local\\Google\\Chrome\\User Data 3")
    # brozer = webdriver.Chrome(executable_path=r"C:\Users\avivv\Documents\chromedriver.exe", options=options)


    brozer = webdriver.Chrome()#chrome_options=opt)
    #
    # options = webdriver.ChromeOptions()
    # פיתחת כרום דרך משתמש רגיל
    # options.add_argument("user-data-dir=C:\\Users\\avivv\\AppData\\Local\\Google\\Chrome\\User Data")
    #
    # brozer = webdriver.Chrome(executable_path=r"C:\Users\avivv\Documents\chromedriver.exe", options=options)
    #
    brozer.get("https://web.mashov.info/students/login")

    time.sleep(0.2)  # 3

    select_school = brozer.find_element_by_id("mat-input-3")
    select_school.click()
    select_school.send_keys("440198")
    select_school.send_keys(Keys.ENTER)

    taz = brozer.find_element_by_xpath("//*[@id=\"mat-input-0\"]")
    taz.send_keys(saveInputId)

    passw = brozer.find_element_by_xpath("//*[@id=\"mat-input-4\"]")
    passw.send_keys(saveInputPass)

    login_button = brozer.find_element_by_xpath("//*[@id=\"mat-tab-content-0-0\"]/div/div/button[1]")
    login_button.click()

    time.sleep(4)  # 4

    def go_to_o_class_tab():
        # מעבר לעמוד הכיתה המכוונת
        try:
            # time.sleep(5)
            brozer.get('https://web.mashov.info/students/main/students/554114ac-058c-44e1-899b-272866932d52/bbb')
            # browser.refresh()
        except:  # מה לעשות במידה ויש שגיאה (העמוד לא נטען)
            ## מעבר לעמוד הכיתה המכוונת אופציה ב'
            hamburger_menu = brozer.find_element_by_class_name("mat-button-wrapper")
            hamburger_menu.click()
            time.sleep(0.5)
            # online_class_button = browser.find_element_by_class_name("ng-tns-c394-1")
            online_class_button = brozer.find_element_by_xpath('//*[@title="כיתה מקוונת"]')
            online_class_button.click()
        else:
            pass

    def disable_loading_circle():
        # מעבר לעמוד הכיתה המקוונת
        try:
            sleep(0.2)  # 5
            loading_circle = brozer.find_elements_by_xpath(
                "//*[@id=\"mainView\"]/mat-sidenav-content/mshv-student/mshv-student-bbb/mat-card[2]/mat-card-title/h1/button/span[1]/spann")
            print("הצלחתי דרך קשור")

            # browser.refresh()
        except:  # מה לעשות במידה ויש שגיאה (העמוד לא נטען)
            brozer.close()
            minemasov()
        else:
            pass

    # go_to_o_class_tab()
    # brozer.get('https://web.mashov.info/students/main/students/554114ac-058c-44e1-899b-272866932d52/bbb')
    # brozer.get('https://web.mashov.info/students/main/students/554114ac-058c-44e1-899b-272866932d52/bbb')
    brozer.get('https://web.mashov.info/students/main/students/554114ac-058c-44e1-899b-272866932d52/bbb')
    disable_loading_circle()
    # go_to_o_class_tab()

    sleep(0.2)  # 2

    # def lesen_checer():
    #     global lesonlink
    #     first_lesson_on_column = brozer.find_element_by_xpath('//*[@id="mainView"]/mat-sidenav-content/mshv-student/mshv-student-bbb/mat-card/mat-nav-list/a[1]/div/div[1]')
    #     actions1.perform()
    #     lesonlink = [my_elem.get_attribute("href") for my_elem in brozer.find_elements_by_xpath("//*[@id=\"mainView\"]/mat-sidenav-content/mshv-student/mshv-student-bbb/mat-card/mat-nav-list/a[1]")]
    #     print(lesonlink)

    global first_lesson_on_column
    sleep(0.2)  # 4

    # lesen_checer()
    def empty_lessons_coming():
        try:
            first_lesson_on_column = brozer.find_element_by_xpath(
                '//*[@id="mainView"]/mat-sidenav-content/mshv-student/mshv-student-bbb/mat-card/mat-nav-list/a[1]/div/div[1]')
            # first_lesson_on_column.click()
            print("נכנס לשיעור")
        except:
            print("אין שיעורים באופק, תהנה")
            sleep(60 * 60 * 3)  # 3 Hours
            empty_lessons_coming()

    empty_lessons_coming()
    actions1 = ActionChains(brozer)
    first_lesson_on_column = brozer.find_element_by_xpath(
        '//*[@id="mainView"]/mat-sidenav-content/mshv-student/mshv-student-bbb/mat-card/mat-nav-list/a[1]/div/div[1]')
    actions1.click(first_lesson_on_column)
    actions1.perform()
    lesonlink = [my_elem.get_attribute("href") for my_elem in brozer.find_elements_by_xpath(
        "//*[@id=\"mainView\"]/mat-sidenav-content/mshv-student/mshv-student-bbb/mat-card/mat-nav-list/a[1]")]
    print(lesonlink)

    sleep(0.2)  # 1
    print(brozer.title + "כותרת אתר")

    brozer.switch_to.window(brozer.window_handles[1])
    # popins = brozer.current_window_handle
    # chaing_to_open_tub = brozer.window_handles
    # sleep(4)
    # for w in chaing_to_open_tub:
    #     if (w != popins):
    #         brozer.switch_to.window(w)
    print(brozer.session_id + "כותרת אתר")

    # print("vhh")
    sleep(0.2)  # 4

    def conect_to_class():
        try:
            # brozer.find_elements_by_tag_name("span")
            brozer.find_element_by_id("xml-viewer-style")
            print("הדף רוענן לבדיקת שיעור")
            sleep(5 * 60)
            brozer.refresh()
            conect_to_class()
        except:
            print("מתחיל שיעור אונליין")
    sleep(10)
    microfon = brozer.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/span/button[2]/span[1]")
    microfon.click()

    chat = brozer.find_element_by_xpath("//*[@id=\"message-input\"]")
    chat.send_keys("אני פה איו לי מיקרופון")
    # sleep(10)
    # microfonTest = brozer.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/span/button[1]/span[1]")
    # microfonTest.click()
    # sleep(6)
    # microfonOFF = brozer.find_element_by_xpath("//*[@id=\"app\"]/main/section/div[1]/section[2]/div/div[2]/span")
    # microfonOFF.click()
    sleep(60 * 60)  # 60*60
    brozer.quit()
    minemasov()

    conect_to_class()
    sleep(0)  # 4


def close_root():
    root.destroy()


def openMashovAndClosPopUp():
    close_root()
    minemasov()


# entryUserId.grid(row=0,column=1)
# buttonUserId.grid(row=1,column=0)

mashovFrame = tk.Frame(root, bg="#106030")
mashovFrame.place(relx=0.34, rely=0.62, height=80, width=200)

startMashov = tk.Button(mashovFrame, text='הפעלת משו"ב', padx=30, pady=15, fg="white", bg="#1c4f2b",
                        command=openMashovAndClosPopUp)  # picture="C:\Users\avivv\Downloads\logo_students.png", command=masov()
startMashov.pack()

root.mainloop()

if saveInputId == []:
    pass
else:
    with open("saveInputId.txt", "w") as f:  # f is the text file
        for saveInputId in saveInputId:
            f.write(str(saveInputId))

if saveInputPass == []:
    pass
else:
    with open("saveInputPass.txt", "w") as f:
        for saveInputPass in saveInputPass:
            f.write(str(saveInputPass))

# with open(file_name + '.txt', 'w') as file_object:
#     file_object.write(file_name)
# with open(file_name + '.txt', 'w') as f:
#     f.write(file_name)

