import smtplib
import webbrowser
import time


def spammer():
        ##
        print("This Works only with gmail")
        fromg = input("Your email:")
        passg = input("Your password:")
        ##
        
        tog = input("TO:")
        
        try:
            print ("Connecting to the server...")
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.login(fromg, passg)
        
            mess = input("What message? ")
            times = int(input("How much times: "))
            
            i = 1
            while i<=times:
                print("Message {} sended".format(i))
                server.sendmail(fromg, tog, mess)
                i = i + 1
                
            server.quit
            
            print ("Created by Yordan Stoychev")
        except:
            print("Something went wrong")
        


           
spammer()

