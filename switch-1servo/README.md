# Light Switch - 1 servo
This project uses a servo to flick on and off a physical light switch via Home Assistant.
### Notes:
- Connect the servo to GPIO 1
- Fill in your WiFi network details
- Optionally, a button can be added on GPIO 14 to toggle on and off the lights!

### Home Assistant integration:
The light switch is configured as a command line switch in Home Assistant.

You will need to add the following to your `configuration.yaml`:
```yaml
command_line:
  - switch:
      name: Smart Lights (1 Servo)
      command_on: "/usr/bin/curl -X GET http://switch.ip.address/light/on"
      command_off: "/usr/bin/curl -X GET http://switch.ip.address/light/off"
      command_state: "/usr/bin/curl -X GET http://switch.ip.address/light/status"
      value_template: '{{ value_json.POWER =="ON"}}'
      unique_id: "D679HJKY8965TGKDSU0DS"
```

[![Open your Home Assistant instance and Open the ingress URL of an add-on.](https://my.home-assistant.io/badges/supervisor_ingress.svg)](https://my.home-assistant.io/redirect/supervisor_ingress/?addon=core_configurator)
