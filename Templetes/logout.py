@app.route('/logout')
def logout():
    name = ''
    id = ''
    msg = 'You have been logged out successfully !'
    return render_template('login.html',msg=msg,name=name,id=id)