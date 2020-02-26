import socket

host = '127.0.0.1'
port = 9501

def main():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.bind((host, port))

    connection.listen()
    certificates = {}

    run_server = True
    while run_server:
        response = ""
        session, addr = connection.accept()
        received_data = session.recv(1024).decode().split(',')
        action = received_data[0]
        host = received_data[1]
        public_key = received_data[2]
        print("Validation date:")
        print(action + "," + host + "," + public_key)

        if action == 'Register':
            certificates[host] = public_key
            response = "200"

        elif action == 'Validate':
            if host in certificates:
                response = certificates[host]
            else:
                response = None

        else:
            response = ""

        if response != "":
            session.send(response.encode())

        session.close()


main()
