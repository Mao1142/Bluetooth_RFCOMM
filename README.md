# Bluetooth_RFCOMM Server&Client
Pyhton編寫的樹苺派藍芽Server跟AppInventer製作的Android藍芽Client

## 環境設定
### 更新系統

        sudo apt-get update
        sudo apt-get upgrade
        
### 安裝藍芽套件

        sudo apt-get install python-bluetooth
        python3 -m pip install pybluez

### 設置SPP

        sudo nano /etc/systemd/system/dbus-org.bluez.service
        
將ExecStart最後加上 –C 並於下一行新增ExecStartPost如下

        ExecStart=/usr/lib/bluetooth/bluetoothd -C
        ExecStartPost=/usr/bin/sdptool add SP

### 藍芽自動認可配對

寫成腳本由rc.local呼叫每次開機執行

        bluetoothctl power on
        bluetoothctl discoverable yes
        bluetoothctl pairable on
        bluetoothctl agent NoInputNoOutput
        bluetoothctl default-agent

## Server端程式執行
於命令列中輸入

    python3 ./BT_server.py

## APP Inventor 專案匯入

1 - 開啟AI2 http://ai2.appinventor.mit.edu/?locale=zh_TW

2 - 匯入專案

3 - 選擇LED_BTClient.aia

4 - 打包APK
