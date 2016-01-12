from flask import Flask, redirect, request, jsonify

from bigbluebutton import BBB_API

import middleware
import settings
import helpers
import json

app = Flask(__name__)
app.wsgi_app = middleware.Auth(app.wsgi_app)

@app.route("/hi")
def hi():
    return 'hi!'

@app.route("/create")
def create():
    """
    Creates a new meeting 
    
    Usage: GET /create?name=...&moderator_pw=...
    """

    name = request.args.get('name', '')
    moderatorPW = request.args.get('moderator_pw', '')
    userPW = request.args.get('attendee_pw', '')
    welcome = request.args.get('welcome_msg', '')
    logout_url = request.args.get('logout_url', '')
    duration = request.args.get('duration', 0)

    query_dict = {
        'name': name, 
        'moderatorPW': moderatorPW, 
        'attendeePW': userPW,
        'welcome': welcome,
        'logoutURL': logout_url,
        'duration': duration
    }

    b = BBB_API()
    c = b.create(query_dict)

    return jsonify(c['response'])

@app.route("/join/<meeting_id>/")
def join(meeting_id):
    """
    Returns the url to join the meeting
    """

    query_dict = {
        'fullName': request.args.get('full_name', '').encode('utf-8'),
        'password': request.args.get('password', ''),
        'meetingID': meeting_id
    }

    if not query_dict['fullName'] or not query_dict['password']:
        return jsonify({'result': 'FAIL', 'message': "You need to send the user's full name and password to join the room"})

    b = BBB_API()
    url = b.join(query_dict)

    return jsonify({'result':'SUCCESS', 'url': url})

if __name__ == "__main__":
    app.run(debug=True)