#Importing libraries, packages
import random
import smtplib
import re

#Setup smtp server config
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
senderEmail = "Enter_Your_Email_Address"
senderAppPassword = "Enter_Your_App_Password_Key_For_Access" #Generate from https://myaccount.google.com/apppasswords section
server.login(senderEmail,senderAppPassword)

#Functions
def emailVerification(emailId):
    emailPattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$')

    if not emailPattern.match(emailId):
        print("Invalid email id")
        emailId = input("Enter correct email id: ")
        return emailVerification(emailId)
    
    return emailId

def generateOTPMessage(otp):
    body = "Dear user, your 6 digit OTP is "+str(otp)+"."
    subject = "Otp Verification Service"
    message = f'subject:{subject}\n\n{body}'
    return message

def generateOtp():
    newOtp = random.randint(100000,999999)
    return newOtp

def sendEmail(senderEmail,receiverEmail,message):
    server.sendmail(senderEmail,receiverEmail,message)

def verifyOtp(otp):
    receivedOtp = int(input("Please Enter OTP: "))
    
    if receivedOtp == otp:
        print("OTP verified")
        return 1
    else:
        print("Invalid OTP")
        return 0
    
def closeServer():
    server.quit()

def verification():
    emailInput = input("Enter your email id: ")
    receiverEmail = emailVerification(emailInput)
    newOtp = generateOtp()
    emailBody = generateOTPMessage(newOtp)
    sendEmail(senderEmail,receiverEmail,emailBody)
    verificationStatus = verifyOtp(newOtp)
    while(verificationStatus != 1):
        verificationStatus = verifyOtp(newOtp)
    closeServer()

#Program Entry Point
verification()
