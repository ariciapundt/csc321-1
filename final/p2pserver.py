import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv_string()
    
    new_msg = input("Enter your message: ")
    socket.send_string(new_msg)
