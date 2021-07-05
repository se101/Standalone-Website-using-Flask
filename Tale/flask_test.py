from flask import Flask,render_template,request
import datetime, time
import jinja2

app=Flask(__name__)
StudName=StudNum=AccBranch=AccNum=AccDesc=BankName=BankCode=BankCity=BankAdd1=BankAdd2=''


displist=[ '', ]
@app.route('/')
def function():
    import csv
    with open('C:/Projects/Tale/templates/banks.csv','r') as csvfile:
        read1=csv.reader(csvfile)
        build=list(read1)
    time1= datetime.datetime.now().timestamp()
    new_time=time.ctime(time1)
    return render_template("test_html.html",hnew_time=new_time,hbuild=build,hstudname="",hstudnum="",haccbrank="",haccnum="",hassdesc="",hbankcode="",hbankcity="",hbankadd1="",hbankadd2="",hccardnum="",hccardname="",hccardexp="",hccardcvv="",hdcardnum="",hdcardname="",hdcardexp="",hdcardcvv="",hfromacc="",hchequenum="",hcaccname="",hcbankname="",hacctype="")
# //    return render_template("test_html.html" array=  list, hnew_time=new_time,hbuild=build,hstudname="",hstudnum="",haccbrank="",haccnum="",hassdesc="",hbankcode="",hbankcity="",hbankadd1="",hbankadd2="",hccardnum="",hccardname="",hccardexp="",hccardcvv="",hdcardnum="",hdcardname="",hdcardexp="",hdcardcvv="",hfromacc="",hchequenum="",hcaccname="",hcbankname="",hacctype="")

@app.route('/', methods=['GET','POST'])

# env = jinja2.Environment(loader=jinja2.FileSystemLoader('C:/Projects/Tale/templates'))
# template = env.get_template('banks-build')
# for data in build:
#   print (template.render(data=build))

def function2():
    FormData=request.form
    StudName=request.form['StudName']
    AccBranch=request.form['AccBranch']
    AccDesc=request.form['AccDesc']
    StudNum=request.form['StudNum']
    AccNum=request.form['AccNum']
    BankName=request.form['BankName']
    BankCity=request.form['BankCity']
    BankCode=request.form['BankCode']
    BankAdd1=request.form['BankAdd1']
    BankAdd2=request.form['BankAdd2']
    CCardNum=request.form['CCardNum']
    CCardName=request.form['CCardName']
    CCardExp=request.form['CCardExp']
    CCardCVV=request.form['CCardCVV']
    DCardNum=request.form['DCardNum']
    DCardName=request.form['DCardName']
    DCardExp=request.form['DCardExp']
    DCardCVV=request.form['DCardCVV']
    FromAcc=request.form['FromAcc']
    ChequeNum=request.form['ChequeNum']
    CAccName=request.form['CAccName']
    CBankName=request.form['CBankName']
    AccType=request.form['AccType']
    print( FormData)
    time1= datetime.datetime.now().timestamp()
    new_time=time.ctime(time1)
    #  StudName , StudNum, AccBranch,AccNum,AccDesc,BankName,BankCode,BankCity,BankAdd1,BankAdd2 
    return render_template("/try.html",hnew_time=new_time,hstudname=StudName,hstudnum=StudNum,haccbrank=AccBranch,haccnum=AccNum,haccdesc=AccDesc,hbankname=BankName,hbankcode=BankCode,hbankcity=BankCity,hbankadd1=BankAdd1,hbankadd2=BankAdd2,hccardnum=CCardNum ,hccardname=CCardName,hccardexp=CCardExp,hccardcvv=CCardCVV,hdcardnum=DCardNum ,hdcardname=DCardName,hdcardexp=DCardExp,hdcardcvv=DCardCVV,hfromacc=FromAcc,hchequenum=ChequeNum,hcaccname=CAccName,hcbankname=CBankName,hacctype=AccType )

if __name__ == "__main__":
    app.run(host='localhost',port=8001,debug=True)

import mysql.connector

connection=mysql.connector.connect(host='localhost',database='tal',user='root',password='admin')
cursor=connection.cursor()
sql=f"create table tal_transaction_details (StudName VARCHAR(20), StudNum VARCHAR(20), AccBranch VARCHAR(20),AccNum VARCHAR(20),AccDesc VARCHAR(20),BankName VARCHAR(20),BankCode VARCHAR(20),BankCity VARCHAR(20),BankAdd1 VARCHAR(20),BankAdd2 VARCHAR(20),CCardNum VARCHAR(20),CCardName VARCHAR(20),CCardExp VARCHAR(20),CCardCVV VARCHAR(20),DCardNum VARCHAR(20),DCardName VARCHAR(20),DCardExp VARCHAR(20),DCardCVV VARCHAR(20),FromAcc VARCHAR(20),ChequeNum VARCHAR(20),CAccName VARCHAR(20),CBankName VARCHAR(20),AccType VARCHAR(20));"
cursor.execute(sql)
sql1=f"insert into {tal_transaction_details} values ({StudName} , {StudNum}, {AccBranch},{AccNum},{AccDesc},{BankName},{BankCode},{BankCity},{BankAdd1},{BankAdd2},{CCardNum},{CCardName},{CCardExp},{CCardCVV},{DCardNum},{DCardName},{DCardExp},{DCardCVV},{FromAcc},{ChequeNum},{CAccName},{CBankName},{AccType}); "
cursor.execute(sql1)
connection.close()

