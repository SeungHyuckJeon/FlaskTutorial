from flask import Flask, render_template, request

# Create Flask Entity Instant
app = Flask(__name__)

def plus():
    return 1+1

@app.route('/',methods=('GET','POST')) #접속하는 URL
def index():
    #get/post 요청 분기
    if request.method == "POST":
        user = request.form.get('user')
        data = {'level':60,'point':360,'exp':45000}
        return render_template('index.html',user=user,data=data)
    elif request.method=='GET':
        user = request.args.get('user')
        data = {'level':60,'point':360,'exp':45000}
        return render_template('index.html',user=user,data=data)

if __name__ == "__main__":
    app.run(debug=True)
    # host 등을 직접 지정하고 싶다면
    # app.run(host="127.0.0.1", port="5000", debug=True)
