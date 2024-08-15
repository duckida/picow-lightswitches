# Light Switch - 2 servos
This project uses 2 servos to flick on and off a physical light switch via Home Assistant.
### Notes:
- Connect the top servo to GPIO0 and the bottom servo to GPIO1
- Fill in your WiFi network details

### Home Assistant integration:
The light switch is configured as a command line switch in Home Assistant. Change the IP to match your Pico W.

You will need to add the following to your `configuration.yaml`:
```yaml
command_line:
  - switch:
      name: Smart Switch (2 servos)
      command_on: "/usr/bin/curl -X GET http://pico.w.ip.address/light/on"
      command_off: "/usr/bin/curl -X GET http://pico.w.ip.address/light/off"
      command_state: "/usr/bin/curl -X GET http://pico.w.ip.address/light/status"
      value_template: '{{ value_json.POWER =="ON"}}'
      unique_id: "D87RLKJFKSHDF242308EFUI"
```

[![Open your Home Assistant instance and Open the ingress URL of an add-on.](https://my.home-assistant.io/badges/supervisor_ingress.svg)](https://my.home-assistant.io/redirect/supervisor_ingress/?addon=core_configurator)
