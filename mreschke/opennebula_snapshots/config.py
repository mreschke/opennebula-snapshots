import os
from dotenv import load_dotenv
load_dotenv()

def env(variable, default = None):
    if variable in os.environ:
        return os.getenv(variable)
    else:
        return default

# OpenNebula Configs
host = env('OPENNEBULA_HOST', 'localhost')
port = env('OPENNEBULA_PORT', 22633)
protocol = env('OPENNEBULA_PROTOCOL', 'http')
path = env('OPENNEBULA_PATH', 'RPC2')
user = env('OPENNEBULA_USER', 'oneadmin')
password = env('OPENNEBULA_PASSWORD', 'password')

