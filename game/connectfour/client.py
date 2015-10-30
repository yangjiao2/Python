import connectfour
import collections, socket


    

    
if __name__ == '__main__':
    connect_socket = socket.socket()
    IP_address = input('What\'s IP address you want to connect?')
    port = eval(input('What\'s your port you want to connect?'))
    connect_socket.connect((IP_address, port))    
    listen_socket.close()  
    connect_socket_output = connect_socket.makefile('w')
    connect_socket_output.write('I32CPF_HELLO')

    
    # see the board
    # drop / pop
    # send to the server
    # waiting for the connection from the server
    # get DROP col / POP col
    
    