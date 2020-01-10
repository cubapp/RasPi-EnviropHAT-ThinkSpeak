# RasPi-EnviropHAT-ThinkSpeak
Send data from RasPi with Enviro pHAT into ThinkSpeak with pyhton 

# Dependencies
thingspeak Python library
enviro Python library 

The script uses Enviro pHAT for Raspberry Pi to measure light, RGB color, magnetic measurement, heading, temperature and atmospheric pressure. The data are printed on stdout and passed to a ThingSpeak Chanell for graphing. All measurements are cut to one decimal place (except for magnetic measurement). The atm pressure is in hPa.  
