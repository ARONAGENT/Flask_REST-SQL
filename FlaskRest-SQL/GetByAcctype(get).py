from flask import Flask
from flask_restful import Resource,Api
import pymysql

app=Flask(__name__)
api=Api(app)


class getByAcctype(Resource):
    def get(self,acctype):
        con=pymysql.connect(host="rohan-mysql-db-rohandbconnections.c.aivencloud.com",user="avnadmin",password="AVNS_jLvqn4KtNKeQMfTv6yn",port=19414,database="rohandb")
        curs=con.cursor()
        curs.execute("select * from accounts where acctype='%s'" %acctype)
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
    
api.add_resource(getByAcctype,'/accounts/type/<acctype>')
app.run(debug=True)