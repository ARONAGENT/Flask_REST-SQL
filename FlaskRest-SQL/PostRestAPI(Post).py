from flask import Flask,request
import pymysql

app=Flask(__name__)

@app.route('/account/add',methods=['POST'])
def addcars():
    ano=request.form.get('accno') 
    anm=request.form.get('accnm')
    atp=request.form.get('acctype')
    bal=float(request.form.get('balance'))
    dic={}
    try:
        con=pymysql.connect(host="rohan-mysql-db-rohandbconnections.c.aivencloud.com",user="avnadmin",password="1111",port=19414,database="rohandb")
        curs=con.cursor()
        curs.execute("insert into accounts values ('%s','%s','%s',%.2f)" %(ano,anm,atp,bal))
        con.commit()
        con.close()
        dic['status']='success'
    except:
        dic['status']='failed'
    return dic

app.run(debug=True)

