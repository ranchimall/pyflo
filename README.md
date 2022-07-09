## Python bitcoin library modified for FLO

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
>>> import pyflo

# ADDRESS GENERATION 
>>> a = pyflo.Address(address_type="P2PKH")
>>> a.address
'FTP7LL7QjhgKfqYX1pis18bCqEpZaGSRzZ'
>>> a.private_key.wif
'R8Gw2Mr3n2fY1ydB2X5gEehxHkdhboeUD6yw4wRtVKHaqAd9gdkK'
>>> a.private_key.hex
'16b6aca5ff6a3bf3a1332dd4edf87880b2883cb4fe16effd073e2e866aa141aa'
>>> a.public_key.hex
'033c30b269e2d5df229f3f0ce294b19c4f0a3a8d12280415ce41e7bd3784a619c4'

# CONVERT MESSAGE INTO SHA-256 HASH 
>>> pyflo.sha256(b'vivek'.hex())
b'\xa3\xdas\x97e\x01\x81,\xd7\xb8!\xa2\x0b\xfb\t\xaf\nj\x89\x1eA\x9c\xdf\xb7a\xfb\x19\xa9,\x91BB'
>>> pyflo.sha256(b'vivek'.hex()).hex()
'a3da73976501812cd7b821a20bfb09af0a6a891e419cdfb761fb19a92c914242'
>>> msg = b'vivek'.hex()
>>> msg_hash_hex = pyflo.sha256(msg).hex()
>>> msg_hash_bytes = pyflo.sha256(msg)
>>> msg
'766976656b'
>>> msg_hash_hex
'a3da73976501812cd7b821a20bfb09af0a6a891e419cdfb761fb19a92c914242'
>>> msg_hash_bytes
b'\xa3\xdas\x97e\x01\x81,\xd7\xb8!\xa2\x0b\xfb\t\xaf\nj\x89\x1eA\x9c\xdf\xb7a\xfb\x19\xa9,\x91BB'

# SIGN AND VERIFY THE MESSAGE 
>>> sig_msg_hex = pyflo.sign_message(msg_hash_hex, a.private_key.wif)
>>> pyflo.verify_signature(sig_msg_hex, a.public_key.hex, msg_hash_hex)
True

# SIGN AND VERIFY MESSAGE IN STANDARD OPERATION
>> pyflo.sign_message_standard_ops('vivek', a.private_key.wif)
'3045022039747449a6fbac008d04d763a3a62f2261d1c5a35ee6a21a8354d8757d27593802210085a4d4b9886de6d06c3563c97160c8d70f492ce56f9e00dbcd7276004369402e'
>> sig_msg_hex = pyflo.sign_message_standard_ops('vivek', a.private_key.wif)

# To verify the above signature, run the following in the console of any Standard Ops app 
>> sign_msg_hex = '3045022039747449a6fbac008d04d763a3a62f2261d1c5a35ee6a21a8354d8757d27593802210085a4d4b9886de6d06c3563c97160c8d70f492ce56f9e00dbcd7276004369402e'
>> a.public_key.hex = '033c30b269e2d5df229f3f0ce294b19c4f0a3a8d12280415ce41e7bd3784a619c4'
>> floCrypto.verifySign('vivek', sig_msg_hex, a.public_key.hex) 
true

```
