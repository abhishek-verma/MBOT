from flask import Flask
from flask import request, jsonify
#from flask.ext.mysqldb import MySQL
from flask_mysqldb import MySQL
from flask import send_file




app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'user'
#app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_PASSWORD'] = 'mysql'
#app.config['MYSQL_DB'] = 'meme' # if not working try meme.db
app.config['MYSQL_DB'] = 'meme' # if not working try meme.db
mysql = MySQL(app)

#all meme data
@app.route('/api/memes/all', methods=['GET'])
def api_all():
    cur =  mysql.connection.cursor()
    first_100_memes = cur.execute('select * from MEMEDATA where selectedStatus=true and postedStatus=false limit 100;').fetchall()
    columns = [col[0] for col in cur.description]
    rows = [dict(zip(columns, row)) for row in first_100_memes]
    return jsonify(rows)

    from flask import send_file

#memes to be displayed for selection
@app.route('/api/memes/selection/all', methods=['GET'])
def api_select_all():
    cur =  mysql.connection.cursor()
    cur.execute('select * from MEMEDATA where selectedStatus IS NULL;')
    first_100_memes = cur.fetchall()
    columns = [col[0] for col in cur.description]
    rows = [dict(zip(columns, row)) for row in first_100_memes]
    return jsonify(rows)



@app.route('/get_image/<string:img_id>', methods=['GET'])
def get_image(img_id):
    filename = img_id + '.png'
    return send_file(filename, mimetype='image/png')

@app.route('/usr_response', methods=['POST'])
def save_meme_response(img_id):

    modify_data = []
    if(request.data):
        # Get response
        response = request.get_json()

        # Fro each response save into db
        for item in request.json['ResponseList']:
            img_id = item["img_id"]
            selected_response = item['is_selected']
    # and save into db
    cur =  mysql.connection.cursor("""update MEMEDATA set selectedStatus=%s where meme_id=%s""", (selected_response, img_id))
    cur.execute()
    return "Success or whatever useful!"

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
