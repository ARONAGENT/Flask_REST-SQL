# Flask_REST_SQL-Project

## Overview
This project is a **REST API-based Flask application** that performs CRUD operations on an `accounts` table stored in an **AWS cloud database (MySQL)**. The API allows users to:
- Add new accounts (POST)
- Retrieve all accounts (GET)
- Search accounts by type (GET)
- Search accounts by account number (GET)
- Transfer money between accounts (PUT)
- Close an account (DELETE)

## Database Schema
The `accounts` table structure in **AWS MySQL**:
```sql
CREATE TABLE accounts (
    accno INT PRIMARY KEY,
    accnm VARCHAR(20),
    acctype VARCHAR(15),
    balance FLOAT
);
```

## Installation Steps
1. Install Python and Flask:
   ```sh
   pip install flask flask-restful pymysql
   ```
2. Clone the repository:
   ```sh
   git clone https://github.com/ARONAGENT/Flask_REST-SQL.git
   cd Flask-SQL-Project
   ```
3. Set up a MySQL database in AWS and configure connection settings in the scripts.
4. Run the Flask application:
   ```sh
   python app.py
   ```

---

## API Endpoints

### 1. Add an Account (POST)
**Endpoint:** `/account/add`
- Adds a new account to the database.
```python
@app.route('/account/add',methods=['POST'])
def add_account():
    ano = request.form.get('accno')
    anm = request.form.get('accnm')
    atp = request.form.get('acctype')
    bal = float(request.form.get('balance'))
    try:
        con = pymysql.connect(host="AWS_DB_HOST", user="USER", password="PWD", port=PORT, database="DB")
        curs = con.cursor()
        curs.execute("INSERT INTO accounts VALUES ('%s', '%s', '%s', %.2f)" % (ano, anm, atp, bal))
        con.commit()
        con.close()
        return {'status': 'success'}
    except:
        return {'status': 'failed'}
```
**Execution ->**

![flask-sql-post](https://github.com/user-attachments/assets/df081ee8-c188-49d7-af84-43902d409f8d)


### 2. Retrieve All Accounts (GET)
**Endpoint:** `/accounts/alldata`
```python
class AllAccounts(Resource):
    def get(self):
        con = pymysql.connect(host="AWS_DB_HOST", user="USER", password="PWD", port=PORT, database="DB")
        curs = con.cursor()
        curs.execute("SELECT * FROM accounts")
        data = curs.fetchall()
        return [{'accno': rec[0], 'accnm': rec[1], 'acctype': rec[2], 'balance': rec[3]} for rec in data]

api.add_resource(AllAccounts, '/accounts/alldata')
```
**Execution ->**

![flask-sql-get](https://github.com/user-attachments/assets/4d8ccbaa-40db-4227-936f-2a3d0ead2b85)


### 3. Search by Account Type (GET)
**Endpoint:** `/accounts/type/<acctype>`
```python
class GetByAcctype(Resource):
    def get(self, acctype):
        con = pymysql.connect(host="AWS_DB_HOST", user="USER", password="PWD", port=PORT, database="DB")
        curs = con.cursor()
        curs.execute("SELECT * FROM accounts WHERE acctype='%s'" % acctype)
        data = curs.fetchall()
        return [{'accno': rec[0], 'accnm': rec[1], 'acctype': rec[2], 'balance': rec[3]} for rec in data]

api.add_resource(GetByAcctype, '/accounts/type/<acctype>')
```
**Execution ->**

![flask-sql-get(search)](https://github.com/user-attachments/assets/f28d8fc3-73af-4ab3-9367-d0c7537a4cfb)

### 4. Search by Account Number (GET)
**Endpoint:** `/accounts/accno/<accno>`
```python
class GetByAccno(Resource):
    def get(self, accno):
        con = pymysql.connect(host="AWS_DB_HOST", user="USER", password="PWD", port=PORT, database="DB")
        curs = con.cursor()
        curs.execute("SELECT * FROM accounts WHERE accno='%d'" % int(accno))
        data = curs.fetchone()
        if data:
            return {'accno': data[0], 'accnm': data[1], 'acctype': data[2], 'balance': data[3]}
        return {'status': 'Account Not Found'}

api.add_resource(GetByAccno, '/accounts/accno/<accno>')
```
**Execution ->**

![flask-sql-searchaccno](https://github.com/user-attachments/assets/c821d201-5fb8-4490-be8a-a374c6532194)


### 5. Transfer Money (PUT)
**Endpoint:** `/account/update`
```python
@app.route('/account/update',methods=['PUT'])
def transfer_money():
    fno = int(request.form.get('fromaccno'))
    tno = int(request.form.get('toaccno'))
    bal = float(request.form.get('balance'))
    try:
        con = pymysql.connect(host="AWS_DB_HOST", user="USER", password="PWD", port=PORT, database="DB")
        curs = con.cursor()
        curs.execute("UPDATE accounts SET balance = balance - %.2f WHERE accno=%d" % (bal, fno))
        curs.execute("UPDATE accounts SET balance = balance + %.2f WHERE accno=%d" % (bal, tno))
        con.commit()
        con.close()
        return {'status': 'success'}
    except:
        return {'status': 'failed'}
```
**Execution ->**

![flask-sql-put](https://github.com/user-attachments/assets/807a4d1d-9922-4519-900b-38fd495024ec)

### 6. Close an Account (DELETE)
**Endpoint:** `/acc/delete`
```python
@app.route("/acc/delete", methods=["DELETE"])
def delete_account():
    ano = int(request.form.get('accno'))
    try:
        con = pymysql.connect(host="AWS_DB_HOST", user="USER", password="PWD", port=PORT, database="DB")
        curs = con.cursor()
        curs.execute("DELETE FROM accounts WHERE accno=%d" % ano)
        con.commit()
        con.close()
        return {'status': 'success'}
    except:
        return {'status': 'failed'}
```
**Execution ->**

![flask-sql-delete](https://github.com/user-attachments/assets/c3529c01-5d63-4f74-81c0-ab8a2fdc9811)

---

## Running the Project
1. Start the Flask app:
   ```sh
   python app.py
   ```
2. Use **Postman** or **Thunderbolt** to test API endpoints.
3. API request/response screenshots are available in the repository.

---

## Clone the Repository
```sh
git clone https://github.com/ARONAGENT/Flask_REST-SQL.git
cd Flask-SQL-Project
```

## Conclusion
This project demonstrates a **Flask-based REST API** that interacts with a **MySQL cloud database** hosted on AWS. The API supports CRUD operations and allows seamless integration with external clients 🚀 .

