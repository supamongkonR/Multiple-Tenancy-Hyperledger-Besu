from cgi import print_environ
import jwt
private_key = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAxPxVUUDdg5Ij3xfDFNkDMimcem8OnLsAJL5oFaRcsGWR0pis
r9T4z3Z820s03blGUTURWBTV6kEGnqcg/7/ebWOSy4obopQixPYelT4RyDmKPg48
lOSqQl6WG4LIYKrT6MDFpvjtK9mpnG4T8HL3C00VFHyWTNPYEDUyMix9UJd9nOB9
vrBFKDLGVskh7JQqpZqBo/LMWYS4MfgnFwGT6imfuyvr2yUEyz65aj06S+mql4H/
TZYjuvvcpEksdiyF+Zv2oFBucm6jYqj0r9MJrHBFqbOI/y7lpVq4Yd36x82aEaON
4Rqwxz52NL/+PyadERtgOFhMBSgt2ptO+eheRwIDAQABAoIBAE+XZSGfg+FVewj5
IOmbhZ8PERqnJNBO/o/aH1QfRRRA9dqRtbSV6LJqvagdiw7LfY3yUz+zq3srKvGP
tdWgQM8SHI4BD4lxMVtD1reWjLjKBwFr3y6J9gE7FounHC9y1oyE11fP3ISLPezm
zUeqLAd07b+JV3FTZ0mlNNLxBvE4jeKt2Be0m/btbz96aQPxVwB4IP7EVsv7Z0NN
FEhLA/4Zm0MdwWdyl8toZ7y5cVj7Z2p8QRjpAH92b99470ZEN2W4PeeSktb4+dML
ZKgd7AYE7AId5ujTgKX6jnpRQrh5N8ngq68mFE+J1S4fBmTt/mHjy3fDZFFvk7bZ
9NLhEYECgYEA/GUWq7qnAR/Lg0mxlePy93QqfRMKf8pjZqXehhuaf24akh7oqZyM
8tz98WPkLnz3UMFD76ffzEonaakREUKj40DGKFINsjrZiVKr33+AQ/AFMOJnp4f1
dA3hmv+tkDxzfod4MwKlg2SR31dBfUii8LpUfSEE75DBh8P9shrQXuUCgYEAx8yi
bUN87tiD+SSCqPmuFmeVvwv7vDypt6aCRphpl0ITcs37wGpUorure2hAKSy3Qh0N
OVyat5JUOTo+nXOxfpW5xfRip2W35dFyQgNJJF0f4r93afxOO/rTaAxXu/fS6YwZ
NAubqOw0goZd+gqUqAJMjvyTl6bKNvbGBtwZCbsCgYA0hrk0HhE5e6t39DNAFYNw
Gj3pb7gEplMPfr+Tu1To5jojZMlY2xq+RF2ZCgfn4Nv7c203CAHcWyZep+/EXtEK
r2VN6N2u1O6G1KyuQ7Om7+G0rbmStQnRED5+am1tkhcbIwhR3WAiuyBckaUwdJhs
buq8a83CKacNIS3ADjKFPQKBgQC1TmYKvtZNK58+47nJuqEWZbNGpYovu+DK7ceE
ZmRTRTu+z1rntdXNwn2PRAANHS3DSfepGPaxJJFXSRpu6QClfRsSnn0zqKNjYlfL
vY2O+Q6pRdQIElOwLCHRZnnq8a2sD10DlJERjh7sXyBCeX2CpGtyyZLpaApSLEdx
DCOQZwKBgQCMEp57JSRRR/VybHNhsfdbS+6NClJNbreos/APEnV+LQu2cAZiIywn
uHELbPtv5ULKLQT6+Bizc15rrkQQHJNSr1VaIhj35NyH4poXyKj5OmUQtRR0gSOc
r4KFJZk7BhlT2cqeFi9eqY7kaNVX3P/eKgcmRsRkb6hxUlzaHy689Q==
-----END RSA PRIVATE KEY-----
"""
public_key = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxPxVUUDdg5Ij3xfDFNkD
Mimcem8OnLsAJL5oFaRcsGWR0pisr9T4z3Z820s03blGUTURWBTV6kEGnqcg/7/e
bWOSy4obopQixPYelT4RyDmKPg48lOSqQl6WG4LIYKrT6MDFpvjtK9mpnG4T8HL3
C00VFHyWTNPYEDUyMix9UJd9nOB9vrBFKDLGVskh7JQqpZqBo/LMWYS4MfgnFwGT
6imfuyvr2yUEyz65aj06S+mql4H/TZYjuvvcpEksdiyF+Zv2oFBucm6jYqj0r9MJ
rHBFqbOI/y7lpVq4Yd36x82aEaON4Rqwxz52NL/+PyadERtgOFhMBSgt2ptO+ehe
RwIDAQAB
-----END PUBLIC KEY-----"""
privacy_public_key = "keiNgxxEVbW1fzp0b8aNj1n5JxN+n1PwSoITiPruYhU="
endcoded = jwt.encode({"permissions":["*:*"],"privacyPublicKey":privacy_public_key,"exp": 1600899999002},private_key, algorithm="RS256")
print("token is: ",endcoded)
