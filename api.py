from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route("/api/signup", methods=['POST'])
def signup_api():
    data = request.get_json()
    name  = data.get('name')
    email = data.get('email')
    passw = data.get('password')
    if not name or not email or not passw:
        return jsonify({'error': 'Missing data'}), 400
    print(data)
    import smtplib
    from email.mime.text import MIMEText
    import random
    OTP = random.randint(1000, 9999)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    email_from = "your email address"
    email_password = "your app password"
    email_to = email
    msg = MIMEText(f'{OTP} is OTP for xyz,Enjoy:)')
    msg['Subject'] = f'<No-Reply>{OTP} is OTP for xyz'
    msg['From'] = email_from
    msg['To'] = email_to
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(email_from, email_password)
        server.sendmail(email_from, [email_to], msg.as_string())
        return jsonify({'message': 'Email sent!'})
if __name__ == '__main__':
    app.run(debug=False  )
