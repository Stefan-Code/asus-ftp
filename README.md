Asus FTP desaster statistics gathering (threaded)
========================================================
About this Tool
---------------------
This script can be used to gather statistics about how many of the known routers suffering from the asus router ftp desaster (google it) are still vulnerable. **PLEASE NOTE: This tool is intended to gather statistics and may not be used to perform any illegal actions.** (Please be sure that what you're doing is legal in your country)
Requirements
-----------
To use it, create a file called `ips.txt` next to the script and fill it with the ip addresses available online (e.g. pastebin). The ips have to be seperated with a comma. The script itself does not have any external dependencies. Only tested using `python3`
Usage
----------
To run the script use `python3 asus-list.py` and it will automatically print some useful numbers to the terminal and additionally save the "vulnerable" ips to a file called `results.txt`. You can also configure stuff like file naming or thread count on the top of the script.

It should be quite fast because it uses many threads simultaneously to test the ips. Speed is about `25 ips/s` for me. You can also try to increase the number of threads to tune this further.
Windows systems
-----------
Not sure if the status printing will work properly in windows. Would be cool if someone could verify this.
