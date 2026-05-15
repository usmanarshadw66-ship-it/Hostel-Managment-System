from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'hostel_secret'

students = []
staffs = []
rooms = []
users = []

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_user():

    email = request.form['email']
    password = request.form['password']

    for user in users:
        if user['email'] == email and user['password'] == password:
            return redirect('/dashboard')

    flash('First create account then login')
    return redirect('/')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/create_account', methods=['POST'])
def create_account():

    data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'password': request.form['password']
    }

    users.append(data)

    flash('Account Created Successfully')

    return redirect('/')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/student', methods=['GET', 'POST'])
def student():

    if request.method == 'POST':

        data = {
            'name': request.form['name'],
            'age': request.form['age'],
            'student_id': request.form['student_id'],
            'room': request.form['room'],
            'fee': request.form['fee']
        }

        students.append(data)

    return render_template('student.html', students=students)


@app.route('/staff', methods=['GET', 'POST'])
def staff():

    if request.method == 'POST':

        data = {
            'name': request.form['name'],
            'age': request.form['age'],
            'staff_id': request.form['staff_id'],
            'position': request.form['position'],
            'salary': request.form['salary']
        }

        staffs.append(data)

    return render_template('staff.html', staffs=staffs)


@app.route('/room', methods=['GET', 'POST'])
def room():

    if request.method == 'POST':

        room_fee = int(request.form['room_fee'])
        units = int(request.form['units'])

        electricity = units * 12
        total = room_fee + electricity

        data = {
            'room_number': request.form['room_number'],
            'room_fee': room_fee,
            'electricity': electricity,
            'total': total
        }

        rooms.append(data)

    return render_template('room.html', rooms=rooms)


if __name__ == '__main__':
    app.run(debug=True)
