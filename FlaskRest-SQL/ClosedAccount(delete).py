from flask import Flask,request
import pymysql

app=Flask(__name__)

@app.route("/acc/delete",methods=["DELETE"])
def delacc():
    ano=int(request.form.get('accno'))
    try:
        con=pymysql.connect(host="rohan-mysql-db-rohandbconnections.c.aivencloud.com",user="avnadmin",password="AVNS_jLvqn4KtNKeQMfTv6yn",port=19414,database="rohandb")
        curs=con.cursor()
        dic={}
        data=curs.execute("select * from accounts where accno=%d"%ano)
        if data:
            curs.execute("delete from accounts where accno=%d "%ano)
            dic["status"]="success"
        else:
            dic["status"]="failed"
            dic["accno"]="accno not found %d"%ano
        con.commit()
        con.close()
    except:
        dic['status']='failed to delete'
    return dic

app.run(debug=True)