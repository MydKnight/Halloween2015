__author__ = 'madsens'
import DMX

dmx=dmx512.dmx
dmx.set_channel(1,255)
dmx.set_channel(419,39)
dmx.send()

dmx.channel[21]