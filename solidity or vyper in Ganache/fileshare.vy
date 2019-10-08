key_share: map(address,string[300])  #stores pks from alice
data_share: map(address,string[300])    #stores data from bob
owner: address

@public
def __init__(_proposalNames: bytes32[2]):
    self.owner = msg.sender

@public
def register (pk: string[300]):
    self.key_share[msg.sender]=pk

@public
@constant
def get_pk (alice: address) -> string[300]:
    assert(msg.sender==self.owner)
    assert(len(self.key_share[alice])>0)
    return self.key_share[alice]

@public
def share_data (alice: address, data: string[300]) :
    assert(msg.sender==self.owner)
    self.data_share[alice]=data

@public
@constant
def get_data () -> string[300]:
    assert(len(self.data_share[msg.sender])>0)
    return self.data_share[msg.sender]
