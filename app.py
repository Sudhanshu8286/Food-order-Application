from flask import Flask, render_template
import database as db
db.createtable()

#here flask is module and flask is the class of the module

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html')

@app.route("/contactus")
def contactus():
    return render_template('contactus.html')    

@app.route("/flist")
def flist():
    foodlist= db.getall() 
    return render_template("foodlist.html",foodlist=foodlist)   

from flask import request, url_for,redirect

@app.route("/addfood",methods=['GET','POST'])
def addfood():
    if request.method=='GET':
        return render_template("foodform.html")
    elif request.method=='POST':
        #here we fetch the data from form #
        fname = request.form['foodName']
        fprice = request.form['foodPrice']
        fdes = request.form['foodDescription']
        #here we insert that data into database
        db.insert(fname,fprice,fdes)
        #after  insert we redirect our request to flist function
        return redirect(url_for('flist'))

@app.route("/deletefood/<int:id>",methods=['POST','GET'])  
def delete(id):
    if request.method=='GET':
        food= db.searchbyId(id)
        return render_template('comfirm.html',food=food)
    elif request.method=='POST':
        db.delete(id)
        return redirect(url_for('flist'))

@app.route("/updatefood/<int:id>",methods=['POST','GET'])
def updatefood(id):
    if request.method=='GET':
        #here we fetch food from database using id
        food =  db.getfoodbyid(id)
        #here we pass that food to form in tuple format
        return render_template('updatefood.html',food=food)
    elif request.method=='POST':
        #here we fetch the data from form 
        fid = request.form['foodId'] 
        fname = request.form['foodName']
        fprice = request.form['foodPrice']
        fdes = request.form['foodDescription']
        #here we insert that data into database
        db.update(fid,fname,fprice,fdes)
        #after insert we redirect our request to flist function
        return redirect(url_for('flist'))   



if __name__=='__main__':
    app.run(debug=True)

















