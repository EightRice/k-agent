import json
import struct

# Michelson schema string
michelson_schema_string = """
(or 
  (or 
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
    (pair %execute_handler (string %handler_name) (bytes %packed_argument)))
  (string %remove_handler))
"""

# JSON data to encode
data_to_encode = {
  "add_handler": {
    "name": "example_handler",
    "code": {
      "prim": "PUSH",
      "args": [
        { "prim": "unit" },
        { "prim": "Unit" }
      ]
    },
    "handler_check": {
      "prim": "PUSH",
      "args": [
        { "prim": "unit" },
        { "prim": "Unit" }
      ]
    }
  }
}

# Function to encode Michelson data
def encode_michelson_data(data):
    def encode_prim(prim, args):
        encoded = b''
        if prim == 'Pair':
            # Assumes that args are encoded sequentially
            for arg in args:
                encoded += encode_michelson_data(arg)
        elif prim == 'string':
            encoded_string = args[0]
            length = len(encoded_string)
            encoded = struct.pack(">I", length) + encoded_string.encode()
        elif prim == 'bytes':
            encoded_bytes = args[0]
            encoded = bytes.fromhex(encoded_bytes)
        elif prim == 'unit':
            encoded = b'\x00'
        return encoded

    if isinstance(data, dict) and 'prim' in data:
        return encode_prim(data['prim'], data['args'])
    elif isinstance(data, dict) and 'string' in data:
        return encode_prim('string', [data['string']])
    elif isinstance(data, dict) and 'bytes' in data:
        return encode_prim('bytes', [data['bytes']])
    elif isinstance(data, dict) and 'unit' in data:
        return encode_prim('unit', [])

    raise ValueError("Unsupported Michelson data format")

# Wrap the data to match the expected format in the schema
wrapped_data = {
    "prim": "Pair",
    "args": [
        {"string": data_to_encode["add_handler"]["name"]},
        {
            "prim": "Pair",
            "args": [
                data_to_encode["add_handler"]["code"],
                data_to_encode["add_handler"]["handler_check"]
            ]
        }
    ]
}

# Encode data according to schema
packed_data = encode_michelson_data(wrapped_data)

# Convert to hex string
hex_string = packed_data.hex()

print("Packed Hex String:", hex_string)
