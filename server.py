import socket

host = '127.0.0.1'
port = 9500
cert_auth_host = '127.0.0.1'
cert_auth_port = 9501
servername = "Server_Name"
public_key = +1
private_key = -1
confirmation_copy = 'key confirmed'

def my_server(  ):
    cert_auth_connection = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    cert_auth_connection.connect( ( cert_auth_host, cert_auth_port ) )
    cert_auth_certificate = servername + " | " + str( public_key )
    cert_auth_connection.send( cert_auth_certificate.encode(  ) )
    cert_auth_respond = cert_auth_connection.recv( 1024 ).decode(  )
    cert_auth_connection.close(  )
    return ( cert_auth_respond == "200" )

def decrypt( text ):
    decrypted_copy = ''
    for char in text:
        decrypted_copy += chr( ord( char ) + private_key )
    return decrypted_copy

def encrypt( text ):
    encrypted_copy = ''
    for char in text:
        encrypted_copy += chr( ord( char ) + public_key )
    return encrypted_copy

def main(  ):
    if my_server(  ):
        print( "Reg Successful" )

        while True:

            connection = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
            connection.bind( ( HOST, PORT ) )

            connection.listen(  )
            print( HOST + ":" + str( PORT ) + "active" )

            session, addr = connection.accept(  )


            run_server = True
            while run_server:
                    receive_data = session.recv( 1024 ).decode(  )

                    if receive_data == "Hi":
                        print( "Hi' received by:" + servername )
                        output_data = servername

                    else:
                        print( "Text received: '" + receive_data + "'" )
                        decrypted_copy = decrypt( receive_data )
                        print( "Client request: '" + decrypted_copy + "'" )
                        if decrypted_copy == confirmationCopy:
                            output_data = encrypt( confirmationCopy + ' acknowledgement' )
                        else:
                            print( "Message handled" )
                            output_data = encrypt( "Confirmed – Message handled" )

                    print( "Response: '" + output_data +"'" )
                    session.send( output_data.encode(  ) )
    else:
        print( "Connection requirements not met." )
        exit


main(  )
