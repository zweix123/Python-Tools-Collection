import os
import time
import pyautogui

Time_wait = 3

def export():  #typora软件自动导出
    #文件(E):(25, 35)
    pyautogui.moveTo(25, 35, duration=1)
    pyautogui.click(button='left')
    #导出:(.., 555)
    pyautogui.moveTo(25, 555, duration=1)
    #html:(480,..)
    pyautogui.moveTo(480, 555, duration=1)
    #pdf:(.., 525)
    pyautogui.moveTo(480, 525, duration=1)
    pyautogui.click(button='left')
    #保存:(620, 660)
    #这里不知道保存窗口弹出要多久，所以保留的时间多一点
    pyautogui.moveTo(620, 660, duration=Time_wait)
    pyautogui.click(button='left')
    #导出需要时间，这里停留几秒
    sizex, sizey = pyautogui.size()
    pyautogui.moveTo(sizex / 2, sizey / 2, duration=Time_wait)

def work(files):
    for file in files:
        #打开文件
        os.startfile(file)
        #等待几秒它打开
        time.sleep(Time_wait)
        export()  #开始导出
        #热键关闭
        pyautogui.hotkey('altleft', 'f4')


if __name__ == '__main__' :
    
    #获得当前文件夹下的文件
    files = os.listdir()
    #取出不是.md的文件（主要是当前这个py文件）
    for file in files: 
        if os.path.splitext(file)[-1] != '.md':
            files.remove(file)
    #查看是否正确
    # print(files)

    work(files)
    #好，现在你运行这个脚本就可以去拉屎了，回来的时候基本就可以了。