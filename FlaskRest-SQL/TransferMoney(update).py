from flask import Flask,request
import pymysql

app=Flask(__name__)

@app.route('/account/update',methods=['PUT'])
def addcars():
    fno=int(request.form.get('fromaccno'))
    tno=int(request.form.get('toaccno')) 
    bal=float(request.form.get('balance'))
    dic={}
    try:
        con=pymysql.connect(host="rohan-mysql-db-rohandbconnections.c.aivencloud.com",user="avnadmin",password="AVNS_jLvqn4KtNKeQMfTv6yn",port=19414,database="rohandb")
        curs=con.cursor()
        curs.execute("update accounts set balance=balance-%.2f where accno=%d" %(bal,fno))
        con.commit()
        curs.execute("update accounts set balance=balance+%.2f where accno=%d" %(bal,tno))
        con.commit()
        con.close()
        dic['status']='success'
    except:
        dic['status']='failed'
    return dic

app.run(debug=True)

