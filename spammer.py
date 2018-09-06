import smtplib
import webbrowser
import time


def spammer():
        ##
        print("This Works only with gmail")
        fromg = input("Your email:")
        passg = input("Your password:")
        ##
        print("TO: (when you are done with adding emails type end.)")
        a = 0
        z = 1
        top = []
        while z==1:
            to = input()
            if(to=="end"):
                z = 0
                break
            top.append(to)
            a  = a + 1
        
        try:
            print ("Connecting to the server...")
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.login(fromg, passg)
        
            mess = input("What message? ")
            times = int(input("How much times:(on every user) "))
            
            i = 1
            b = 0
            while i<=times:
                while b<a:
                    tog = top[b]
                    print(tog)
                    server.sendmail(fromg, tog, mess)
                    print("Message {} sended".format(i))
                    
                    b = b + 1
                if(b>=a):
                    i = i + 1
                    b = 0
                
                
            server.quit
            
            print ("Created by Yordan Stoychev")
        except:
            print("Something went wrong")
        


           
spammer()

