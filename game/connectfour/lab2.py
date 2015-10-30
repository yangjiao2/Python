# Jordan Minatogawa, Yang Jiao 82222745. Lab section 3, project 2.


# two programs are connected via sockets within thoes programs we have 2 streams:input stream, output stream.
# two programs:
# 1. client :  initiated the connection
# 2. server :  waiting for another program to connect to it and responded to the request
#
# IP address: ask the IP address before the program start.
# "loopback" address: 127.0.0.1 (test connections on one machine)
# Port: a server will register its interest in a particular port by binding to it


import socket


if __name__ == '__main__':
    # Create a new socket object.
    listen_socket = socket.socket()
    print ('listen_socket', listen_socket)
    IP_address = '127.0.0.1'
    ##IP_address = input('What\'s your IP address?')
    listen_address = (IP_address, 19999)
    listen_socket.bind(listen_address)
    print ('listen_socket', listen_socket)
    listen_socket.listen(0)
    stream_socket, from_address = listen_socket.accept()
    print ('listen_socket', listen_socket)