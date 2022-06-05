# Downloads-Folder-Organization
Python can automatically sort files inside your downloads folder so you can spend less time searching/organizing and get back to what is important! Browsing the web and downloading more stuff!

These instructions are only for windows!

1) Change the drive letter and username to match yours in main.py
![2022-06-05 12_43_06-Book1 - Excel](https://user-images.githubusercontent.com/99138808/172061153-23015864-ab57-4462-bc6a-dc04743856f8.png)


2) If desired, change the folder names in utilities.py
![2022-06-05 12_43_51-DocumentsControl – utilities py](https://user-images.githubusercontent.com/99138808/172061204-b6bff825-4d52-4098-8609-f2b13d302f0e.png)


***If you know how to make an .exe of the .py files, you can skip to step 7!***

3) Once files are saved, open up the directory you saved the .py files inside of the terminal. 
   Easily done by right clicking inside of your folder, and 'Open in Terminal'.


4) Install pyinstaller using pip
   'pip install pyinstaller'
![2022-06-05 12_17_15-](https://user-images.githubusercontent.com/99138808/172061282-3dc0ec66-3c60-44c6-9501-76a8fd3a29c2.png)


5) Using pyinstaller, create a single .exe!
   'pyinstaller --onefile main.py'
![2022-06-05 12_17_52-](https://user-images.githubusercontent.com/99138808/172061326-ec595c4b-f53d-4c3a-8b1b-fcf6f792c27f.png)


6) With pyinstaller done, a 'dist' folder will be created in the folder you started in. Inside, is the main.py turned into main.exe!
![2022-06-05 12_50_51-dist](https://user-images.githubusercontent.com/99138808/172061436-8a0b29d7-66d9-44b7-b0f4-0d921e7a6406.png)


7) Click the 'Start Button' and search for 'Task Scheduler' and open.
![2022-06-05 10_07_42-Settings](https://user-images.githubusercontent.com/99138808/172061521-1d186773-585c-45a6-975f-7c6f325394c2.png)


8) Inside of task scheduler, click 'Create Basic Task' 
![2022-06-05 10_03_07-Settings](https://user-images.githubusercontent.com/99138808/172061626-6c4bcd95-dbd9-4b81-82eb-56990c405e65.png)


9) Name your task and give yourself a description of the task, then click next.
![2022-06-05 10_04_10-Create Basic Task Wizard](https://user-images.githubusercontent.com/99138808/172061646-91ea9d3a-8ca4-4ac0-bc13-55bdf30c5236.png)


10) For the trigger, select 'When the computer starts' or 'When I log on' and click next.
![2022-06-05 10_04_53-Create Basic Task Wizard](https://user-images.githubusercontent.com/99138808/172061667-19bd0fbf-fa38-47dc-82b2-510de68f5461.png)


11)








