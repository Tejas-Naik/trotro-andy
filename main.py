from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/contact')
def contact_us():
   return render_template('contact.html')

@app.route('/signin')
def signin():
   return render_template('signin.html')
@app.route('/signup')
def signup():
   return render_template('signup.html')
@app.route('/faq')
def faq():
   return render_template('faq.html')
if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)