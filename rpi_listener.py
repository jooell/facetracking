import os

fifo_path = '/tmp/input_pipe'

if not os.path.exists(fifo_path):
    os.mkfifo(fifo_path)

print("listening...")

with open(fifo_path, 'r') as fifo:
    while True:
        input_data = fifo.read().strip()
        if input_data:
            print(f"recieved: {input_data}")