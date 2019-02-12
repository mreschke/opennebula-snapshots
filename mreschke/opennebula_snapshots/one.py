import pyone
from . import config
from .utils import dump, dd

class Opennebula:

    ALL_RESOURCES = -2
    ACTIVE_STATE = 3

    def __init__(self, host=config.host, port=config.port,
                 protocol=config.protocol, path=config.path,
                 user=config.user, password=config.password):

        self.host = host
        self.port = port
        self.protocol = protocol
        self.path = path
        self.user = user
        self.password = password
        self.vms = None

        self.api = pyone.OneServer(self.url(), session=config.user + ":" + config.password)


    #def connect(self):


    def listvms(self):
        # Get all ACTIVE VMs
        if self.vms is None:
            self.vms = self.api.vmpool.info(self.ALL_RESOURCES, -1, -1, self.ACTIVE_STATE).VM

        return self.vms

    def find(self, name):
        self.listvms()
        for vm in self.vms:
            if vm.NAME == name:
                return vm

    def show(self, id):
        # Get all ACTIVE VMs
        # To see XML use server command: onevm show 61 --xml
        return self.api.vm.info(id)

    def url(self):
        return self.protocol + "://" + self.host + ":" + str(self.port) + "/" + self.path
