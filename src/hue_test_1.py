#!/usr/bin/python

from phue import Bridge

hue_bridge = Bridge('192.168.1.134')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
hue_bridge.connect()

# Get the bridge state (This returns the full dictionary that you can explore)
hue_bridge.get_api()

# Prints if light 1 is on or not
#hue_bridge.get_light(1, 'on')
lights = hue_bridge.lights

# Print light names
for l in lights:
    print(l.name)


# Set brightness of lamp 1 to max
#hue_bridge.set_light(1, 'bri', 254)

# Set brightness of lamp 2 to 50%
#hue_bridge.set_light(2, 'bri', 127)

# Turn lamp 2 on
#hue_bridge.set_light(2,'on', True)

# You can also control multiple lamps by sending a list as lamp_id
#hue_bridge.set_light( [1,2], 'on', True)

# Get the name of a lamp
#hue_bridge.get_light(1, 'name')

# You can also use light names instead of the id
#hue_bridge.get_light('Kitchen')
#hue_bridge.set_light('Kitchen', 'bri', 254)

# Also works with lists
#hue_bridge.set_light(['Bathroom', 'Garage'], 'on', False)

# The set_light method can also take a dictionary as the second argument to do more fancy stuff
# This will turn light 1 on with a transition time of 30 seconds
#command =  {'transitiontime' : 300, 'on' : True, 'bri' : 254}
#hue_bridge.set_light(1, command)
