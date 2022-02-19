import paho.mqtt.client as mqtt

def on_connect(client,userdata,flags,rc):
    # if rc=0 client is sucessful with broker

    if (rc==0):
        client.connected_flag=True
        print("Connected OK")
    else:
        print("Bad connection ",rc)

def on_subscribe(client,userdata,mid,granted_qos):
    print("Subscribed",str(mid),str(granted_qos))

def on_message(client,userdata,message):
    print("message.topic ",message.topic)
    if str(message.topic)!=pubtop:
        print(str(message.topic), str(message.payload.decode("utf-8")))

def on_disconnect(client,userdata,rc):
    if(rc!=0):
        print("Broker disconnected")

broker_add = "test.mosquitto.org"
port = 1883

client=mqtt.Client()

client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_disconnect = on_disconnect

client.connect(broker_add,port)

pubtop = input("Topic to publish")
subtop = input("Topic to be subscribed")


client.loop_start()
#genereate loop for continuous connectivity
client.subscribe(subtop)

while(1):
    chat = input()
    if(chat == 'Exit'):
        break
    elif(chat == 'subscribe'):
        new_subtop=input('Subscribe to topic ?')
        client.subscribe(new_subtop)
    elif(chat == 'Publish'):
        pubtop=input('Publish the new topic')
    else:
        client.publish(pubtop,chat)


client.disconnect()
client.loop_stop()
