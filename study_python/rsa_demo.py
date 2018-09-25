#coding=utf-8
import base64

import rsa
import base64


class RsaDemo(object):
    private_key_pem = '''
    -----BEGIN RSA PRIVATE KEY-----
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
        '''


    private_key_pem = '''
-----BEGIN RSA PRIVATE KEY-----
MIIBOwIBAAJBAKH0aYP9ZFuctlPnXhEyHjgc8ltKKx9M0c+h4sKMXwjhjbQAZdtW
Iw8RRghpUJnKj+6bN2XzZDazyULxgPhtax0CAwEAAQJADwR36EpNzQTqDzusCFIq
ZS+h9X8aIovgBK3RNhMIGO2ThpsnhiDTcqIvgQ56knbl6B2W4iOl54tJ6CNtf6l6
zQIhANTaNLFGsJfOvZHcI0WL1r89+1A4JVxR+lpslJJwAvgDAiEAwsjqqZ2wY2F0
F8p1J98BEbtjU2mEZIVCMn6vQuhWdl8CIDRL4IJl4eGKlB0QP0JJF1wpeGO/R76l
DaPF5cMM7k3NAiEAss28m/ck9BWBfFVdNjx/vsdFZkx2O9AX9EJWoBSnSgECIQCa
+sVQMUVJFGsdE/31C7wCIbE3IpB7ziABZ7mN+V3Dhg==
-----END RSA PRIVATE KEY-----
    '''

    transdata = {"transtype": 0, "result": 0, "transtime": "2018-09-22 18:41:36", "count": 1, "paytype": 5,
                 "money": 100, "waresid": 231437, "appid": "1809130758960.app.ln", "exorderno": "20180922184116872",
                 "feetype": 0, "transid": "2180922184136725326312529", "cpprivate": "123456"}
    sign = "cJESzwvvdL4VPHN9oTE5FwOOc5KntYTt + jP5DTxhNELvO4AosdIdY86hcZH3G0gjnm3JN0p0CIlcztjyb16iPU3Dk4 + 2ZCQMq6w09U38 + zihyOh3ZbjF39ckZbm7aN9jFHcD2MRduHG6w9v1d2t4 + sTrJRXIQBgTqHEfBbsUFks ="
    key = '''BEGIN PRIVATE KEY-----MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAKXs7sQccmss5EoBcC8XJ3FhNgmnsiZmUOio4RGiUdbmcw+zAY0NLWPOHZD3lfBiQCm87NhUA/1Dab7qKd99MlkfEJi/4DxtEYvP9DYVs4d0D4D9pcAj4erH2Gj+emwYlm/4duh20/jwrZH8OMUpdM9MEo6LTzSGMYwxCUojCb5pAgMBAAECgYAfVqK6E41gxLfRangfzMW8Wln0dOHm8sgxSURJKlk+t4Pf4TVXyLdb9GANM1X0cvofZ/lr2mJugT8FugByn5jUgQThtKHLkDPX50i4R5WaU7Oo6eVRa8rzJnGo8lEHxO0eGp9AWkLvUWd750ccrQHH1vyhZcp2G9ge1mQjcqQl6QJBAPn280njw3vgFGqbVan2Uc74crV3FAtLP24W0e7n9h6cjCIu91rxihVu15i9zTk3So5DvH3IjC9xr3pvv6+N4bMCQQCp7ofFlJAQhJBbMz6kHsnS9nLOEmTDFQQWmy0BOCl+8S6rW9vmQCFqouzgwAFohDuiyaRg6wyjuPtP1QZxgblzAkEA8OUMa95Dy4MVSfQvZ1/KUZNgQP/kYkn/dCIr6XjE2ZV2+46VtaBnueYbgskQGZ7ujBI9el8msqZ2PaGqcw5iPwJAFU79436/mfKlj2obnsTllfilaMXRsMy/2H3Y5OBAA9UGfyJjrrm39wE7JuuswYhjWgRjAmw3B4i4qsgRqMYVlQJACCCm7mlNR6f+9LRMT4zF/UQD9bKBd/u3rEKuKtYmY8ivhj1WgQT9tkq0m43drubXtjYwC3DSID0alyRlAyTI/w=='''

    def sign(self):
        transdata = {"transtype": 0, "result": 0, "transtime": "2018-09-22 18:41:36", "count": 1, "paytype": 5,
                     "money": 100, "waresid": 231437, "appid": "1809130758960.app.ln", "exorderno": "20180922184116872",
                     "feetype": 0, "transid": "2180922184136725326312529", "cpprivate": "123456"}
        sign = "cJESzwvvdL4VPHN9oTE5FwOOc5KntYTt + jP5DTxhNELvO4AosdIdY86hcZH3G0gjnm3JN0p0CIlcztjyb16iPU3Dk4 + 2ZCQMq6w09U38 + zihyOh3ZbjF39ckZbm7aN9jFHcD2MRduHG6w9v1d2t4 + sTrJRXIQBgTqHEfBbsUFks ="
        pri_key = rsa.PrivateKey.load_pkcs1(self.private_key_pem)
        signature = rsa.sign(str(transdata), priv_key=pri_key, hash_method='SHA-1')
        key_sign = base64.b64encode(signature)
        print(key_sign)
        if sign == key_sign:
            print("true")
        else:
            print("false")


if __name__ == "__main__":
    # RsaDemo().rsa_demo()

    RsaDemo().sign()
