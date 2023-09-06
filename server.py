from flask import Flask, render_template, url_for, request, redirect
import csv
# render_template = to open html file from our folder (to send html file to our web)
# request =

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/<string:page_name>')
def index_page_name(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open('database.csv', mode ='a', newline = '') as database:
        email = data["email"]
        subject =data["subject"]
        message =data["message"]
        csv_writter = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL )
        # delimeter is a symbol to tell where to make the collum, in this case is a comma to indicate collums
        # quotechar and quoting search in the documentation
        csv_writter.writerow([email, subject, message])

# a route for submiting data from website to server
@app.route('/submit_data', methods=['POST', 'GET'])
def submit_data():
    # error = None
    if request.method == 'POST':
        try:
            data = request.form.to_dict() #request data and send it to dictionary
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return "not saved in database, please try again"
    else:
        return 'Sorry, something went wrong'









# use above instead of using the bellow code, it is too much :)

# @app.route("/")
# def index():
#     return render_template('index.html')

# @app.route("/index.html")
# def home():
#     return render_template('index.html')

# @app.route("/about.html")
# def about():
#     return render_template('about.html')

# @app.route("/components.html")
# def components():
#     return render_template('components.html')

# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')

# @app.route("/thankyou.html")
# def thankyou():
#     return render_template('thankyou.html')

# @app.route("/work.html")
# def work():
#     return render_template('work.html')

# @app.route("/works.html")
# def works():
#     return render_template('works.html')


