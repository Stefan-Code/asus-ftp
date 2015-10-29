#!/usr/bin/python3
"""
Python 3 script to collect statistics about the asus ftp desaster.
This may be used for statistical purposes only!
"""
import ftplib
import socket
import sys
from multiprocessing.dummy import Pool as ThreadPool
from threading import Lock

# Configuration
num_workers = 64
#ips seperated by commas like so: 127.0.0.1, 127.0.0.2, 127.0.0.3
ip_file = "ips.txt"
#open ips get written there
results_file = "results.txt"

def allows_anonymous_login(ip):
    """
    returns True if ip allows anonymus ftp logins
    """
    ftp = ftplib.FTP()
    try:
        ftp.connect(ip, 21, 3)
        ftp.login()
        return True
    except socket.error:
        return False
    except ftplib.error_temp:
        return True
    except EOFError:
        return False
    except ftplib.error_perm:
        return False


ips = []
with open(ip_file, "r") as f:
    contents = f.read()
    ips = [ip.strip() for ip in contents.split(",")]
total = len(ips)
avail, processed = (0, 0)
lock = Lock()
pool = ThreadPool(num_workers)
print(total, "ips in list")

def info_allows_anonymous_login(ip):
    """
    Ugly global use, but it works :)
    Print stuff needed in here because of threads
    """
    global processed
    global avail
    global total
    if allows_anonymous_login(ip):
        lock.acquire()
        avail += 1
        processed += 1
        sys.stdout.write(str(processed) + "/" + str(total) + " ("+ str(avail) + "/" + str(total) + ")\r")
        sys.stdout.flush()
        lock.release()
        return (ip, True)
    else:
        processed += 1
        return (ip, False)


results = pool.map(info_allows_anonymous_login, ips)
pool.close()
pool.join()
with open(results_file, "w") as f:
    for result in results:
        if result[1]:
            f.write(result[0]+"\n")
print("                             ")  # needed to clean up mess left behind in the terminal sometimes
print("done.")
print(avail, "of", total, "open")
