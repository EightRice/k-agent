import { packDataBytes } from '@taquito/michel-codec';

async function proposeHandler() {
 const Tezos = new TezosToolkit('https://rpc.ghostnet.teztnets.com');
  
  // Set up the handler code
  const handlerCode = `{ UNPAIR ;
      UNPAIR ;
      PUSH string "example_key" ;
      PUSH bytes 0x01020304 ;
      DIG 3 ;
      SOME ;
      DIG 2 ;
      UPDATE ;
      PAIR ;
      PUSH (option address) None ;
      PAIR ;
      NIL operation ;
      PAIR }`;

  // Set up the handler check function
  const handlerCheck = `{ DROP ; UNIT }`;

  // Create the add_handler proposal
  const addHandlerProposal = {
    prim: 'Pair',
    args: [
      {
        prim: 'Pair',
        args: [
          { string: handlerCode },
          { string: handlerCheck }
        ]
      },
      { string: 'example_handler' }
    ]
  };

  // Pack the add_handler proposal
  const packedProposal = packDataBytes(addHandlerProposal, { prim: 'pair', args: [{ prim: 'pair', args: [{ prim: 'lambda', args: [{ prim: 'pair', args: [{ prim: 'pair', args: [{ prim: 'map', args: [{ prim: 'string' }, { prim: 'bytes' }] }, { prim: 'bytes' }] }, { prim: 'pair', args: [{ prim: 'address' }, { prim: 'nat' }, { prim: 'bytes' }] }] }, { prim: 'pair', args: [{ prim: 'pair', args: [{ prim: 'option', args: [{ prim: 'address' }] }, { prim: 'map', args: [{ prim: 'string' }, { prim: 'bytes' }] }] }, { prim: 'list', args: [{ prim: 'operation' }] }] }] }, { prim: 'lambda', args: [{ prim: 'pair', args: [{ prim: 'bytes' }, { prim: 'map', args: [{ prim: 'string' }, { prim: 'bytes' }] }] }, { prim: 'unit' }] }] }, { prim: 'string' }] });

  // Set up the propose parameters
  const proposeParams = {
    from: 'tz1T5kk65F9oZw2z1YV4osfcrX7eD5KtLj3c', // Replace with actual proposer address
    frozen_token: 10000, // 1 tez worth of tokens, adjust as needed
    proposal_metadata: packedProposal.bytes
  };

  console.log(proposeParams)

  // // Get the contract instance
  // const contract = await Tezos.contract.at('KT1VG3ynsnyxFGzw9mdBwYnyZAF8HZvqnNkw');

  // // Estimate gas and storage
  // const estimation = await contract.methods.propose(proposeParams.from, proposeParams.frozen_token, proposeParams.proposal_metadata).estimate();

  // console.log('Estimated gas:', estimation.totalCost, 'mutez');
  // console.log('Estimated storage:', estimation.storageLimit, 'bytes');

  // // Call the propose method
  // try {
  //   const op = await contract.methods.propose(proposeParams.from, proposeParams.frozen_token, proposeParams.proposal_metadata).send();
  //   await op.confirmation();
  //   console.log('Transaction confirmed:', op.hash);
  // } catch (error) {
  //   console.error('Error:', error);
  // }
}

proposeHandler();