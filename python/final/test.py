import paho.mqtt.publish as publish

publish.single("CoreElectronics/test", "Hello", hostname="192.168.66.19")
publish.single("CoreElectronics/topic", "World!", hostname="192.168.66.19")
print("Done")