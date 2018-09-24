#coding=utf-8
import base64

import rsa
from rsa.prime import gcd

from pyCrypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64


class RsaDemo(object):
    public_key_pem = '''
    -----BEGIN PRIVATE KEY-----
        MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAKXs7sQccmss5EoBcC8XJ3FhNgmn
    siZmUOio4RGiUdbmcw+zAY0NLWPOHZD3lfBiQCm87NhUA/1Dab7qKd99MlkfEJi/4DxtEYvP9DYV
    s4d0D4D9pcAj4erH2Gj+emwYlm/4duh20/jwrZH8OMUpdM9MEo6LTzSGMYwxCUojCb5pAgMBAAEC
    gYAfVqK6E41gxLfRangfzMW8Wln0dOHm8sgxSURJKlk+t4Pf4TVXyLdb9GANM1X0cvofZ/lr2mJu
    gT8FugByn5jUgQThtKHLkDPX50i4R5WaU7Oo6eVRa8rzJnGo8lEHxO0eGp9AWkLvUWd750ccrQHH
    1vyhZcp2G9ge1mQjcqQl6QJBAPn280njw3vgFGqbVan2Uc74crV3FAtLP24W0e7n9h6cjCIu91rx
    ihVu15i9zTk3So5DvH3IjC9xr3pvv6+N4bMCQQCp7ofFlJAQhJBbMz6kHsnS9nLOEmTDFQQWmy0B
    OCl+8S6rW9vmQCFqouzgwAFohDuiyaRg6wyjuPtP1QZxgblzAkEA8OUMa95Dy4MVSfQvZ1/KUZNg
    QP/kYkn/dCIr6XjE2ZV2+46VtaBnueYbgskQGZ7ujBI9el8msqZ2PaGqcw5iPwJAFU79436/mfKl
    j2obnsTllfilaMXRsMy/2H3Y5OBAA9UGfyJjrrm39wE7JuuswYhjWgRjAmw3B4i4qsgRqMYVlQJA
    CCCm7mlNR6f+9LRMT4zF/UQD9bKBd/u3rEKuKtYmY8ivhj1WgQT9tkq0m43drubXtjYwC3DSID0a
    lyRlAyTI/w==
    -----END PRIVATE KEY-----
    '''

    transdata = {"transtype": 0, "result": 0, "transtime": "2018-09-22 18:41:36", "count": 1, "paytype": 5,
                 "money": 100, "waresid": 231437, "appid": "1809130758960.app.ln", "exorderno": "20180922184116872",
                 "feetype": 0, "transid": "2180922184136725326312529", "cpprivate": "123456"}
    sign = "cJESzwvvdL4VPHN9oTE5FwOOc5KntYTt + jP5DTxhNELvO4AosdIdY86hcZH3G0gjnm3JN0p0CIlcztjyb16iPU3Dk4 + 2ZCQMq6w09U38 + zihyOh3ZbjF39ckZbm7aN9jFHcD2MRduHG6w9v1d2t4 + sTrJRXIQBgTqHEfBbsUFks ="
    key = '''BEGIN PRIVATE KEY-----MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAKXs7sQccmss5EoBcC8XJ3FhNgmnsiZmUOio4RGiUdbmcw+zAY0NLWPOHZD3lfBiQCm87NhUA/1Dab7qKd99MlkfEJi/4DxtEYvP9DYVs4d0D4D9pcAj4erH2Gj+emwYlm/4duh20/jwrZH8OMUpdM9MEo6LTzSGMYwxCUojCb5pAgMBAAECgYAfVqK6E41gxLfRangfzMW8Wln0dOHm8sgxSURJKlk+t4Pf4TVXyLdb9GANM1X0cvofZ/lr2mJugT8FugByn5jUgQThtKHLkDPX50i4R5WaU7Oo6eVRa8rzJnGo8lEHxO0eGp9AWkLvUWd750ccrQHH1vyhZcp2G9ge1mQjcqQl6QJBAPn280njw3vgFGqbVan2Uc74crV3FAtLP24W0e7n9h6cjCIu91rxihVu15i9zTk3So5DvH3IjC9xr3pvv6+N4bMCQQCp7ofFlJAQhJBbMz6kHsnS9nLOEmTDFQQWmy0BOCl+8S6rW9vmQCFqouzgwAFohDuiyaRg6wyjuPtP1QZxgblzAkEA8OUMa95Dy4MVSfQvZ1/KUZNgQP/kYkn/dCIr6XjE2ZV2+46VtaBnueYbgskQGZ7ujBI9el8msqZ2PaGqcw5iPwJAFU79436/mfKlj2obnsTllfilaMXRsMy/2H3Y5OBAA9UGfyJjrrm39wE7JuuswYhjWgRjAmw3B4i4qsgRqMYVlQJACCCm7mlNR6f+9LRMT4zF/UQD9bKBd/u3rEKuKtYmY8ivhj1WgQT9tkq0m43drubXtjYwC3DSID0alyRlAyTI/w=='''

    def rsa_demo(self):

        key = rsa.newkeys(3000)#生成随机秘钥
        privateKey = key[1]#私钥
        publicKey = key[0]#公钥
        message ='sanxi Now is better than never.'
        print('Before encrypted:',message)
        message = message.encode()
        cryptedMessage = rsa.encrypt(message, publicKey)
        print('After encrypted:\n',cryptedMessage)
        message = rsa.decrypt(cryptedMessage, privateKey)
        message = message.decode()
        print('After decrypted:',message)

    def gcd(self, a, b):
        print(a % b)
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    def sign(self):
        transdata = {"transtype": 0, "result": 0, "transtime": "2018-09-22 18:41:36", "count": 1, "paytype": 5,
                     "money": 100, "waresid": 231437, "appid": "1809130758960.app.ln", "exorderno": "20180922184116872",
                     "feetype": 0, "transid": "2180922184136725326312529", "cpprivate": "123456"}
        sign = "cJESzwvvdL4VPHN9oTE5FwOOc5KntYTt + jP5DTxhNELvO4AosdIdY86hcZH3G0gjnm3JN0p0CIlcztjyb16iPU3Dk4 + 2ZCQMq6w09U38 + zihyOh3ZbjF39ckZbm7aN9jFHcD2MRduHG6w9v1d2t4 + sTrJRXIQBgTqHEfBbsUFks ="
        #key = '''BEGIN PRIVATE KEY-----MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAKXs7sQccmss5EoBcC8XJ3FhNgmnsiZmUOio4RGiUdbmcw+zAY0NLWPOHZD3lfBiQCm87NhUA/1Dab7qKd99MlkfEJi/4DxtEYvP9DYVs4d0D4D9pcAj4erH2Gj+emwYlm/4duh20/jwrZH8OMUpdM9MEo6LTzSGMYwxCUojCb5pAgMBAAECgYAfVqK6E41gxLfRangfzMW8Wln0dOHm8sgxSURJKlk+t4Pf4TVXyLdb9GANM1X0cvofZ/lr2mJugT8FugByn5jUgQThtKHLkDPX50i4R5WaU7Oo6eVRa8rzJnGo8lEHxO0eGp9AWkLvUWd750ccrQHH1vyhZcp2G9ge1mQjcqQl6QJBAPn280njw3vgFGqbVan2Uc74crV3FAtLP24W0e7n9h6cjCIu91rxihVu15i9zTk3So5DvH3IjC9xr3pvv6+N4bMCQQCp7ofFlJAQhJBbMz6kHsnS9nLOEmTDFQQWmy0BOCl+8S6rW9vmQCFqouzgwAFohDuiyaRg6wyjuPtP1QZxgblzAkEA8OUMa95Dy4MVSfQvZ1/KUZNgQP/kYkn/dCIr6XjE2ZV2+46VtaBnueYbgskQGZ7ujBI9el8msqZ2PaGqcw5iPwJAFU79436/mfKlj2obnsTllfilaMXRsMy/2H3Y5OBAA9UGfyJjrrm39wE7JuuswYhjWgRjAmw3B4i4qsgRqMYVlQJACCCm7mlNR6f+9LRMT4zF/UQD9bKBd/u3rEKuKtYmY8ivhj1WgQT9tkq0m43drubXtjYwC3DSID0alyRlAyTI/w=='''
        pri_key = rsa.PrivateKey.load_pkcs1(self.public_key_pem)
        signature = rsa.sign(str(transdata), priv_key=pri_key, hash='SHA-1')
        key_sign = base64.b64encode(signature)
        print(key_sign)
        if sign == key_sign:
            print("true")
        else:
            print("false")

    # def sign(self):
    #     '''
    #     @param signdata: 需要签名的字符串
    #     '''
    #     signdata = self.transdata
    #     key = self.key
    #
    #     signer = pk.new(rsa.importKey(key))
    #     signn = signer.sign(signdata)
    #     # signn=base64.b64encode(signn,["-","_"])
    #     signn = base64.urlsafe_b64encode(signn)
    #     return signn

    def RSA_sign(encrData):
        privateKey = '''MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAOG/8J9TP8cN7upNoZ+LoBs9xImv
    4hHAwO/gq7TLGjZ5IoUIxWPJbGtUI+muXsFf8tBfjE3p86ava1R1Ji0c0Sh98bPT4lFMqGFWV5OJ
    d2VbvLGG4DclFzkZxMuB4M7sSvXlKdfawHuFFG/HiEEzjuiROfqWlP3qZ6Ix0QLRhE9HAgMBAAEC
    gYBdPujnBn3rfIfY4+QEgKnLVsIdlTat2o5XBtglv1a+dV6a0LqnswVDd+e1mD6vZTBofW74p8/q
    Y77TjegM7kA90Nw9N4z2uuhn7kXFNI+RiA2MUXcqf4Vwb/64wRpqH70abZzCuyhxQYXqNqEmJuL4
    jAxMoxztxj4BvXt5zk9ekQJBAPLwghERrLNgu+ty/Fmdk15NWE/Eoazig15THPEgrZ5Ruaq90U9O
    4sTWbYgDLYJI75uDTgFoPE+VHkT40WspYZMCQQDt4tsPwVHtXEX4sYclEAbWzXEYDlNXCA3zvWf6
    9cb9N+oY4FfMuThFdfpC5H2D+5bhqCRLZUzuvthS7i18ljv9AkEApJkFVvFFtIc+60iN513XAhaf
    VfRgohUacqcXPdwpJdIzXJadIQHOrRSnQ3b7t4EZLqFpEZUA/96Fkq+Om+9+lwJBAK0fjwt9RrF2
    mNmv4UnAyyliZC78pfxNuVGsg1LpsYKxQaYPBvbPyTsL7DDodswpuhnJs3hHZeDOdUKNYf8smsUC
    QDhQqQHjf6Kf9ZI/zO6Ldvn0y5cMomzfFaH8ltRcjuNB8num1Vt0Oyk+k90q+OYak5twRvKGGsQD
    8v+gOIQ8ZfA='''
        private_keyBytes = base64.b64decode(privateKey)
        priKey = RSA.importKey(private_keyBytes)
        # priKey = RSA.importKey(privateKey)
        signer = PKCS1_v1_5.new(priKey)
        hash_obj = MD5.new(data.encode('utf-8'))
        signature = base64.b64encode(signer.sign(hash_obj))
        return signature






if __name__ == "__main__":
    # RsaDemo().rsa_demo()

    RsaDemo().sign()
