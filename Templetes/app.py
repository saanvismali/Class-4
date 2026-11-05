@app.route('/login',methods=['GET','POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:

        username = request.form['username']
        password = request.form['password']

        mydb = mysql.connecter.connect(
            host = "YOUR_DATABASE_HOST"
            user = "YOUR_DATABASE_USER"
            password = "YOUR_DATABASE_PASSWORD"
            database = "YOUR_DATABASE_NAME"
        )

        mycursor = mydb.cursor()

        mycursor.execute(
            "SELECT * FROM LoginDetails Where Name = %s AND Password = %s", (username, password)
        )

        account = mycursor.fetchone()

        if account:
            print("Login successful")

            name = account[1]
            id = account[0]

            msg = 'Logged in successfully !'

            print('Logged in successfully !')

            mycursor.close()
            mydb.close()

            return render_template('index.html', msg=msg, name=name, id=id)
        else:
            msg = 'Incorrect Credentials. kindly check'

            mycursor.close()
            mydb.close()

            return render_template('login.html', msg=msg)
    else:
        return render_template('login.html')
    
            
