## Python bitcoin library modified for FLO

Current version is 2.0


### Feature Support

* Basic functions
* Supports addresses types PUBKEY, P2PKH, P2SH, P2SH-PWPKH, P2WPKH, P2WSH.
* Supports BIP32(Hierarchical Deterministic Wallets), BIP39(Mnemonic code generation)
* Supports BIP141(Segregated Witness)
* Transaction constructor


### Installation

To install pyflo, 

    $ git clone https://github.com/ranchimall/pyflo
    $ cd pyflo
    $ sudo python3 setup.py install
    
### Dependencies

* Python 3.3.3+
* secp256k1


#### Message signing and verification 

Every message sent to the Blockchain is in hash format, and not in plain string. So we convert the message we are signing into a SHA256 hash before. 

```
>>> import pybtc

# ADDRESS GENERATION 
>>> a = pybtc.Address(address_type="P2PKH")
>>> a.address
'FTP7LL7QjhgKfqYX1pis18bCqEpZaGSRzZ'
>>> a.private_key.wif
'R8Gw2Mr3n2fY1ydB2X5gEehxHkdhboeUD6yw4wRtVKHaqAd9gdkK'
>>> a.private_key.hex
'16b6aca5ff6a3bf3a1332dd4edf87880b2883cb4fe16effd073e2e866aa141aa'
>>> a.public_key.hex
'033c30b269e2d5df229f3f0ce294b19c4f0a3a8d12280415ce41e7bd3784a619c4'

# CONVERT MESSAGE INTO SHA-256 HASH 
>>> pybtc.sha256(b'vivek'.hex())
b'\xa3\xdas\x97e\x01\x81,\xd7\xb8!\xa2\x0b\xfb\t\xaf\nj\x89\x1eA\x9c\xdf\xb7a\xfb\x19\xa9,\x91BB'
>>> pybtc.sha256(b'vivek'.hex()).hex()
'a3da73976501812cd7b821a20bfb09af0a6a891e419cdfb761fb19a92c914242'
>>> msg = b'vivek'.hex()
>>> msg_hash_hex = sha256(msg).hex()
>>> msg_hash_bytes = sha256(msg)
>>> msg
'766976656b'
>>> msg_hash_hex
'a3da73976501812cd7b821a20bfb09af0a6a891e419cdfb761fb19a92c914242'
>>> msg_hash_bytes
b'\xa3\xdas\x97e\x01\x81,\xd7\xb8!\xa2\x0b\xfb\t\xaf\nj\x89\x1eA\x9c\xdf\xb7a\xfb\x19\xa9,\x91BB'

# SIGN AND VERIFY THE MESSAGE 
>>> sig_msg_hex = pybtc.sign_message(msg_hash_hex, a.private_key.wif)
>>> pybtc.verify_signature(sig_msg_hex, a.public_key.hex, msg_hash_hex)
True
```



