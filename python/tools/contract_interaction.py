import json
import binascii
import requests
from dotenv import dotenv_values
import csv
# Load the .env file
env_vars = dotenv_values(".env")
filename = 'tries.txt'
private_key=env_vars.get("TEZOS_WALLET_1")
rpc1="https://rpc.ghostnet.teztnets.com"
rpc2='https://ghostnet.ecadinfra.com'
last_metadata=b""
from python.helpers.tool import Tool, Response
already_tried=[]
with open(filename, 'r') as file:
    # Read each line and strip any trailing newline characters
    already_tried = [line.strip() for line in file]
last_rpc=rpc1
BASE_URL = "http://127.0.0.1:5000"
class ContractInteraction(Tool):
    def execute(self, proposal_metadata="", **kwargs):
        response = requests.get(f"{BASE_URL}/hello", params={"metadata":proposal_metadata})
        content = json.loads(response.content)
        return Response(message=str(content), break_loop=False)