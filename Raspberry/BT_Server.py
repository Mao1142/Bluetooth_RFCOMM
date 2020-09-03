import uuid
import bluetooth

port=1
server_socket=bluetooth.BluetoothSocket(bluetooth.RFCOMM) #設定為射頻通訊
server_socket.bind(("", port)) #連結至port1
server_socket.listen(1) #監聽port1
service_id = str(uuid.uuid4()) #設定隨機UUID(通用唯一識別碼)

try:
    print('按下 Ctrl-C 可停止程式')
    while True:
        print('等待 RFCOMM 頻道 {} 的連線'.format(port))
        client_socket, client_info = server_socket.accept()
        print('接受來自 {} 的連線'.format(client_info))
        try:
            while True:
                data = client_socket.recv(1024).decode().lower()
                if len(data) == 0:
                    break
                if data == 'on':
                    print('開燈')
                    client_socket.send('Turn On  ')
                elif data == 'off':
                    print('關燈')
                    client_socket.send('Turn Off  ')
                else:
                    print('未知的指令: {}'.format(data))
        except IOError:
            pass
        client_socket.close()
        print('中斷連線')
except KeyboardInterrupt:
    print('中斷程式')
finally:
    if 'client_socket' in vars():
        client_socket.close()
    server_socket.close()
    print('中斷連線')
