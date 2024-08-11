Here is the definition of a add_handler, which is a data structure in a Tezos smart contract: 

(pair %add_handler
  (pair (lambda %code
           (pair (pair (map %handler_storage string bytes) (bytes %packed_argument))
                 (pair %proposal_info
                    (address %from)
                    (nat %frozen_token)
                    (bytes %proposal_metadata)))
           (pair (pair (option %guardian address) (map %handler_storage string bytes))
                 (list %operations operation)))
        (lambda %handler_check (pair bytes (map string bytes)) unit))
  (string %name))

for full context, the data structure is defined here: https://github.com/tezos-commons/baseDAO/blob/be77424a313ace8e3f3c2748a1cbbc18acfe8001/src/variants/lambda/types.mligo#L63

You will need to interate upon the logic below to produce a hex string pertaining to this data structure. This will be an actual implementation, without any placeholders. DO NOT change the address (the 'from' parameter) or the value of 'frozen_token_amount' which is 10000. When you have a viable new hex string to try, use the contract_interaction tool. Know that the tool will relay the error from the RPC code if the call wasn't successfull, which is your cue to continue iterating. (code 111 means failure to unpack metadata). You should submit your iteration every time to the contract_interaction tool as a hex string. 
Here is your starting point:

import json

def create_add_handler_proposal(handler_name, code, handler_check):
    return {
        "prim": "Pair",
        "args": [
            {e
                "prim": "Pair",
                "args": [
                    {
                        "prim": "Lambda",
                        "args": [
                            {
                                "prim": "Pair",
                                "args": [
                                    {
                                        "prim": "Pair",
                                        "args": [
                                            {"prim": "map", "args": [{"prim": "string"}, {"prim": "bytes"}]},
                                            {"prim": "bytes"}
                                        ]
                                    },
                                    {
                                        "prim": "Pair",
                                        "args": [
                                            {"prim": "address"},
                                            {"prim": "nat"},
                                            {"prim": "bytes"}
                                        ]
                                    }
                                ]
                            },
                            {
                                "prim": "Pair",
                                "args": [
                                    {
                                        "prim": "Pair",
                                        "args": [
                                            {"prim": "option", "args": [{"prim": "address"}]},
                                            {"prim": "map", "args": [{"prim": "string"}, {"prim": "bytes"}]}
                                        ]
                                    },
                                    {"prim": "list", "args": [{"prim": "operation"}]}
                                ]
                            }
                        ],
                        "code": code
                    },
                    {
                        "prim": "Lambda",
                        "args": [
                            {
                                "prim": "Pair",
                                "args": [
                                    {"prim": "bytes"},
                                    {"prim": "map", "args": [{"prim": "string"}, {"prim": "bytes"}]}
                                ]
                            },
                            {"prim": "unit"}
                        ],
                        "code": handler_check
                    }
                ]
            },
            {"string": handler_name}
        ]
    }

def create_propose_call_data(proposer_address, frozen_token_amount, proposal):
    return {
        "entrypoint": "propose",
        "value": {
            "prim": "Pair",
            "args": [
                {"string": proposer_address},
                {"int": str(frozen_token_amount)},
                proposal
            ]
        }
    }

# Simple Michelson code for the handler
handler_code = [
    {"prim": "DROP"},
    {"prim": "PUSH", "args": [{"prim": "string"}, {"string": "Hello, World!"}]},
    {"prim": "PUSH", "args": [{"prim": "bytes"}, {"bytes": "0123"}]},
    {"prim": "PUSH", "args": [{"prim": "string"}, {"string": "example_key"}]},
    {"prim": "DIG", "args": [{"int": "2"}]},
    {"prim": "PUSH", "args": [{"prim": "map", "args": [{"prim": "string"}, {"prim": "bytes"}]}, []]},
    {"prim": "PUSH", "args": [{"prim": "option", "args": [{"prim": "address"}]}, {"prim": "None"}]},
    {"prim": "PAIR"},
    {"prim": "PAIR"},
    {"prim": "NIL", "args": [{"prim": "operation"}]},
    {"prim": "PAIR"}
]

# Simple Michelson code for the handler check
handler_check_code = [
    {"prim": "DROP"},
    {"prim": "UNIT"}
]

# Build the data structure
handler_name = "example_handler"

proposal = create_add_handler_proposal(handler_name, handler_code, handler_check_code)
call_data = create_propose_call_data("tz1T5kk65F9oZw2z1YV4osfcrX7eD5KtLj3c", 10000, proposal)

print(bytes(str(call_data),"utf-8").hex())