from flask import Flask,jsonify
from flask_restful import Resource,Api
import pymysql

app=Flask(__name__)
api=Api(app)


class getByAcctype(Resource):
    def get(self,accno):
        no=int(accno)
        con=pymysql.connect(host="rohan-mysql-db-rohandbconnections.c.aivencloud.com",user="avnadmin",password="AVNS_jLvqn4KtNKeQMfTv6yn",port=19414,database="rohandb")
        curs=con.cursor()
        curs.execute("select * from accounts where accno='%d'" %no)
        data=curs.fetchone()
        if data:
            return jsonify({
                "accno": data[0],
                "accnm": data[1],
                "acctype": data[2],
                "balance": data[3]
                })
        else:
            return jsonify({
                "accno": accno,
                "accnm": "not found",
                "acctype": "not found",
                "balance": 0
            })
    
api.add_resource(getByAcctype,'/accounts/accno/<accno>')
app.run(port=6000,debug=True)