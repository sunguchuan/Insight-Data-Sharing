# Instructions of running test cases
## Environment requirements
It is strongly recommened that the test is run in Linux or MacOS.
### Ganache-cli
You need to run a Ganachi Ethereum testnet. You may refer [here](https://github.com/trufflesuite/ganache-cli) for more details of setting up the testnet.
### Python3
The application is implemented in python3. There are also some extra modules needed, you may use pip to install them:
* web3
* rsa
* ipfsapi
## Run test
In ./Guchuan, run the following command in the terminal to deploy the smart contract:

```
python3 init_contract.py test.txt
```
After a few seconds, the contract is deployed and the terminal prints the <address> of this contract.
In ./Hiring Manager, run the following command in the terminal to generate an RSA key pair and share the public key to the contract:

```
python3 hiring_manager.py <address>
```
Within 15 seconds, in ./Guchuan, run the following command to retrieve the shared key, upload file to IPFS, do encryption, and upload encrypted IPFS hash:

```
python3 guchuan_share.py <address>
```
You can check in ./Hiring Manager that the file is downloaded and pops out!
