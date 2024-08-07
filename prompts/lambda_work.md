In your working folder there is a file called baseDAOdocs.md that explains how the DAO contract works on Tezos. At the end of the file you have the actual relevant part of the implementation, written in LIGO. Your task is to figure out how to successfully make a contract call of type add_handler, and add another simple function to the contract. You will need to spin up a code execution environment where you can actually produce the logic that will generate the required hex string. Please use Tezos-specific libraries in order to maximize compatibility, but if those aren't available for some reason, use more generic libraries for encoding and parsing the content. When you have a viable hex string to try (that you didn't try before), use the contract_interaction tool. Know that the tool will relay the error from the RPC code if the call wasn't successfull, which is your cue to continue iterating. (code 111 means failure to unpack metadata). Feel free to search online for relevant information as you iterate to find the appropriate way to format and encode this parameter. Know that you won't find any specific information about this contract, or this method, so whatever you search for online will need to be more generic than this paricular contract. You should submit your iteration every time to the contract_interaction tool as a hex string. 





I think you should account for the actual method that unpacks the par
ameter and is at the end of the baseDAOdocs.md file. I mean that is the actual code on the other side, so it's not like we're completely in th
e dark here. Examine that code, figure out exactly what it is expecting
 and then produce the hex string accordingly. You might already be doin
g that (although not likely because you haven't made a successful call
yet). I'm saying all this because I'm noticing that you're not really t
rying to use any Michelson code in the code and the handler_check field
s. That might be required, or it might not, but the answer is in the co
de in the file baseDAOdocs.md . So please try to acquire a good underst
anding of that code, use online resources if needed. It might very well
 be that the code is faulty and will fail regardless of what parameters
 we send, and if that's your conclusion it will need to be well argumen
ted.


great, now let's change gears and focus our attention on figuring out if the endpoint is broken. You have the code in the baseDAOdocs.md file and you can search online to understand if it's written correctly. Or maybe you can use your builtin knowledge of the Ligo programming language. Either way, your task is to understand if the endpoint is broken or not. You can still make use of all your tools, including contract_interaction