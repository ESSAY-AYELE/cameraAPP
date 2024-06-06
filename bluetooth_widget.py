
from jnius import autoclass

BluetoothAdapter = autoclass('android.bluetooth.BluetoothAdapter')
BluetoothDevice = autoclass('android.bluetooth.BluetoothDevice')
BluetoothSocket = autoclass('android.bluetooth.BluetoothSocket')
UUID = autoclass('java.util.UUID')

class BluetootWidget:
    def __init__(self, name) -> None:
        self.name = name
        self.recv_stream, self.send_stream = self.get_socket_stream()
    def get_socket_stream(self):
        paired_devices = BluetoothAdapter.getDefaultAdapter().getBondedDevices().toArray()
        socket = None
        for device in paired_devices:
            if device.getName() == self.name:
                socket = device.createRfcommSocketToServiceRecord(
                    UUID.fromString("00001101-0000-1000-8000-00805F9B34FB"))
                recv_stream = socket.getInputStream()
                send_stream = socket.getOutputStream()
                break
        socket.connect()
        return recv_stream, send_stream
