#email scheduling
import smtplib
s=smtplib.SMTP("smpt.gmail.com",587)
s.startls()
s.login("brunda045@gmail.com","*********")
msg="Hi! How are you?"
s.sendmail("brunda045@gmail.com","ilmachachiya65@gmail.com",msg)
print("success")
s.quit()
