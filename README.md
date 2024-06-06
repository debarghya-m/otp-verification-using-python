# Email Verification OTP System

This Python program provides a simple email verification system using OTP (One Time Password). It generates a 6-digit OTP and sends it to the user's email address for verification.

## Functionality

### `emailVerification(emailId)`
- Validates the format of the provided email address using regular expressions.
- If the email format is invalid, prompts the user to enter a correct email address.

### `generateOTPMessage(otp)`
- Generates a message containing the OTP to be sent via email.
- Constructs the subject and body of the email.

### `generateOtp()`
- Generates a random 6-digit OTP.

### `sendEmail(senderEmail,receiverEmail,message)`
- Sends an email containing the OTP message to the provided receiver email address using SMTP.

### `verifyOtp(otp)`
- Prompts the user to enter the OTP received via email.
- Compares the entered OTP with the generated OTP.
- Returns a status indicating whether the OTP is verified or not.

### `closeServer()`
- Closes the SMTP server connection.

### `verification()`
- Main function to initiate the email verification process.
- Takes user input for their email address.
- Verifies the email address format and generates an OTP.
- Sends the OTP via email and prompts the user to enter the OTP.
- Repeats the OTP verification process until the correct OTP is entered.
- Closes the SMTP server connection.

### `Note` 
    Please change the senderEmail and senderAppPassword variable before running the program.
    senderEmail = "Enter_Your_Email_Address"
    senderAppPassword = "Enter_Your_App_Password_Key_For_Access" 
    Generate from https://myaccount.google.com/apppasswords section