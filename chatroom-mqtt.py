import paho.mqtt.client as mqtt

#The function defines here are predefined functions of the paho library, which we override to make them according to our needs.
def on_connect(client,userdata,flags,rc):
    # if rc=0 marks a successful connection of the client to the broker.rc, the result of the publishing. It could be MQTT_ERR_SUCCESS to indicate success,
    # MQTT_ERR_NO_CONN if the client is not currently connected, or MQTT_ERR_QUEUE_SIZE when max_queued_messages_set is used to
    # indicate that message is neither queued nor sent.

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
