import web3
from web3 import Web3
import json
# from web3.auto.gethdev import w3
from operations import w3, data, transact, get_return_value
import codecs
import rsa
import sys

def encrypt_data(info,key):
	pubkey=rsa.PublicKey.load_pkcs1(key)
	res=rsa.encrypt(info.encode(),pubkey)
	res=codecs.encode(res,'hex')
	return res

if __name__=='__main__':
	address=sys.argv[1]
	pub=get_return_value(address,data['abi'],'get_pk',argv={'alice':w3.eth.accounts[1]},source=w3.eth.accounts[2])
	if pub:
		print('Get public key succeeded')
	encrypto=encrypt_data('QmbQ7odTPcFdtnuVTvWPdsskxenB7NxmehVNRbWpEZJreR',pub)
	print(encrypto)
	tx_hash=transact(address,data['abi'],'share_data',argv={'alice':w3.eth.accounts[1],'data':encrypto},source=w3.eth.accounts[2])
	if tx_hash:
		print('Data is shared, the transaction hash is: ',tx_hash)
	
