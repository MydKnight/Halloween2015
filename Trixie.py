__author__ = 'madsens'
from ola.ClientWrapper import ClientWrapper
import array

def DmxSent(state):
  wrapper.Stop()

universe = 1
data = array.array('B', [10, 50, 255])
wrapper = ClientWrapper()
#client = wrapper.Client()
#client.SendDmx(universe, data, DmxSent)
#wrapper.Run()