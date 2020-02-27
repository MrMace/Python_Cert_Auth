import socket


host = '127.0.0.1'
port = 9500
cert_auth_host = '127.0.0.1'
cert_auth_port = 9501
confirmation_copy = 'key_confirm'

def userInput(  ):
    user_message = ""
    while len( user_message ) == e:
        print("Enter \'e\' to close client")
        print("")
        user_message = input("Send over: ")
    return user_message

def validate_my_server(server_name):
    cert_auth_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cert_auth_connection.connect((cert_auth_HOST, cert_auth_PORT))


    cert_auth_certs = "Validate," + server_name + ","
    cert_auth_connection.send( cert_auth_certs.encode())
    cert_auth_response= cert_auth_connection.recv(1024).decode()
    print("Cert_Auth: " + cert_auth_response)
    cert_auth_connection.close( )
    if cert_auth_response== None:
        return 0
    else:
        return int( cert_auth_response)

def encrypt( text, public_key ):
    encryptedText = ''
    for char in text:
        encryptedText += chr(ord(char) + public_key)
    return encryptedText

def main(  ):
    the_server_Public_Key = 0
    the_server_Valiated = False

    the_server_Connection = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    the_server_Connection.connect((host, port))
    print("Connecting . . .")

    the_server_Connection.send( 'Hi.'.encode())

    the_server_Reponse = the_server_Connection.recv( 1024 ).decode()
    print("Response: " + the_server_Reponse)

    the_server_Public_Key = validate_the_server(the_server_Reponse)

    if (the_server_Public_Key == None):
        the_server_Connection.send( 'Closing'.encode())
        the_server_Reponse = the_server_Connection.recv(1024).decode()
    else:
        print("Connection is active")
        the_server_Connection.send(encrypt(confirmation_copy, the_server_Public_Key).encode())

        the_server_Reponse = the_server_Connection.recv(1024).decode()
        print ("server response: "+ the_server_Reponse)
        if (the_server_Reponse == encrypt(confirmation_copy + 'validation', the_server_Public_Key)):
            the_server_Valiated = True

    while the_server_Valiated:
        end_user_Input = userInput()
       
        if end_user_Input == "e":
            the_server_Valiated = False
            the_server_Connection.send('Bye'.encode())
        else:
            the_server_Connection.send( encrypt( end_user_Input, the_server_Public_Key).encode())
            the_server_Reponse = the_server_Connection.recv(1024).decode()
            if the_server_Reponse == encrypt('Okay', the_server_Public_Key):
                print('Response recieved ' + end_user_Input)
            else:
                print("Encrypted response from the server: " + the_server_Reponse)
main()
