import click
from . import config
from .one import Opennebula
from .utils import dump, dd

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    """
    \b
    mreschke.opennebula-snapshots
    Copyright (c) 2019 Matthew Reschke
    License http://mreschke.com/license/mit
    """
    pass

@cli.command()
def list():
    """List all ACTIVE VMs"""

    #vms = one.listvms()
    #for vm in vms:
        #dd(vm.toxml())
    #vm = one.show(61)

@cli.command()
@click.option('--name', help="VM name", required=True)
def snapshot(name):
    """Create Live Qcow2 Snapshot using libvirt"""
    one = Opennebula()
    vm = one.find(name)
    if vm is None:
        print(f"VM with name {name} not found")
        exit()

    print(f"Found VM {name}")
    #dd(vm.TEMPLATE, vm.NAME, vm.ID)


    #dd('hi')

# Backup one live KVM qcow2 virtual machine image snapshot using virsh snapshot-create-as
# mReschke 2019-02-11



# Connect to OpenNebula RPC API Url
#a = One()
#one = a.connect()


#for vm in vms.VM:
    #dd(vm.TEMPLATE)

# Initiate cli
if __name__ == '__main__':
    cli()
