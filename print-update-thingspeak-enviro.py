#!/usr/local/bin/python3 
from envirophat import light, motion, weather, leds
import thingspeak
from datetime import datetime

# Structure of the record - semicolon separated:
# UNIX timestamp;ISO date; light; rgb; motion; heading; temp (celsius); pressure (hPa)
# Example:
# unixtimest;date in ISO format........;LUX.;Rgb,rGb,rgB;Magnetometering...............................;Compa;temp;press
# 1578576608;2020-01-09T14:30:07.703674;90.0;119,102,102;0.0137939453125,0.3582763671875,0.956298828125;135.6;22.4;983.0

# your ThnkSpeak Channel and API Write Key
channel_id="123456"
api_key="123456ASDFGHJKLP"
thingspeak_data = {}
try:
    now = datetime.now()
    ch = thingspeak.Channel(channel_id, api_key)
    timestamp = round(datetime.timestamp(now))
    cas = now.isoformat()
    leds.off()
    lux = light.light()
    rgb = str(light.rgb())[1:-1].replace(' ', '')
    leds.on()
    acc = str(motion.accelerometer())[1:-1].replace(' ', '')
    heading = motion.heading()
    temp = weather.temperature()
    press = round(weather.pressure()/100)
    print('%s;%s;%.1f;%s;%s;%.1f;%.1f;%.1f' % (timestamp,cas,lux, rgb, acc, heading, temp, press))
    thingspeak_data['field1'] = cas
    thingspeak_data['field2'] = lux
    thingspeak_data['field3'] = rgb
    thingspeak_data['field4'] = acc
    thingspeak_data['field5'] = heading
    thingspeak_data['field6'] = temp
    thingspeak_data['field7'] = press
    response = ch.update(thingspeak_data)
    leds.off()

except KeyboardInterrupt:
    leds.off()
