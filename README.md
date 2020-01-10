# RasPi-EnviropHAT-ThinkSpeak
Send data from RasPi with Enviro pHAT into ThinkSpeak with pyhton 

# Dependencies
There are two main dependencies: ThingSpeak and Enviro python libraries. For more information please go to:
* https://thingspeak.readthedocs.io/en/latest/
* https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-enviro-phat

Installation is perplexing... :

```
pip3 install thingspeak
curl https://get.pimoroni.com/envirophat | bash
```

The script uses Enviro pHAT for Raspberry Pi to measure light, RGB color, magnetic measurement, heading, temperature and atmospheric pressure. The data are printed on stdout and passed to a ThingSpeak Chanell for graphing. All measurements are cut to one decimal place (except for magnetic measurement). The atm pressure is in hPa.  

### The structure is CSV, semicolon separated: 

```
UNIX timestamp;ISO date; light; rgb; motion; heading; temp (celsius); pressure (hPa)
```

### Example:

``` 
unixtimest;date in ISO format........;LUX.;Rgb,rGb,rgB;Magnetometering...............................;Compa;temp;press
1578576608;2020-01-09T14:30:07.703674;90.0;119,102,102;0.0137939453125,0.3582763671875,0.956298828125;135.6;22.4;983.0
```
I call the Python from a shell script via crontab:

```
$ crontab -l 
*/2 * * * * /path/to/update-ts-enviro.sh

$ cat /path/to/update-ts-enviro.sh
#!/bin/bash

/usr/bin/python3 /path/to/print-update-thingspeak-enviro.py >> /logging/path/logs/enviro.csv

```
