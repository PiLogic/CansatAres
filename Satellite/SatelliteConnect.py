from LoRaRF import SX126x
LoRa = SX126x()
LoRa.setSPI(0, 0, 7800000)
LoRa.setPins(22, 23, 26, 5, 25)
LoRa.begin()

message = "Hello CanSat!\0"
messageList = list(message)
for i in range(len(messageList)): 
    messageList[i] = ord(messageList[i])
counter = 0

LoRa.beginPacket()
LoRa.write(message, len(message)) 
LoRa.write(counter)                 
LoRa.endPacket()
LoRa.wait()
counter += 1