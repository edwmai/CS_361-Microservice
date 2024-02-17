# This microservice program returns back random video game names. It can also return back random video game names in a specific genre.

## Utilizing the API <br>
In order to use the API from IGDB, you must have a Twitch Account and sign up for the Twitch Developer Portal. You can do that here: https://api-docs.igdb.com/#getting-started <br>
After generating yoiur unique Client ID and Client Secret, replace your unique Client ID and Client Secret into the code of the microservice in order to get authorized to call the API.


## Requesting Data:<br>
  Using sockets, connect to HOST '192.168.5.9' and PORT 50007.<br>
  The microservice will accept 3 messages: 'name', 'genre:{genre}', and 'end'<br>

  ### 'name': When requesting for a random video game name, send message containing the string 'name' through the socket.
  Ex. Getting a random video game name
    
    # Echo client program
    import socket

    HOST = '192.168.5.9'    # The remote host
    PORT = 50007            # The same port as used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            try:
                message = 'name'
                s.sendall(message.encode('utf-8'))
                data = s.recv(1024)
                if data.decode('utf-8') == 'Goodbye':
                    print('Connection closed')
                    break
                print('Received:', data.decode('utf-8'))
            except KeyboardInterrupt:
                print('Connection closed')
                break
  ### 'genre:{genre}': When requesting for a random video game name in a specific genre, send a message in the format of 'genre:{genre}'<br>
  __*** This microservice only supports the following genres: point-and-click, fighting, shooter, music, platform, puzzle, racing, rts, rpg, simulator, sport, strategy ***__<br>
    Ex. Getting a random video game name in the fighting genre<br>
    
    # Echo client program
    import socket

    HOST = '192.168.5.9'    # The remote host
    PORT = 50007            # The same port as used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            try:
                message = 'genre:fighting'
                s.sendall(message.encode('utf-8'))
                data = s.recv(1024)
                if data.decode('utf-8') == 'Goodbye':
                    print('Connection closed')
                    break
                print('Received:', data.decode('utf-8'))
            except KeyboardInterrupt:
                print('Connection closed')
                break
  ### 'end': When you are done, send a message containing the string 'end' through the socket. The server will send back a "Goodbye" message which you can use to close the connection.<br>
  Ex. Ending and closing the connection
    
    HOST = '192.168.5.9'    # The remote host
    PORT = 50007            # The same port as used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            try:
                message = 'end'
                s.sendall(message.encode('utf-8'))
                data = s.recv(1024)
                if data.decode('utf-8') == 'Goodbye':
                    print('Connection closed')
                    break
                print('Received:', data.decode('utf-8'))
            except KeyboardInterrupt:
                print('Connection closed')
                break


## Receiving data:
  After sending a message through the socket, you will have to call .recv(1024) on the socket to catch the data that was sent back. In this case we pass 1024 to .recv() because that is enough data size for the name.<br>
  Ex. Getting a random video game name. (data = s.recv(1024)
    
    # Echo client program
    import socket

    HOST = '192.168.5.9'    # The remote host
    PORT = 50007            # The same port as used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            try:
                message = 'name'
                s.sendall(message.encode('utf-8'))
                data = s.recv(1024)
                if data.decode('utf-8') == 'Goodbye':
                    print('Connection closed')
                    break
                print('Received:', data.decode('utf-8'))
            except KeyboardInterrupt:
                print('Connection closed')
                break
  

## UML Sequence Diagram
![image](https://github.com/edwmai/CS_361-Microservice/assets/102533375/48bbdff7-c4d0-498a-8827-90393938d76e)




