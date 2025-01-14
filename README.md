# email-api
This is an simple email api which I built to verify user's for my platform Cohortize using OTP auth method, it takes data in json format with three fields namely - name, email, and password. As it uses the standard python library smtplib to send mails, its free of cost!

Let's start with the steps to use it - 
Firstly, Clone the repo
'''git clone https://github.com/Manan-Coder/email-api'''

After that install Flask by running - 
'''pip install flask'''

After that enter your email id(from which you want to send mails) and a specific app password for it(I will not have access to your app password, this is a poor 20 line api,you'll have to enter it as python lib smtplib uses it :) in the code where marked, then you are good to go. Just run the program.

To test it, you can use tools like postman or curl, or even connect it to your frontend to make a working signup page.
Thanks for reading!
