# Echo server program
import socket
import requests
import math
import os
from dotenv import load_dotenv
import random

load_dotenv()

client_id = os.environ['client_id']
Authorization = os.environ['Authorization']

def get_random_name(connection, message):
    while True:
        game_id = random.randint(1,299999)
        response = requests.post('https://api.igdb.com/v4/games', **{'headers': {'Client-ID': f'{client_id}', 'Authorization': f'{Authorization}'},'data': 'fields name; genres; where id={};'.format(game_id)})
        data = response.json()
        if data and data[0]:
            message = data[0]['name']
            return message
            #connection.sendall(message.encode('utf-8'))
            #break

def get_random_name_from_genre(connection, message):
    genre = message[6:]
    genre_id = 0
    return_message = ''
    match genre:
        case 'fighting':
            genre_id = 4
        case 'shooter':
            genre_id = 5
        case 'music':
            genre_id = 7
        case 'platform':
            genre_id = 8
        case 'puzzle':
            genre_id = 9
        case 'racing':
            genre_id = 10
        case 'rts':
            genre_id = 11
        case 'rpg':
            genre_id = 12
        case 'simulator':
            genre_id = 13
        case 'sport':
            genre_id = 14
        case 'strategy':
            genre_id = 15

    data = requests.post('https://api.igdb.com/v4/games', **{'headers': {'Client-ID': f'{client_id}', 'Authorization': f'{Authorization}'},'data': 'fields name; where genres = {};'.format(genre_id)})
    response = data.json()
    if response and response[0]:
        return_message = random.choice(response)['name']
        return return_message
    else:
        return_message = 'No games found'
        return return_message

if __name__ == '__main__':
    HOST = '192.168.5.9'                 
    PORT = 50007                         
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                message = data.decode('utf-8').lower()
                if not data: 
                    break
                if message == 'name':
                    name = get_random_name(conn, data.decode('utf-8'))
                    print("Sending: ", name)
                    conn.sendall(name.encode('utf-8'))

                elif message[:5] == 'genre':
                    name = get_random_name_from_genre(conn, data.decode('utf-8'))
                    print("Sending: ", name)
                    conn.sendall(name.encode('utf-8'))

                else:
                    print("Sending: Not a valid message")
                    conn.sendall('Not a valid message'.encode('utf-8'))
        s.close()
    


            
            
            
