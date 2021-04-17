from os			import getenv as env
from client import Discord

client = Discord()
client.run(env('DC_TOKEN'))