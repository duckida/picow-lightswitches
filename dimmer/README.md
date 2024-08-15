# Dimmer Switch (ESPHome)
This project uses a Pico W and a servo to turn a dimmer.

### How to install:
1. Install ESPHome on Home Assistant
2. Create a new device
3. Add the contents of `esphome-config.yaml` to your ESPHome device
4. Install the code
5. Home Assistant should automatically detect the device.

### Home Assistant setup:
This project uses a template light to control the servo

You will need to add the following to your configuration.yaml:
```yaml
light:
  - platform: template
    lights:
      glowdim_2024:
        unique_id: 'glowdim-2024'
        friendly_name: "Dimmer Switch"
        level_template: |-
          {% set servo_min = -100 %}
          {% set servo_max = 100 %}
          {% set light_brightness_min = 0 %}
          {% set light_brightness_max = 255 %}
          {% set input_value = states('number.dimmer_light_pico_servo_control') | float %}
          {% set output_value = ((input_value - servo_min) / (servo_max - servo_min)) * (light_brightness_max - light_brightness_min) %}
          {{output_value}}
        turn_on:
          - action: number.set_value
            data:
              entity_id: number.dimmer_light_pico_servo_control
              value: 100
        turn_off:
          - action: number.set_value
            data:
              entity_id: number.dimmer_light_pico_servo_control
              value: -100
        set_level:
          - action: number.set_value
            data:
              entity_id: number.dimmer_light_pico_servo_control
              value: >
               {% set brightness = brightness | int %}
               {% set converted_number = (brightness / 255.0 * 200) - 100 %}
               {{ converted_number | round(0) }}
```

[![Open your Home Assistant instance and Open the ingress URL of an add-on.](https://my.home-assistant.io/badges/supervisor_ingress.svg)](https://my.home-assistant.io/redirect/supervisor_ingress/?addon=core_configurator)
