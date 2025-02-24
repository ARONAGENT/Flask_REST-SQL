from flask import Flask
from flask_restful import Resource,Api
import pymysql

app=Flask(__name__)
api=Api(app)

class allaccounts(Resource):
    def get(self):
        con=pymysql.connect(host="rohan-mysql-db-rohandbconnections.c.aivencloud.com",user="avnadmin",password="1111",port=19414,database="rohandb")
        curs=con.cursor()
        curs.execute('select * from accounts')
        data=curs.fetchall()
        lst=[]
        for rec in data:
            dic={}
            dic['accno']=rec[0]
            dic['accnm']=rec[1]
            dic['acctype']=rec[2]
            dic['balance']=rec[3]
            lst.append(dic)        
        return lst
    
api.add_resource(allaccounts,'/accounts/alldata')
app.run(debug=True)
