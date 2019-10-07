# Insight-Data-Sharing
Enabling secure information transmission via smart contract
#### Guchuan Sun
## Project motivation
As the network environment is insecure nowadays. People take risks when they are transmitting sensitive information because malicious users can steal the information by monitoring the channels and blockchains. My project aims at creating a trust-worthy, light-weight and encrypted environment that enables secure information transmission.

## Solution
In order to achieve this goal, there are mainly 3 tools used in my project:
### Smart contract
The reason of using smart contract is that it provides the trust-worth: After deployed on Ethereum, a smart contract becomes an immutable program, whose source code and stored data are public. As a result, it only does what it is told to and everone can check its correctness. For more details you can refer to this [white paper](https://github.com/ethereum/wiki/wiki/White-Paper).
### IPFS
IPFS (InterPlanet File System) is a distributed system where files are divided to blocks, the hashes of which aggregate to a Merkle tree. The root hash of the Merkle is the index to this file and only users who have this hash can download the file. It provides a fast, secure way of file transmission. Besides, it is free to use, which makes it much cheaper than Ethereum in terms of large file transmission. You may refer to the introduction of IPFS [here](https://github.com/ipfs/ipfs).
### RSA key pair
RSA key pair is a classic encryption tool and is widely used in crytocurrencies. There is no need to emphasize its security. With the help of RSA key pairs, the sensitive plain text become cipher text that is uninterpretable to anyone except key holders. There is no need to data exposure into Ethereum.

## Flow chart
Here is a example of sharing my resume to the hiring manager, the process is shown in the below image:
![pic](/images/Flow_chart.png)

## Technical support
There are smart contracts implemented with Solidity, Vyper and TypeScript. For details of running code in different environments, please check details in the corresponding folders.
