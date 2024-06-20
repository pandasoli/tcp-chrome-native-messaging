#!/bin/env python3

import struct
import logging
from socket    import socket, AF_INET, SOCK_STREAM
from sys       import stdout, stdin, exit
from threading import Thread

logging.basicConfig(
  filename='native-messaging-host.log',
  level=logging.DEBUG,
  format='%(asctime)s %(levelname)s: %(message)s',
  datefmt='%Y-%m-%d %H:%M:%S'
)

HOST = '127.0.0.1'
PORT = 65432

server = socket(AF_INET, SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
logging.info(f'Listening on tcp://{HOST}:{PORT}')

def handle():
  while True:
    logging.info(f'Waiting for incoming TCP connection')
    conn, addr = server.accept()
    logging.info(f'Connected to {addr}')

    with conn:
      data = conn.recv(1024) # 1e+6 = 1mb
      if not data: return

      data = data.decode()

      logging.info(f'TCP received "{data}"')
      conn.send(data.encode())
      send(f'"{data}"')

def send(msg, fd=stdout):
  fd.buffer.write(struct.pack('I', len(msg)))
  fd.write(msg)
  fd.flush()

def read():
  while True:
    text_len_bytes = stdin.buffer.read(4)

    if len(text_len_bytes) == 0:
      break

    text_len = struct.unpack('@I', text_len_bytes)[0]
    text = stdin.buffer.read(text_len).decode('utf-8')

    logging.info(f'Received message: {text}')
    send(text)

if __name__ == '__main__':
  read_th = Thread(target=read)
  read_th.start()

  tcp_th = Thread(target=handle)
  tcp_th.start()

  read_th.join()
  tcp_th.stop()
  server.close()

  exit(0)
