import network
import asyncio
import socket
import time
from picozero import Servo
from machine import Pin

# Wi-Fi credentials
ssid = 'Your WiFi network name'
password = 'Your WiFi password'

# Initialize variables
state = "OFF"
servo = Servo(1)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

# HTML template for the webpage
def webpage(random_value, state):
    html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Smart Switch</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
        </head>
        <body>
            <h1>It works!</h1>
        </body>
        </html>
        """
    return str(html)

# Init Wi-Fi Interface
def init_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    # Connect to your network
    wlan.connect(ssid, password)
    # Wait for Wi-Fi connection
    connection_timeout = 10
    while connection_timeout > 0:
        print(wlan.status())
        if wlan.status() >= 3:
            break
        connection_timeout -= 1
        print('Waiting for Wi-Fi connection...')
        time.sleep(1)
    # Check if connection is successful
    if wlan.status() != 3:
        print('Failed to connect to Wi-Fi')
        return False
    else:
        print('Connection successful!')
        network_info = wlan.ifconfig()
        print('IP address:', network_info[0])
        return True

# Asynchronous functio to handle client's requests
async def handle_client(reader, writer):
    global state
    global response

    print("Client connected")
    request_line = await reader.readline()
    print('Request:', request_line)
    
    # Skip HTTP request headers
    while await reader.readline() != b"\r\n":
        pass
    
    request = str(request_line, 'utf-8').split()[1]
    print('Request:', request)
    # Process the request and update variables
    if request == '/light/status':
        response = '{"POWER": "%s"}' % state
    elif request == '/light/on':
        print('LED on')
        servo.value = 0.15
        state = 'ON'
        response = '{"POWER": "%s"}' % state
    elif request == '/light/off':
        print('LED off')
        servo.value = 0.4
        state = 'OFF'
        response = '{"POWER": "%s"}' % state


    # Send the HTTP response and close the connection
    writer.write('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    writer.write(response)
    await writer.drain()
    await writer.wait_closed()
    print('Client Disconnected')


async def main():
    global state
    if not init_wifi(ssid, password):
        print('Exiting program.')
        return
    
    # Start the server and run the event loop
    print('Setting up server')
    server = asyncio.start_server(handle_client, "0.0.0.0", 80)
    asyncio.create_task(server)
    while True:
        # Add other tasks that you might need to do in the loop
        await asyncio.sleep(0.1)
        if button.value():
            if state == 'OFF':
                servo.value = 0.15
                state = 'ON'
            elif state == 'ON':
                servo.value = 0.4
                state = 'OFF'
            time.sleep(0.2)
# Create an Event Loop
loop = asyncio.get_event_loop()
# Create a task to run the main function
loop.create_task(main())

try:
    # Run the event loop indefinitely
    loop.run_forever()
except Exception as e:
    print('Error occured: ', e)
except KeyboardInterrupt:
    print('Program Interrupted by the user')

