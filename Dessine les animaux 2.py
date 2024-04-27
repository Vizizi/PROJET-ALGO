import paho.mqtt.client as mqtt
import turtle
import json

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "victor")
client.connect("srv-lora.isep.fr")
#client.connect("broker.hivemq.com")
turtle.penup()
def on_message_callback(client_inst, userdata, message):
    # Décoder le message JSON envoyé par la carte arduino
    print(message.payload)
    try:
        data = json.loads(message.payload)
    except json.JSONDecodeError as e:
        print(f"Erreur de décodage JSON - {e}")
        return

    # Vérifier si le message contient l'objet "message"
    if "object" in data and "message" in data["object"]:
        message_content = data["object"]["message"]

        # Vérifier si le message commence par "F"
        if message_content.startswith("Daisy"):
            # Séparer les parties du message
            parts = message_content.split(":")
            if len(parts) == 3:
                name, x, y = parts

                # Déplacer la tortue à la position spécifiée
                try:
                    turtle.goto(int(x), int(y))
                    turtle.dot(10, 'blue')
                    # Message si l'anmial sort de l'enclos
                    if int (x) > 200 :
                        print ("Daisy est sortie")
                    if int (x) < -200 :
                        print ("Daisy est sortie")
                    if int (y) > 200 :
                        print ("Daisy est sortie")
                    if int (y) < -200 :
                        print ("Daisy est sortie")
                except ValueError as e:
                    print(f"Erreur lors du déplacement de la tortue - {e}")

        elif message_content.startswith("Trevor"):
             # Séparer les parties du message
             parts = message_content.split(":")
             if len(parts) == 3:
                 name, x, y = parts

                 # Déplacer la tortue à la position spécifiée
                 try:
                     turtle.goto(int(x), int(y))
                     turtle.dot(10, 'pink')
                     # Message si l'anmial sort de l'enclos
                     if int(x) > 200:
                         print("Trevor est sortie")
                     if int(x) < -200:
                         print("Trevor est sortie")
                     if int(y) > 200:
                         print("Trevor est sortie")
                     if int(y) < -200:
                         print("Trevor est sortie")
                 except ValueError as e:
                     print(f"Erreur lors du déplacement de la tortue - {e}")


        elif message_content.startswith("Medor"):
            # Séparer les parties du message
            parts = message_content.split(":")
            if len(parts) == 3:
                name, x, y = parts

                # Déplacer la tortue à la position spécifiée
                try:
                    turtle.goto(int(x), int(y))
                    turtle.dot(10, 'black')
                    # Message si l'anmial sort de l'enclos
                    if int (x) > 200 :
                        print ("Medore est sortie")
                    if int (x) < -200 :
                        print ("Medore est sortie")
                    if int (y) > 200 :
                        print ("Medore est sortie")
                    if int (y) < -200 :
                        print ("Medore est sortie")
                except ValueError as e:
                    print(f"Erreur lors du déplacement de la tortue - {e}")
    else:
        print("Message JSON invalide")


client.on_message = on_message_callback

client.subscribe("#") #subscribe, donc on reçoit seulement les infos
client.loop_start()

turtle.mainloop()