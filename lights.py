from phue import Bridge
from time import sleep


class ExtendedBridge(Bridge):
    ip = '10.0.1.101'

    def __init__(self, *args, **kwargs):
        super(ExtendedBridge, self).__init__(*args, **kwargs)
        self.connect()

    def create_group_from_name(self, name):
        lights = self.lights
        group_ids = [light.light_id for light in lights if light.name.startswith(name)]
        return self.create_group(name, group_ids)

    def sunrise(self, group='Main'):
        self.set_group(group, 'on', True, transitiontime=1)
        self.set_group(group, 'bri', 1, transitiontime=1)
        self.set_group(group, 'sat', 180, transitiontime=1)
        self.set_group(group, 'hue', 10000, transitiontime=1)
        self.set_group(group, 'sat', 50, transitiontime=3000)
        self.set_group(group, 'bri', 200, transitiontime=3000)

    def sunset(self, group='Main'):
        self.set_group(group, 'hue', 7000, transitiontime=6000)
        self.set_group(group, 'sat', 180, transitiontime=6000)
        self.set_group(group, 'on', False, transitiontime=12000)

    def off(self, group='Main'):
        self.set_group(group, 'on', False)

l = ExtendedBridge()


