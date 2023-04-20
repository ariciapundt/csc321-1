import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://node00:5555")

#get user message
message = input("Please enter your message here: ")
socket.send_string(message)

reply= socket.recv()
print("Received reply:", reply)