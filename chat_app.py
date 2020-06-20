from flask import Flask,render_template,request,redirect,url_for
from flask_socketio import SocketIO,join_room

app=Flask(__name__)
socketio=SocketIO(app)


@app.route('/')
def home():
    return render_template('chatrooms.html')

@app.route('/chat')
def chat():
    username=request.args.get('username')
    room=request.args.get('room')

    if username and room:
        return render_template('chat.html',username=username,room=room)
    else:
        return redirect(url_for('home'))

@socketio.on('join_room')
def handle_join_room_event(data):
    app.logger.info("{} joined room {}".format(data['username'],data['room']))
    join_room(data['room'])
    socketio.emit('join_room_announcement', data)

if __name__=='__main__':
    socketio.run(app,debug=True)