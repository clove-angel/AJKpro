#!/usr/bin/env python
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import base64
import json
import zlib

#加密解密
class ED(object):
    def decryption(self,token): #解密
        tn = base64.b64decode(token.encode()) #base64解码

        tnz = zlib.decompress(tn) #zlib解码，生成字节
        # print(tnz)
        bn = eval(str(tnz,'utf-8'))  #字节转换为字典,并返回字典
        # print(bn)
        return bn



    def encryption(self,bn): #加密
        te = json.dumps(bn).encode('utf-8') #将字典转为字节类型
        tez = zlib.compress(te) #将字节用zlib加密
        ten = base64.b64encode(tez) #在经过base64方式加密 返回为字节
        ten = bytes.decode(ten) #字节转字符串
        return ten

if __name__ == '__main__':
    # to = "eJxdjklPg0AYhv/LXEvKsA0zTTzYllI2W2gRxXigMAUqi2ylYvzvjoleTL7kXb7n8H6C1kjAQoCQQMiBK23BAghzOEeAA33HPkhSoYxkQVIklQPxvw5jDpzaxzVYvGAEOYLI60/hsfwiEBFyAsTwlfvzMvOizO6HMhgEsr5/7xY8Hzfzkub9EFXzuC555rss59kIwNDyyFCmb78a/Wr/lx22mrFdnlbMUXMsLkdhdz9pbkZnh7F5lK5OgTqYDv6qfvOceGleIzewpj483nQ5Nd34sB1crPWOZaJKUek0ohCvZNlfog2fby1xdMr4gs8VIWf1o9Uqo9i/B4GyoTr1g+BYbmpS+Otduqpje9J4PDSDUQxEd098nT1sojAXbLGqnyxy85c9pY1mHxQCw9ZrAkGnqyYZYjTtCe9Z0SyJAvPWFGd1drmsQ9FX7bpo7JFuvVH/IJV4v88kZ9yZylJXBylpt9Nz4umpfErsGS4OvnEHvr4BML+N4w=="
    to2 = 'eJyllmkS7DYIhK9kgxDycbze/wj5Gnscv0p+pCozNYtWaOgG99ajW/c+8Vn70v/f+PgP+ydb+v6OWcmJ8ci5L3l488ndgznm/fT0znjXnG++8O0+s76yc2V+dc/B/5n5hVH6/Zo4t/llVw7rNTn74bvtbsZZa6ydfuVsM1YY22Jnbv84f9rcM3X7ofOvf2HyTP5tzM8//6K1BO5lq2U/wWN2se4hZOEHqGYCkn7FsMkOzsxYX3yPM9LPwOO42JvsxsfHl+Bf4r3j8+xTjNg4c/pmEzYvy9te63i62GYrtucceWUaNonvxsdy57ux2nv2jVG3id9Jse8DrM7ukyxuyQavVbK3JnhzMmM0c8PCDRf/N2Kjs1uEtRsPf7KZheIbsk3srNsS8mHJ0XX/rPXWe8sjGiyY06K3ua122dTYmRjHc/zplzkxLf86Wee+xv5sk0UIx4YHva93/rBs3DuBNLh3za01zhu2nf17I17Y6Mw4aYJv2bHRU2zMlnXfAZYAH95ynfIfbYgwdsY9zvCbP+SPi3hP97jfY3HElC/eG/zXC56LT77ye5BPMWfBFvcp1R1u+GpHi8qVYQF+ET+UQm6FZrK9IZ+2trAdrFusiGsqeV0Pf0eDA/wHAy/D742YDAMBdApGGtfKPSafXeOO07gOX/lpxMriQCunYu1JbohhnkR0jt3nkM6a7bnA6x6bAFjknnjoCviQz21Itya0cBwlmJTACnywQYxWHz5sZpSkrZH/Q3yWM8XnEcudL6oDmlU9MEW2oSdTfKKVvkwKQQ9X1QopXXZTfEQvUcpZ/YYofLJY8ZLypSdTClCoUUxYHaDBPjNXoemltfINxUmJxJeTZBc77DedWljt3Dkxb6Xf4Xn7Lzyu/BM7fa/ObvwAq4sB7I3SORFwVadRDEJ/eH4j1p5dimD1YkRWCvFdr8S19iIW0ulBvFR0vohV144H8Wpe+L+IydaD2E0+/4n4wO6NWBgGN9yIp0J8+vggnqs+C/FUeFP2XryyH4U3ZV/Z+eBNYSy8vexTjz94448MT58MK/a8P3jnuunGSzVx3fjvGS77j70fXtXYG2/Unnzw9sKr3X/j/fWCrXLTxYAH769zKL+ziafS7I1nIwKF7cajbHn/+PvzZ6056e7rz/XaE5LltSdO3PGVPcoJ2vnZi8rHwxfFw+0bnz/sLX/gPx4G3/akOlfHQqFn1cFLCk7U3dqr0FkdUx2K08Ovpvu5RfdT4/2pyMsdEzogxS7wjzayUKHgymM/i31b26HOzJteQLfQKa+KoieC5qp4dBVuaLH0sxRNJmgIVv6TPyroSoHDPl1J/JukNt1K/k/q7NUOOkXxR7KsiLm8osd5qH+N9uWfgrZTUSMW+vIUV7+5GuJv9Dv+7aJi77EqPzF4JFHE6CBqrfAR/rSdwnu98ZjruWf8Ix79jUcnO8dvXZ9at3c9n4po8jfWFG+v8he+vv5WhwtV6LfD5UQsqoM/He8zrjwpNk+H/+Wz6m775VP1XspiJZ9a1cu6tKvKd7SsfFT8S4+3Xl+8qlmFJ188/qugFf96JqsnorLzxZNZeKbCY77GFkcefwHN74iU'

    en = ED()
    tos = en.decryption(to2)

    s = en.encryption(tos)
    print(s)


