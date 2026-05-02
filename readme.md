Needs Python installed!

Please place gentle-notifications.vbs into the windows startup folder 😺 (Win+r, "shell:startup").
Edit gentle-notifications.vbs so that the paths are that of your python.exe file and the directory where gentleNotifications.py is.


### Stopping
create a file named "stop.txt" in the folder where gentleNotifications.py is.

### Faster boot (optional)

Open Windows Task Scheduler and create a new task for opening the gentleNotifications.py script. This avoids the 5-10 seconds needed for Windows to wake up and starts the script straight away!

#### **General tab**

* Name: `Gentle Notifications 💛`
* ✔ Run with highest privileges

#### **Triggers tab**

* New →

  * Begin the task: **At log on**
  * ✔ “Delay task for”: set to **0 seconds** (important: removes that startup lag)

#### **Actions tab**

* New →

  * Program/script (use pythonw instead of python):

    ```
    C:\Users\pc\AppData\Local\Programs\Python\Python314\pythonw.exe
    ```
  * Arguments:

    ```
    C:\Repositories\gentle-windows-notifications\gentleNotifications.py
    ```
  * Start in:

    ```
    C:\Repositories\gentle-windows-notifications
    ```

#### **Conditions tab**

* ❌ uncheck “Start only if computer is on AC power” (if laptop)

#### **Settings tab**

* ✔ Allow task to be run on demand

#### **🌼 result**

Now it usually runs:

👉 **~0–2 seconds after login**