from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta, date
from pytz import timezone
from dateutil.relativedelta import relativedelta





# Create a timezone-aware UTC datetime


# Load environment variables from .env file
load_dotenv()

# Create a Flask app
app = Flask(__name__)

# app.secret_key = '0df660dd7e2503a4'

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# 10:00 AM
# 11:00 AM
# 12:00 PM
# 01:00 PM
# 02:00 PM
# 03:00 PM
# 04:00 PM
# 05:00 PM
# 06:00 PM
# 07:00 PM
# db.create_all()


class Result(db.Model):
    __tablename__ = "results"
    id = db.Column(db.Integer, primary_key=True)
    slot_1_1 = db.Column(db.String(1), nullable=True)
    slot_1_3 = db.Column(db.String(3), nullable=True)
    slot_2_1 = db.Column(db.String(1), nullable=True)
    slot_2_3 = db.Column(db.String(3), nullable=True)
    slot_3_1 = db.Column(db.String(1), nullable=True)
    slot_3_3 = db.Column(db.String(3), nullable=True)
    slot_4_1 = db.Column(db.String(1), nullable=True)
    slot_4_3 = db.Column(db.String(3), nullable=True)
    slot_5_1 = db.Column(db.String(1), nullable=True)
    slot_5_3 = db.Column(db.String(3), nullable=True)
    slot_6_1 = db.Column(db.String(1), nullable=True)
    slot_6_3 = db.Column(db.String(3), nullable=True)
    slot_7_1 = db.Column(db.String(1), nullable=True)
    slot_7_3 = db.Column(db.String(3), nullable=True)
    slot_8_1 = db.Column(db.String(1), nullable=True)
    slot_8_3 = db.Column(db.String(3), nullable=True)
    slot_9_1 = db.Column(db.String(1), nullable=True)
    slot_9_3 = db.Column(db.String(3), nullable=True)
    slot_10_1 = db.Column(db.String(1), nullable=True)
    slot_10_3 = db.Column(db.String(3), nullable=True)
    date = db.Column(db.String(30), nullable=False)


class Extra(db.Model):
    __tablename__ = "extra_results"
    id = db.Column(db.Integer, primary_key=True)
    open_1 = db.Column(db.String(1), nullable=True)
    open_3 = db.Column(db.String(3), nullable=True)
    close_1 = db.Column(db.String(1), nullable=True)
    close_3 = db.Column(db.String(3), nullable=True)
    date = db.Column(db.String(30), nullable=False)


# Get the admin password from the environment variable
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')


# @app.route('/delete_old_results', methods=['POST'])
# def delete_old_results():
#     old_results = datetime.now(timezone("Asia/Kolkata")) - relativedelta(months=2)
#     old_results = old_results.strftime('%d-%m-%Y')
#     old_results = Result.query.filter(Result.date.like(f"%{old_results}%")).all()
        
#     if old_results:
#         for data in old_results:
#             db.session.delete(data)
#         db.session.commit()

@app.route('/delete_old_results', methods=['GET', 'POST'])
def delete_old_results():
    # Calculate the date 2 months ago from now
    cutoff_1 = datetime.now(timezone("Asia/Kolkata")) - relativedelta(months=1)
    cutoff_1 = cutoff_1.strftime('%b-%Y')

    cutoff_2 = datetime.now(timezone("Asia/Kolkata")) - relativedelta(months=2)
    cutoff_2 = cutoff_2.strftime('%b-%Y')

    cutoff_3 = datetime.now(timezone("Asia/Kolkata")) - relativedelta(months=3)
    cutoff_3 = cutoff_3.strftime('%b-%Y')

    cutoff_4 = datetime.now(timezone("Asia/Kolkata")) - relativedelta(months=4)
    cutoff_4 = cutoff_4.strftime('%b-%Y')

    cutoff_5 = datetime.now(timezone("Asia/Kolkata")) - relativedelta(months=5)
    cutoff_5 = cutoff_5.strftime('%b-%Y')

    cutoff_6 = datetime.now(timezone("Asia/Kolkata")) - relativedelta(months=6)
    cutoff_6 = cutoff_6.strftime('%b-%Y')

    # Query records older than 2 months
    # old_results_1 = Result.query.filter(Result.date < cutoff_date).all()
    old_results_1 = Result.query.filter(Result.date.like(f"%{cutoff_1}%")).all()
    old_results_2 = Result.query.filter(Result.date.like(f"%{cutoff_2}%")).all()
    old_results_3 = Result.query.filter(Result.date.like(f"%{cutoff_3}%")).all()
    old_results_4 = Result.query.filter(Result.date.like(f"%{cutoff_4}%")).all()
    old_results_5 = Result.query.filter(Result.date.like(f"%{cutoff_5}%")).all()
    old_results_6 = Result.query.filter(Result.date.like(f"%{cutoff_6}%")).all()

    # Delete the old records
    if old_results_1:
        for data in old_results_1:
            db.session.delete(data)
        db.session.commit()

    if old_results_2:
        for data in old_results_2:
            db.session.delete(data)
        db.session.commit()

    if old_results_3:
        for data in old_results_3:
            db.session.delete(data)
        db.session.commit()

    if old_results_4:
        for data in old_results_4:
            db.session.delete(data)
        db.session.commit()

    if old_results_5:
        for data in old_results_5:
            db.session.delete(data)
        db.session.commit()

    if old_results_6:
        for data in old_results_6:
            db.session.delete(data)
        db.session.commit()


    old_extras_1 = Extra.query.filter(Extra.date.like(f"%{cutoff_1}%")).all()
    old_extras_2 = Extra.query.filter(Extra.date.like(f"%{cutoff_2}%")).all()
    old_extras_3 = Extra.query.filter(Extra.date.like(f"%{cutoff_3}%")).all()
    old_extras_4 = Extra.query.filter(Extra.date.like(f"%{cutoff_4}%")).all()
    old_extras_5 = Extra.query.filter(Extra.date.like(f"%{cutoff_5}%")).all()
    old_extras_6 = Extra.query.filter(Extra.date.like(f"%{cutoff_6}%")).all()

    # Delete the old records
    if old_extras_1:
        for data in old_extras_1:
            db.session.delete(data)
        db.session.commit()

    if old_extras_2:
        for data in old_extras_2:
            db.session.delete(data)
        db.session.commit()

    if old_extras_3:
        for data in old_extras_3:
            db.session.delete(data)
        db.session.commit()

    if old_extras_4:
        for data in old_extras_4:
            db.session.delete(data)
        db.session.commit()

    if old_extras_5:
        for data in old_extras_5:
            db.session.delete(data)
        db.session.commit()

    if old_extras_6:
        for data in old_extras_6:
            db.session.delete(data)
        db.session.commit()

    return redirect(url_for('home'))


@app.route("/")
def home():
    results = Result.query.order_by(Result.id.desc()).all()

    now = datetime.now(timezone("Asia/Kolkata"))

    currentday = now.strftime('%d-%b-%Y(%a)')
    daily_data = Result.query.filter_by(date=currentday).first()
    daily_extra = Extra.query.filter_by(date=currentday).first()

    g_matka_result0 = Result.query.filter_by(date=currentday).first()

    g_matka_1 = datetime.now(timezone("Asia/Kolkata")) - relativedelta(days=1)
    g_matka_1 = g_matka_1.strftime('%d-%b-%Y(%a)')
    g_matka_result1 = Result.query.filter_by(date=g_matka_1).first()

    g_matka_2 = datetime.now(timezone("Asia/Kolkata")) - relativedelta(days=2)
    g_matka_2 = g_matka_2.strftime('%d-%b-%Y(%a)')
    g_matka_result2 = Result.query.filter_by(date=g_matka_2).first()

    g_matka_3 = datetime.now(timezone("Asia/Kolkata")) - relativedelta(days=3)
    g_matka_3 = g_matka_3.strftime('%d-%b-%Y(%a)')
    g_matka_result3 = Result.query.filter_by(date=g_matka_3).first()

    g_matka_4 = datetime.now(timezone("Asia/Kolkata")) - relativedelta(days=4)
    g_matka_4 = g_matka_4.strftime('%d-%b-%Y(%a)')
    g_matka_result4 = Result.query.filter_by(date=g_matka_4).first()

    g_matka_5 = datetime.now(timezone("Asia/Kolkata")) - relativedelta(days=5)
    g_matka_5 = g_matka_5.strftime('%d-%b-%Y(%a)')
    g_matka_result5 = Result.query.filter_by(date=g_matka_5).first()

    g_matka_6 = datetime.now(timezone("Asia/Kolkata")) - relativedelta(days=6)
    g_matka_6 = g_matka_6.strftime('%d-%b-%Y(%a)')
    g_matka_result6 = Result.query.filter_by(date=g_matka_6).first()

    g_matka_results = [g_matka_result0, g_matka_result1, g_matka_result2, g_matka_result3, g_matka_result4, g_matka_result5, g_matka_result6]


    g_night_result0 = Extra.query.filter_by(date=currentday).first()

    g_night_1 = datetime.now(timezone("Asia/Kolkata")) - relativedelta(days=1)
    g_night_1 = g_night_1.strftime('%d-%b-%Y(%a)')
    g_night_result1 = Extra.query.filter_by(date=g_night_1).first()

    g_night_2 = datetime.now(timezone("Asia/Kolkata")) - relativedelta(days=2)
    g_night_2 = g_night_2.strftime('%d-%b-%Y(%a)')
    g_night_result2 = Extra.query.filter_by(date=g_night_2).first()

    g_night_3 = datetime.now(timezone("Asia/Kolkata")) - relativedelta(days=3)
    g_night_3 = g_night_3.strftime('%d-%b-%Y(%a)')
    g_night_result3 = Extra.query.filter_by(date=g_night_3).first()

    g_night_4 = datetime.now(timezone("Asia/Kolkata")) - relativedelta(days=4)
    g_night_4 = g_night_4.strftime('%d-%b-%Y(%a)')
    g_night_result4 = Extra.query.filter_by(date=g_night_4).first()

    g_night_5 = datetime.now(timezone("Asia/Kolkata")) - relativedelta(days=5)
    g_night_5 = g_night_5.strftime('%d-%b-%Y(%a)')
    g_night_result5 = Extra.query.filter_by(date=g_night_5).first()

    g_night_6 = datetime.now(timezone("Asia/Kolkata")) - relativedelta(days=6)
    g_night_6 = g_night_6.strftime('%d-%b-%Y(%a)')
    g_night_result6 = Extra.query.filter_by(date=g_night_6).first()

    g_night_results = [g_night_result0, g_night_result1, g_night_result2, g_night_result3, g_night_result4, g_night_result5, g_night_result6]

    start_time = {
    'slot1' : now.replace(hour=10, minute=0, second=0, microsecond=0),
    'slot2' : now.replace(hour=11, minute=0, second=0, microsecond=0),
    'slot3' : now.replace(hour=12, minute=0, second=0, microsecond=0),
    'slot4' : now.replace(hour=13, minute=0, second=0, microsecond=0),
    'slot5' : now.replace(hour=14, minute=0, second=0, microsecond=0),
    'slot6' : now.replace(hour=15, minute=0, second=0, microsecond=0),
    'slot7' : now.replace(hour=16, minute=0, second=0, microsecond=0),
    'slot8' : now.replace(hour=17, minute=0, second=0, microsecond=0),
    'slot9' : now.replace(hour=18, minute=0, second=0, microsecond=0),
    'slot10' : now.replace(hour=19, minute=0, second=0, microsecond=0)
    }

    end_time = {
    'slot1' : now.replace(hour=10, minute=55, second=0, microsecond=0),
    'slot2' : now.replace(hour=11, minute=55, second=0, microsecond=0),
    'slot3' : now.replace(hour=12, minute=55, second=0, microsecond=0),
    'slot4' : now.replace(hour=13, minute=55, second=0, microsecond=0),
    'slot5' : now.replace(hour=14, minute=55, second=0, microsecond=0),
    'slot6' : now.replace(hour=15, minute=55, second=0, microsecond=0),
    'slot7' : now.replace(hour=16, minute=55, second=0, microsecond=0),
    'slot8' : now.replace(hour=17, minute=55, second=0, microsecond=0),
    'slot9' : now.replace(hour=18, minute=55, second=0, microsecond=0),
    'slot10' : now.replace(hour=19, minute=55, second=0, microsecond=0),
    }

    return render_template('index.html', g_matka_results=g_matka_results, g_night_results=g_night_results, results=results, extra=daily_extra, now=now, start_time=start_time, end_time=end_time, daily_data=daily_data, title="Fastest and Live Online Goa Satta Result only at goasatta.in")


@app.route("/admin_auth", methods=['GET', 'POST'])
def admin_auth():
    if request.method == 'POST':
        password = request.form['password']
        if password == ADMIN_PASSWORD:
            session['admin'] = True
            return redirect(url_for('admin'))
        else:
            flash("Invalid Password. Try Again!!!")
            return redirect(url_for('admin_auth')) 
    return render_template('login.html', title="Admin Login")


@app.route("/admin")
def admin():
    if 'admin' in session:
        now = datetime.now(timezone("Asia/Kolkata"))
        currentday = now.strftime('%d-%b-%Y(%a)')
        daily_data = Result.query.filter_by(date=currentday).first()
        daily_extra = Extra.query.filter_by(date=currentday).first()
        return render_template('admin.html', daily_data=daily_data, daily_extra=daily_extra, title="Admin Panel")
    return redirect(url_for('admin_auth'))
    

@app.route('/add', methods=['POST'])
def add():
    currentday = datetime.now(timezone("Asia/Kolkata")).strftime('%d-%b-%Y(%a)')
    daily_data = Result.query.filter_by(date=currentday).first()

    if not daily_data:
        daily_data = Result(date=currentday)

    slot = request.form['slots']
    value_1 = request.form['one_digit']
    value_3 = request.form['three_digit']

    if slot == '1':
        daily_data.slot_1_1 = value_1
        daily_data.slot_1_3 = value_3
    elif slot == '2':
        daily_data.slot_2_1 = value_1
        daily_data.slot_2_3 = value_3
    elif slot == '3':
        daily_data.slot_3_1 = value_1
        daily_data.slot_3_3 = value_3
    elif slot == '4':
        daily_data.slot_4_1 = value_1
        daily_data.slot_4_3 = value_3
    elif slot == '5':
        daily_data.slot_5_1 = value_1
        daily_data.slot_5_3 = value_3
    elif slot == '6':
        daily_data.slot_6_1 = value_1
        daily_data.slot_6_3 = value_3
    elif slot == '7':
        daily_data.slot_7_1 = value_1
        daily_data.slot_7_3 = value_3
    elif slot == '8':
        daily_data.slot_8_1 = value_1
        daily_data.slot_8_3 = value_3
    elif slot == '9':
        daily_data.slot_9_1 = value_1
        daily_data.slot_9_3 = value_3
    elif slot == '10':
        daily_data.slot_10_1 = value_1
        daily_data.slot_10_3 = value_3

    db.session.add(daily_data)
    db.session.commit()
    return redirect('/admin')


@app.route('/update/<int:slot>', methods=['GET', 'POST'])
def update(slot):
    if 'admin' in session:
        currentday = datetime.now(timezone("Asia/Kolkata")).strftime('%d-%b-%Y(%a)')
        daily_data = Result.query.filter_by(date=currentday).first()

        slot_one  = f'slot_{slot}_1'
        slot_three  = f'slot_{slot}_3'

        one = getattr(daily_data, slot_one)
        three = getattr(daily_data, slot_three)

        if request.method=='POST':
            oneDigi = request.form['oneDigi']
            threeDigi = request.form['threeDigi']
            setattr(daily_data, slot_one, oneDigi)
            setattr(daily_data, slot_three, threeDigi)
            db.session.commit()
            return redirect('/admin')
        return render_template('update.html', one = one, three = three, slot=slot, title="Edit Result")
    return redirect(url_for('admin_auth'))


@app.route('/delete/<int:slot>', methods=['GET', 'POST'])
def delete(slot):
    if 'admin' in session:
        currentday = datetime.now(timezone("Asia/Kolkata")).strftime('%d-%b-%Y(%a)')
        daily_data = Result.query.filter_by(date=currentday).first()

        slot_one  = f'slot_{slot}_1'
        slot_three  = f'slot_{slot}_3'

        setattr(daily_data, slot_one, None)
        setattr(daily_data, slot_three, None)
        db.session.commit()
        return redirect('/admin')
    return redirect(url_for('admin_auth'))


@app.route('/add_extra', methods=['POST'])
def add_extra():
    currentday = datetime.now(timezone("Asia/Kolkata")).strftime('%d-%b-%Y(%a)')
    daily_extra = Extra.query.filter_by(date=currentday).first()

    if not daily_extra:
        daily_extra = Extra(date=currentday)

    slot = request.form['slots']
    value_1 = request.form['one_digit']
    value_3 = request.form['three_digit']

    if slot == '1':
        daily_extra.open_1 = value_1
        daily_extra.open_3 = value_3
    elif slot == '2':
        daily_extra.close_1 = value_1
        daily_extra.close_3 = value_3

    db.session.add(daily_extra)
    db.session.commit()
    return redirect('/admin')


@app.route('/update_extra/<int:slot_no>', methods=['GET', 'POST'])
def update_extra(slot_no):
    if 'admin' in session:
        currentday = datetime.now(timezone("Asia/Kolkata")).strftime('%d-%b-%Y(%a)')
        daily_extra = Extra.query.filter_by(date=currentday).first()
        
        slot = 'open' if slot_no == 1 else 'close'

        slot_one  = f'{slot}_1'
        slot_three  = f'{slot}_3'

        one = getattr(daily_extra, slot_one)
        three = getattr(daily_extra, slot_three)

        if request.method=='POST':
            oneDigi = request.form['oneDigi']
            threeDigi = request.form['threeDigi']
            setattr(daily_extra, slot_one, oneDigi)
            setattr(daily_extra, slot_three, threeDigi)
            db.session.commit()
            return redirect('/admin')
        return render_template('update_extra.html', one = one, three = three, slot_no=slot_no, slot=slot, title="Edit Result")
    return redirect(url_for('admin_auth'))


@app.route('/delete_extra/<int:slot_no>', methods=['GET', 'POST'])
def delete_extra(slot_no):
    if 'admin' in session:
        currentday = datetime.now(timezone("Asia/Kolkata")).strftime('%d-%b-%Y(%a)')
        daily_extra = Extra.query.filter_by(date=currentday).first()

        slot = 'open' if slot_no == 1 else 'close'

        slot_one  = f'{slot}_1'
        slot_three  = f'{slot}_3'

        setattr(daily_extra, slot_one, None)
        setattr(daily_extra, slot_three, None)
        db.session.commit()
        return redirect('/admin')
    return redirect(url_for('admin_auth'))


@app.route('/admin_logout')
def logout():
    session.pop('admin', None)
    return redirect(url_for('admin_auth'))


@app.route("/about")
def about():
    return render_template('about.html', title="About Us")

@app.route("/text")
def text():
    
    results = Result.query.order_by(Result.id.desc()).all()

    now = datetime.now(timezone("Asia/Kolkata"))

    currentday = now.strftime('%d-%b-%Y(%a)')
    daily_data = Result.query.filter_by(date=currentday).first()
    daily_extra = Extra.query.filter_by(date=currentday).first()

    start_time = {
    'slot1' : now.replace(hour=10, minute=0, second=0, microsecond=0),
    'slot2' : now.replace(hour=11, minute=0, second=0, microsecond=0),
    'slot3' : now.replace(hour=12, minute=0, second=0, microsecond=0),
    'slot4' : now.replace(hour=13, minute=0, second=0, microsecond=0),
    'slot5' : now.replace(hour=14, minute=0, second=0, microsecond=0),
    'slot6' : now.replace(hour=15, minute=0, second=0, microsecond=0),
    'slot7' : now.replace(hour=16, minute=0, second=0, microsecond=0),
    'slot8' : now.replace(hour=17, minute=0, second=0, microsecond=0),
    'slot9' : now.replace(hour=18, minute=0, second=0, microsecond=0),
    'slot10' : now.replace(hour=19, minute=0, second=0, microsecond=0)
    }

    end_time = {
    'slot1' : now.replace(hour=10, minute=55, second=0, microsecond=0),
    'slot2' : now.replace(hour=11, minute=55, second=0, microsecond=0),
    'slot3' : now.replace(hour=12, minute=55, second=0, microsecond=0),
    'slot4' : now.replace(hour=13, minute=55, second=0, microsecond=0),
    'slot5' : now.replace(hour=14, minute=55, second=0, microsecond=0),
    'slot6' : now.replace(hour=15, minute=55, second=0, microsecond=0),
    'slot7' : now.replace(hour=16, minute=55, second=0, microsecond=0),
    'slot8' : now.replace(hour=17, minute=55, second=0, microsecond=0),
    'slot9' : now.replace(hour=18, minute=55, second=0, microsecond=0),
    'slot10' : now.replace(hour=19, minute=55, second=0, microsecond=0),
    }

    return render_template('text.html', results=results, extra=daily_extra, now=now, start_time=start_time, end_time=end_time, daily_data=daily_data, title="Fastest and Live Online Goa Satta Result only at goasatta.in")




# @app.route("/online")
# def online():
#     return render_template('online.html', title="Play Online")

@app.route("/contact")
def contact():
    return render_template('contact.html', title="Contact Us")
@app.route("/old")
def old():


      matka_results = Result.query.order_by(Result.id.desc()).limit(31).all()
      night_results = Extra.query.order_by(Extra.id.desc()).limit(31).all()
      return render_template('old.html', matka_results=matka_results, night_results=night_results, title="Old Result")
if __name__ == '__main__':
    app.run(debug=True)