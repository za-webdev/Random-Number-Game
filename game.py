from flask import Flask ,render_template,request,redirect,session ,flash
import random

app=Flask(__name__)

app.secret_key = 'ThisIsSecret'

def setSession():
	session['number']=random.randrange(0,101)


@app.route('/')
def guess():
	if "number" not in session:
		setSession()
		
	return render_template('/game.html')

@app.route('/guess', methods=['post'])
def guess_here():	
	
	guess=int(request.form['guess'])
	print request.form['guess']
	print session['number']

	if guess> session['number']:
		flash("Too High","error")

		
	elif guess<session['number']:
		flash("Too Low","error")

	elif guess==session['number']:
		flash("You got it right","success")

	else:
		flash("Not a valid number ","error")

	return redirect('/')

@app.route('/reset',methods=['post'])
def reset():
	session.clear()
	return redirect('/')

app.run(debug=True)







	



