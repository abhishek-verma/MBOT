from flask import Flask
from flask import request, jsonify
#from flask.ext.mysqldb import MySQL
from flask_mysqldb import MySQL



app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'user'
#app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_PASSWORD'] = 'mysql'
#app.config['MYSQL_DB'] = 'meme' # if not working try meme.db
app.config['MYSQL_DB'] = 'trial' # if not working try meme.db
mysql = MySQL(app)

@app.route('/api/memes/all', methods=['GET'])
def api_all():
    cur =  mysql.connection.cursor()
    #first_100_memes = cur.execute('SELECT * FROM MEMEDATA where selectedStatus=true and postedStatus=false limit 100;').fetchall()
    cur.execute('SELECT * FROM MEMEDATA limit 100;')
    first_100_memes = cur.fetchall()
    columns = [col[0] for col in cur.description]
    rows = [dict(zip(columns, row)) for row in first_100_memes]
    return jsonify(rows)

    from flask import send_file

'''
@app.route('/get_image', methods=['GET'])
def get_image():
    img_id = request.args('meme_id')
    filename = img_id + '.png'
    return send_file(filename, mimetype='image/png')

@app.route('/usr_response')
def save_meme_response(img_id):
    # get response either using
    req_data = request.get_json()

    # or using
    img_id = request.args('meme_id')

    # then get response
    selected_response = request.args.get("is_selected")

    # and save into db
'''
'''
@app.route('/get_image/<string:img_id>', methods=['GET'])
def get_image(img_id):
    filename = img_id + '.png'
    return send_file(filename, mimetype='image/png')

@app.route('/usr_response/<string:img_id>', methods=['PUT'])
def save_meme_response(img_id):

    # Get response
    selected_response = request.json['is_selected']

    # and save into db
    cur =  mysql.connection.cursor("""update MEMEDATA set selectedStatus=%s where meme_id=%s""", (selected_response, img_id))
    cur.execute()
    return "Success or whatever useful!"
'''
