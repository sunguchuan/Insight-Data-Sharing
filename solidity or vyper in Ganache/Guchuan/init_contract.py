import web3
from web3 import Web3
import json
import codecs
from operations import w3, deploy,data,transact
import sys
import ipfsapi
import hashlib

def create_hash(file):  #CREATE A cryptographic HASHID FROM IPFS SERVER
    try:
        connect = ipfsapi.connect('127.0.0.1',5001)  #LOCAL IPFS SERVER, PREVOUSLY INSTALLED
        print("Successful connected to IPFS nectwork")
    except Exception as e:
        print("Unexpected Error, on IPFS::")
        print(e)
        exit(-1)

    res = connect.add(file)
    if res["Hash"]:
        return res["Hash"]
    else:
        return None

#def revoke(address):
    #print('Contract address:',address)
    #return transact(address,data['abi'],'revoke',source=w3.eth.accounts[0])

if __name__=='__main__':    # arguments:fingerprint file name
    id=create_hash(sys.argv[1])
    print('Actural ID:',id)
    address=deploy(w3.eth.accounts[2])
    print('Contract deployed, the address is:',address)
