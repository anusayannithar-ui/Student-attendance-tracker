from  evdev  import InputDevice,list_devices,ecodes,categorize
import requests 

devices = [InputDevice(path) for path in list_devices()]


for device in devices:
    print(device.path,device.name,device.phys)



# after this we can connect to sutiable one 

scanner =  InputDevice("dev/input/event?")
print(scanner)


for event in device.read_loop():
    if event.type == ecodes.EV_KEY:
        print(categorize(event))


url = "http://vidyananda"

after_scan_std_data = {
    "qr_code_hashed":"qr_code_hashed"
}
response = requests.post(url,json=after_scan_std_data)

print(response.status_code)
print(response.json())















