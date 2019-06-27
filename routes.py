from app import app
@app.route('/index')
def index ():
	a=45
	b=52
	c=a+b
	d=c*a
	e=d+c*b
	print(e)
	return str(e)
	