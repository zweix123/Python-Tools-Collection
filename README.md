# Python-Tools-Collection
Gadgets written in Python

# export.py
+ 用处：批量自动导出由typora编辑的`.md`导出为`.pdf`
+ 预备：需要下载pyautogui库：命令行运行`pip install pyautogui`
+ 使用：在要批量导出的`.md`文件中新建`.py`文件，将代码复制进去，运行，然后电脑会一个个的把这个文件夹下的`.md`文件导出（时间可能比较长，但是全自动，可以去拉个屎）
+ 原理：利用pyautogui模拟手动点击的过程
+ 注意：比如软件打开、typora导出的时间代码开始有个变量表示，我这里设置等待3秒，可修改，不建议太短（我也没咋测试）
