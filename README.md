# Hyperledger besu Multiple-tenency
This network use Hyperledger besu and Tessera for using to send private transaction to the node that want privacy in blockchain network
that mean another node in network can't see private transaction 
and setting privacy transaction to multi-tenant network


## How private transaction work?

private transaction diagram (Low level)

![besuAndTesseraDiagram drawio](https://user-images.githubusercontent.com/73258014/195951920-17386857-7483-4293-94a0-7761cdacb8eb.png)

breifly recap!

private transaction on hyperledger besu is integration with tessera. tessera will use the same key pair as besu node and decrypt transaction with signature solution and send to tessera endpoint node that we want to do some private transaction by P2P network. when finished P2P process tessera will return transaction to besu node that return transaction call enclave transaction. besu node will be sending transaction to next process call minning for distribute transaction to all nodes when transaction distributed the only node that can be read data in enclave transaction is endpoint node


example Web3Quorum sending transaction

```sh
const Web3 = require("web3");
const Web3Quorum = require("web3js-quorum");
const web3 = new Web3Quorum(new Web3("http://127.0.0.1")) // besu endpoint network 

const contractOption = {
    data: '0x123',// conrtract byte code 
    privateFrom: "tesseraNode1Publickey", //tesseraNode1Publickey
    privateFor: ["tesseraNode2PublicKey"], //tesseraNode2PublicKey
    privateKey: "besuNode1PrivateKey" //besuNode1PrivateKey
};
web3.priv.generateAndSendRawTransaction(contractOption);

```


## Multiple-tenency Blueprint
![NewDiagram drawio](https://user-images.githubusercontent.com/73258014/196552859-6b35e930-e245-40bc-aff1-a984ffc0cc43.png)

user that need to access to tenant will authentication in besu provide 2 way to authenticate that is username password and JWT
when finished of authentication user will resolve token to use for request api data in tenant


## Installation

install besu and tessera

```sh
$ brew install besu
$ brew install libsodium
```
Download tessera distribute from https://github.com/ConsenSys/tessera/releases/tag/tessera-22.1.7

```sh
$ tar xvf tessera-[version].tar
$ export PATH=$PATH:tessera-[version]/bin
$ tessera help
```
or move tessera directory to network directory and use 
```sh
$ ../../tessera-22.1.7/bin/tessera help

```
## Start network 

start besu node 
```sh
$ besu --data-path=data --genesis-file=../genesis.json [--option]
```
hyperledger besu private network option
https://besu.hyperledger.org/en/stable/private-networks/reference/cli/options/#specify-options

start tessera node 
```sh
$ tessera -configfile tessera.conf
or 
$ ../../tessera-22.1.7/bin/tessera -configfile tessera.conf

```
## Authentication

What you prepare for authenticatate
- Type of secret key
- Payload
- secret key

secert key (RSA)

```sh
openssl genrsa -out privateRSAKey.pem 2048
```
public RSA key
```sh
openssl rsa -pubout -in privateRSAKey.pem -pubout -out publicRSAKey.pem
```

payload
```sh
{ "permissions":["*:*"],
  "privacyPublicKey":tesseraNode_publicKey,
  "exp": 1600899999002
 }
```
generate JWT token
```sh
python3 generateJWT.py
```
example out put

<img width="400" alt="jwtExample" src="https://user-images.githubusercontent.com/73258014/195951260-ca169da1-b7a2-445b-9e58-90bc234df9ae.png">

example to use token
```sh
curl -X POST -H 'Authorization: Bearer <JWT_TOKEN>' -d '{"jsonrpc":"2.0","method":"<API_METHOD>","params":[],"id":1}' <JSON-RPC-http-hostname:port>
```
you can use in postman for easily way

## Hyperledger besu API
https://api.besu.hyperledger.org

## Tessera API
https://consensys.github.io/tessera/#tag/quorum-to-tessera/operation/getDecryptedPayloadJson

## Following the hyperledger besu private network document 
https://besu.hyperledger.org/en/stable/private-networks/

## Following Tessera private transaction manager document
https://docs.tessera.consensys.net/en/stable/
