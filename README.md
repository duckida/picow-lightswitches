# picow-lightswitches
Pico W code to use servos to turn on and off the lights via Home Assistant

To learn more about the different types of switches and learn to add them to Home Assistant, open their folders.
The types are:
- [Smart Switch (on and off)](https://github.com/duckida/picow-lightswitches/tree/main/switch-1servo)
- [Smart Switch with 2 servos (older version of Smart Switch with 1 servo)](https://github.com/duckida/picow-lightswitches/tree/main/switch-2servos)
- [Dimmer Switch](https://github.com/duckida/picow-lightswitches/tree/main/dimmer)

The Smart Switches are powered by MicroPython, while the dimmer uses ESPHome.

### API control
The smart switches use HTTP endpoints to turn on and off the lights.

`http://switch.ip.address/light/on` - turns on the light and returns status

`http://switch.ip.address/light/off` - turns off the light and returns status

`http://switch.ip.address/light/status` - returns the light status (format `{"POWER": "ON"}`)
