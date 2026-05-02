Set WshShell = CreateObject("WScript.Shell")
WshShell.CurrentDirectory = "C:\Repositories\gentle-windows-notifications"
WshShell.Run """C:\Users\pc\AppData\Local\Programs\Python\Python314\python.exe"" ""gentleNotifications.py""", 0, False