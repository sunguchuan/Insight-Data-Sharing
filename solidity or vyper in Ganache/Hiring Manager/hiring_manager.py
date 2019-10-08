import web3
from web3 import Web3
import json
# from web3.auto.gethdev import w3
from operations import w3, data, transact, get_return_value
import codecs
import rsa
import sys
import ipfsapi
import time
import os

def genkey():
	(pubkey,prikey)=rsa.newkeys(1024)
	pub=pubkey.save_pkcs1()
	pri=prikey.save_pkcs1()
	print('Public Key: ',pub)
	print('Private Key: ',pri)
	pubfile=open('pubkey.pem','wb')
	pubfile.write(pub)
	pubfile.close()
	prifile=open('prikey.pem','wb')
	prifile.write(pri)
	prifile.close()
	return pub

def decrypt_data(data,keyfile):
	prifile=open(keyfile,'rb')
	pri=prifile.read()
	prifile.close()
	prikey=rsa.PrivateKey.load_pkcs1(pri)
	data=codecs.decode(data,'hex')
	res=rsa.decrypt(data,prikey)
	res=res.decode()
	return res

def retrieve(hash):  #CREATE A cryptographic HASHID FROM IPFS SERVER
	try:
		connect = ipfsapi.connect('127.0.0.1',5001)  #LOCAL IPFS SERVER, PREVOUSLY INSTALLED
		print("Successful connected to IPFS nectwork")
	except Exception as e:
		print("Unexpected Error, on IPFS::")
		print(e)
		exit(-1)
	try:
		res = connect.get(hash)
		print('File has been downloaded')
	except Exception as e:
		print(e)
		exit(-1)
        
if __name__=='__main__':
	address=sys.argv[1]
	pub=genkey();
	tx_hash=transact(address,data['abi'],'register',argv={'pk':pub},source=w3.eth.accounts[1])
	if tx_hash:
		print('Registraction succeeded, tx hash: ',tx_hash)
	time.sleep(15)
	share=get_return_value(address,data['abi'],'get_data',argv={},source=w3.eth.accounts[1])
	decrypto=decrypt_data(share,'prikey.pem')
	if decrypto:
		print('The file\'s IPFS ID is: ',decrypto)
		retrieve(decrypto)
		os.system('evince '+decrypto)
