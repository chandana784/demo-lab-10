from flask import Flask

app=Flask(__name__)
@app.route("/")
def home():
    "hello docker is running"
    return 
    
if __name__=="__main___":
    app.run(host="0.0.0.0",port=5000)
