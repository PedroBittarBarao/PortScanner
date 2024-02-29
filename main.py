import socket
import time
import pandas as pd

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = input('Where to scan?: ')
port_start = int(input('Start port: '))
port_end = int(input('End port: '))

ports = pd.read_csv('tcp.csv', index_col=0) # https://github.com/maraisr/ports-list/blob/main/tcp.csv?plain=1
ports_dict = ports.set_index('port')['description'].to_dict()

target_ip = socket.gethostbyname(target)
print('Starting scan on host:', target_ip)

def port_scan(port):
    try:
        s.connect((target_ip, port))
        return True
    except:
        return False
 
 
start = time.time()
for port in range(port_start, port_end+1):
    if port_scan(port):
        print(f'port {port} is open ({ports_dict.get(port, "unknown")})')
    else:
        print(f'port {port} is closed ({ports_dict.get(port, "unknown")})')
 
end = time.time()
print(f'Time: {end-start:.2f} seconds')