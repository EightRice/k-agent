# import json
# import binascii
# lambda_code='''(lambda %new_handler (unit) : unit
#   {
#     DROP;
#     NIL operation;
#     PAIR;
#   })'''
# # Example Michelson code
# michelson_code = lambda_code

# lines = lambda_code.strip().split(';')
# micheline = {'parameter': lines[0].split()[1], 'storage': lines[1].split()[1], 'code': lines[2].strip()}
# micheline_json = json.dumps(micheline)
# encoded_bytes = micheline_json.encode('utf-8')
# hex_string = binascii.hexlify(encoded_bytes).decode('utf-8')
# print(hex_string)
testnet1="https://ghostnet.ecadinfra.com"
testnet2="https://rpc.ghostnet.teztnets.com"

from pytezos import pytezos
from dotenv import dotenv_values
# Load the .env file
env_vars = dotenv_values(".env")
private_key=env_vars.get("TEZOS_WALLET_1")
pytezos = pytezos.using(key=private_key, shell=testnet1)
# Define the contract address
contract_address = 'KT1VG3ynsnyxFGzw9mdBwYnyZAF8HZvqnNkw' #DAO Thursday Bug Hunt
# contract_address = 'KT1Je4UBengJdFq28TnecpsmiR73Au4bG9U6' #simple function contract
# Load the contract
contract = pytezos.contract(contract_address)

import json
import binascii
lambda_code='''(lambda %new_handler (unit) : unit
  {
    DROP;
    NIL operation;
    PAIR;
  })'''
# Example Michelson code
michelson_code = lambda_code

lines = lambda_code.strip().split(';')
micheline = {'parameter': lines[0].split()[1], 'storage': lines[1].split()[1], 'code': lines[2].strip()}
micheline_json = json.dumps(micheline)
encoded_bytes = micheline_json.encode('utf-8')
hex_string = binascii.hexlify(encoded_bytes).decode('utf-8')


def call_contract(proposal_metadata):
    global hex_string
    public_key="tz1T5kk65F9oZw2z1YV4osfcrX7eD5KtLj3c"
    mers=False
    something=None
    global stuff
    try:
        result = contract.propose(public_key, 10000, proposal_metadata ).send(min_confirmations=1)
        mers=True
    except Exception as e:
        print("exception: ",e)
        something=e
    if not mers:
        return something
    else:
        return "Transaction submitted."
call_contract(proposal_metadata=hex_string)