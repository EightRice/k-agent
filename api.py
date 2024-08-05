from flask import Flask, jsonify, request
from pytezos import pytezos
import json
import binascii
from dotenv import dotenv_values
app = Flask(__name__)
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



@app.route('/hello')

def hello():
    metadata = request.args.get('metadata')
    last_rpc=rpc1
    proposal_metadata=str(metadata)
    global filename
    # The new element to be added
    global pytezos
    global last_metadata
    currentRPC=""
    if last_rpc==rpc1:
        currentRPC=rpc2
    else:
        currentRPC=rpc1
    pytezos = pytezos.using(key=private_key, shell=currentRPC)
    # # Define the contract address
    contract_address = "KT1VG3ynsnyxFGzw9mdBwYnyZAF8HZvqnNkw"
    # # Load the contract
    contract = pytezos.contract(contract_address)
    if proposal_metadata in already_tried:
        return jsonify({"BLOCKED BY SCRIPT": "This bytes sequence has already been tried and it didn't work."})
    # print("last metadata "+str(last_metadata))
    # print("curr metadata "+str (proposal_metadata))
    last_metadata=proposal_metadata
    print("*** USING CONTRACT INTERACTION TOOL ***")
    public_key="tz1T5kk65F9oZw2z1YV4osfcrX7eD5KtLj3c"
    mers=False
    something=None
    try:
        result = contract.propose(public_key, 10000, bytes(proposal_metadata, "utf-8")).send(min_confirmations=1)
        mers=True
    except Exception as e:
        print("exception: ",e)
        something=e
    if not mers:
        new_element = str(proposal_metadata)
        # Open the file in append mode and write the new element
        with open(filename, 'a') as file:
            file.write(new_element + "\nfailed with: "+ str(something) +'\n\n')
        return jsonify({"ERROR FROM CHAIN": f"{something}"})
    else:
        return jsonify({"SUCCESS": "Operation submitted!"})

    



if __name__ == '__main__':
    app.run(debug=True)