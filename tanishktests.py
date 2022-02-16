import pyflo

# pk = pybtc.create_private_key()
# print("pk = " + pk)
# pk = "RCJ9Q6kH5ywdRhchVKrxPUFiJE7cGMKFEB8n9zd4VgdNVYzHNedz"


# a = pybtc.sign_message_tanishk("hey", pk, hex=True)
# print(a)
# b = pybtc.verify_signature(a, public, "6865790D0A")
# print(b)
# pybtc.test_function()
msg = "hey"
pk = "RCJ9Q6kH5ywdRhchVKrxPUFiJE7cGMKFEB8n9zd4VgdNVYzHNedz"
public = pyflo.private_to_public_key(pk)
print("public = " + public)
sig = '30460221008b30bdc5039264abb40b686b1bdb9db0900e0b6c50dea793c0c1b1bde654119a022100b51e25bc73c274a5f3cd8bcdb11143921a2b1595c3b62f1cffcbe3bc5e876b65'
sig = pyflo.sign_message(msg, pk)
print(sig)

