def create_add_handler_proposal(handler_name, code, handler_check):
    return {
        "prim": "Pair",
        "args": [
            {
                "prim": "Pair",
                "args": [
                    {"prim": "Lambda", "args": [code]},  # Placeholder for actual Michelson code
                    {"prim": "Lambda", "args": [handler_check]}  # Placeholder for actual Michelson code
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

# Example usage
handler_name = "example_handler"
code = "..."  # Actual Michelson code would go here
handler_check = "..."  # Actual Michelson code would go here

proposal = create_add_handler_proposal(handler_name, code, handler_check)
call_data = create_propose_call_data("tz1...", 1000000, proposal)

print(call_data)