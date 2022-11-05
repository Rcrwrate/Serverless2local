import requests


class VC():
    '''http://fast.95man.com/auth/main.html'''
    def __init__(self):
        self.session = requests.Session()
        self.session.trust_env = False
        self.session.keep_alive = False
        # r = self.session.get("http://api.95man.com:8888/api/Http/UserTaken?user=RRRRR&pwd=12345678&isref=0")
        # self.token = r.text.split("|")[1]
        self.token = "4EOSA8YEjP5Qk40LmDBrlJ6Nb6as"
    
    def get_code(self,base64):
        url = "http://api.95man.com:8888/api/Http/Recog?Taken=" + self.token + "&len=4"
        header = {
            "Content-Type":"application/x-www-form-urlencoded"
        }
        Data = "ImgBase64=" + base64
        Data = {
            "ImgBase64":base64
        }
        r = self.session.post(url,data=Data,headers=header)
        try:
            return r.text.split("|")[1]
        except Exception:
            pass
        return r.text
    

if __name__ == "__main__":
    vc = VC()
    print(vc.token)
    base = "iVBORw0KGgoAAAANSUhEUgAAAMgAAAA8CAIAAACsOWLGAAAOuElEQVR4Xu3dT2xcVxXH8SO8AYkdCxA7EAIWLIpU6taxk9impBUSZIuEEIKCQoPtNInjpPnTFgm3qlLyr0lTsUJihwoUFtGlLW2IiZs4jh3biRMndtK48Z/8rVokEBISZ3zGN2fO7777/syMkzSVvorGd+57bxJ9et+bN7ZL7o03PmkJGhsZJhrA8Y9rhEPVRLSx8ssncM59G9vSXx69fFoy04h6cNs6RdSOg9VH9HpxWET/w8FPimdsXZo9zw3fnJIQWf0iWoeDNYyInsTRyhnP4WBdI/oMDhaLaDMO3tnYluHl08g4YYfTqonoLA7Wo6wrFtHvcdA0cmWcw/GMEX0eBz+WRWz5/InSC9Ph/KSIfoiDS1BWWCaiv+KgVCWv+6QstnwemT9XIrVc2pagwrBexEFdMV5EP8DBpIi+jIN3Q0RfwEEsbsu8DfIhMh9Su4PaCsLKWDFe909xW6lFkPmQ2tJoqy8sSXjdK8Iu9w/hYF2rxpaURZgOqdVc21LAku4hXveiLV9eZD6kVo22HLD6+o9W39jchIRPEV3EwSXL/GXvaVu+wsh8SC2jNguLqBknZYmoCwcj1Xv1Wvvclnhmfl9J9pOa2snjA+gvS36fh9YvT02/hnrY8sWFjQye5HAcQ2dBardhEX0Rn653teWFejKGu5KKrVuoJ0uybU1srXlwZ7DGhl7+c+3yfT4zofORPRJuazJHZFtXh69JQs2uWLqOqeFgm+ZHOZxfuOp5oZUC4W5dTlvIJW8u7a3i7OhgMD0HHSSVhCyVF74w36W+y1xWWM2vvWN4Tc0c5XCrwhXmhUQKZ/ZM9GeX2RYqKZZLsxVMI9vYtAdDHCZEFlnA8AWYbsMamh3h9HO4Vul4gtiqB68kYXOjpzj/JcqoMjyilGqLQbyzdVUwpJOaK2TLpwVsaN4n9bSUQnBBdqnC8KAmu2KxLaKvyWPEZGBJNbflory8LaHQtPp76KNweDhfxBbK0CG1LOZcflszU+ULc6NE5535ZByplWOLCzEyzcuVlvPf4mvwWVhuceniEFMQlrTEvHqef4bTJppW/xih5A0P5GNYSbaQRcZ6Wx9EbdLU5KQrags9RQo6wzSy7uX7bpwd4fT59+zwuM8FYUkMa/3VM+gpCZZUD14OLr8EAdrCcFd6D6bOnc8dnT4XTLYK2kIuGL4AnIOxLenK9LR/7MN9SmwLWZgaG3Y3NvRUuGnZz3WvONCz4kCcWmPD8/yn3Lk4MTvByXE1svc/uJIIyy2cCtlWEi+c76srL6MhiRdujvXN9nMdL23j9FZEm8xML2x4ZorT5v62/Ts+xHEopErCmZENcd1CalnYpba2ZTfzEmcSUtPzPS8vTEqBJQV54XxTnXg9tfNZLm4Lt0pNeAk1fFZn1i1NQSOTkhY/3PbNHW0RWC5kKxJSy8JO1iS2xeF6Js1fOD9z9rRJNvfCWFsmWEFeOD9YbXk1rf6F0EnihZtkj3dy+eIlTnj5cKa2ZTTEcTi1+JnVjnvj2VV65cNtc9mKFBRmTnnGlo9nsi0dj2hkk6dLVcAykoIFVy/M/k1qxEtLCvLSNyMKJ7z8l0Fk3hZiisPS4XxZt5JWO25w/iKufDUJDeHShVs5cCbUcsOSUnnh4V1OXkQfmRGjyvDiZJq+13X52LiE+0/N8JI0svdHR9gW4tDhbnU4/9CCLeGF87nJifn3L93ipQvNYbh5UqgKbeFWSbGtgrCkCC88mCS2svPSISmduTcR5FVAWJCXj239Y/O33Y5WCZXgJjqcr23hfB/b4nDchNR0gzeucC5ZleaFO49XFayORVvI6+z5IZ05ajFbiEnnp3le5ja9q0KY8AoK40XrcHd7mdGiMI0MNyH6qgup6m39un88OPcuh9v6xko/AbuZFzB8Klcdra9Ia1e8nBQr7D//LoebJ1UtLAltEX1J79k4E2qGF1H5XJYUYgrCkiK8XIIwohNmmt0qgZe2dduTQobvAFBVxbYLc7LY4thWYV5+TepaflDC5WrNwkmQbR27PsnhyufTe64NLEnzwr+DyQubuTXABRc2HUqKqPIJr6AtKSgsNeTV2/oNtFVhJbSYJeV3m9GWW7j2KsALDSEvov/oTSLrlkZmYfVMj2BoKJLwwqNKRH/BQbe4egUXNgkxBWERXcOdp/JyhYQZXnFYFW4UMuMMj+IWeOGgzt+GyMULVRleHG7lFmxFeEkVsEzeClLjLp7ok3BDDr9Xwke0NzT4XQcnR6cWtg0v7pBQlYYFu93uH7OtqWuTEVtSXmGaV+qbxGD6jIknTQltET2gv9S3uLLwQkwYTxu/NM/h5qm2MsEK5qd5YT6iq/IgwisS8nJqxfLCdLiTpIQXh0+ZcgnzvLLc3ML8fiL3ZtGWCW0l8TKAOhrtt82IKp/wQmERWzWAFUl4nbs+xhl8ONlkeOEqpYucQ4MJL39vIl52YYe3Pcb1bXsc6WTM7NA4y2XLJfBCQ2LL8MKdB3nppYvom368vrB0ZvXCdQ7Z6ZteiElnjkV0IQs1Pi1m5+XShHkcYov/RDdZwj372NbQvwZwMdPhxz6GF6pCW7hbneEVPC0uHSy3aCvLyVEjmxvv57p7t0qoCmEF08g+mJjjRBvz0ndWs4TC0IfYivDqbX0AByU8ok7eKkZOmsHv4hJbTzWHbyhoW3jEYHoBQ1tLCkvKaMu0cec2jg15Ybosp1eif+sv505Nc2VnF85wEzcvcLhhJLF1eNOjHPqQ94lsi+hnrvQCHvMb4mQTHks6NXaWw9sQBlnQFtNhWBKqknjaYH/K/TyT5uUHawaL6HOLD/6Iu8Ly8pKVyfPyNa3u8isWnlLx9GoSXuXHC/cjhFfqaVQicmVDC7a8sN7WB8vj3eVfmYe3vhBTLlujt4aTLrmE15mpUc4vZlpPEi+/B7aVkRfRh/JAeE3M3xBeNYNVrOy8NCbkhfMxpCZdGxkytlzl96waZIaa0eB5yZnOlf7p/+QnG16IycCSHxPyDV85z8njuC1J1i229eTKXb4IL71tdls6scXlhtX82okawpIy8qpcqLoNL5yfPeHFLVI7zvGDC1fPJV1+Ca+3t7b7UNjtS7HKb2jWHw2hJ2ML07zYFodzfGJLL0sGWWPDJuGF2xazJeWG5cP5VZbKS8PyeV44v0D+zOiXLuEl4WqnEWhkkixsYuv6wBnzXlJsRa7uk2BJhhcvYDhHYj1dTXu1LUR2ceY6J+8ciV7XmxezdRfBkiK8UJXmhfOLhVdd8liWLrN6He5Zaept/ZY8YBbm7Hlz8OzVkQvmboW8c0ziZV4b5nnxOVGuvZy63nX6Y+YEW2vUGVB4ceZtZoGl666DJQV5oScT7qdwhpd+SvNCCj62hSvc/NCx2dPHro0MsjDJn0ODvPCFBRNecr3leTm4ZZVky+xNbkwIL19eW3cpLLdoy/BCTEtmK8gLPaWy4Out286GB45sbuvb3M4d2dLG9T3dfmTH414bbh6JbY1+VHqRYgsBBcP9SOaWPdsaGh3i8LZZsCWCVfj/JGBsoaRcsOK/ezy4eWTp4t7a/iiHpOIs8Id89N0KXuqObGkvCdvSxsub72LCHRMT22JhLKZz2cucByS/aiaiKvgLYPETIV639EqWhGyJYFWZ5oWYpO5fb5Nw8yzFXeJFvSQsIrxwV1LSZ9UVwrY9pu9N8FWadibUdH4mnxM72/d2rthfqpJXkqp4hpc5JwadFYe1xLbcIi8kFRT23rF+DneC6W3xWV9w6fIgelvbhRcKw11J8e/fElult5PTs3hzVTJvDry29Y/8ZkPz7lLL9kjIC/cWj+hNzStyySW8qoKVFO4qNfnQI0tsa91LgR99Dia8gshw8toQLKLSjxv4NC/JgAjywt2W6HS3x23JzPLdiulZEYa7Mq1r2cN1Lnu1s/nVrraFxyv2l4U1lYTh0pUrf081aMt/bBWD5Yrawv3UPLaVnZfkz5UcPivhgSSiXf6xsYUgDiXwwuK2zGvQwsxTOi/glw+/0rnsYMfK3UJtXduBUssPrGvZj1zyxrZk9WJbwf+r0r0Kyy0sOQV4SUnI8ChJaV5owlfYlux5eKQfu72Ahb57xwhgW1zFyIr9wqsMbjHUE88tXnvhuuVSYRERukkN91OnREMqr6d2/ipSzwvPSAUu/LPYSg1t4YF0Xtjk5Cg3ceYkJyMOYK1ZXLrWlN4YPuEH8bo+Ly//etjW5cmbhlcKLFdo0cKd1C9tK84rNbY1OzYsjVw5nyWnli4Uk73e1odu/3Ai/B3j8YWXrF4cC+ts2hVu2UEWhj7wuj6pxobt+kv7MiZvcv7LdFgS6omEm9c7kZFqq2n1Vhz06R0Gr/pPTvzTNH5jSro1dZ37+zOrUnvz6dZgb29t4/AQEv6VTfLOkYWtf3ifZFiwra6W3V3L9lpwTaWPorPz8uFrKL2MyZvlDxzxuUhoKBhumCWiVTiYK/GRygvDXemCyHREP3GZl663tq8KxuvfhblLXHBdRGrBZmenN658hZPzWkfzLqyz6SCnR7qad5dq2cs1Nuwpf9m8G7flGht+JA/Mof2/Bp8T2VY+WHckonM4mFoqL9wkS6nIzEV9b2vp0+hIZnPzy7ckpBZv7uq8vvVF9JDZITcwMMPhuP6o0bxpIPqUf4wbamSjk8fvAVjVhJ821rAIMnOvK1dBW3nzwjiUJ506c4uTx2ZzzSuYMaeTCbWBRbQCRv6B0+5UdeUlITK8lZq9Km0RbdBfJt24l2TpQnbc+MX3OHl87tp7pvHR8D9peXnDJ5Ysot/hYPaIfo6Dkepty6eRFeblbRGl/2xtliK8kk6LUtLSFdQm8VN3EtbHO/lWd7b14ekZDk+XqVWzaCUlvILC4rxyxYsZTR2f4fC5T6ptnlcuYfWw5dJ4udJ/FX/Ap3JVXrHqx4vopzh4v0X0fXkgp0W2dW52XMLJpjrZcsm8arJ0lWERfdrVk1c1Eb2Ag5GI1uKgevYrOFgs+cV8eTNXXcJraHrMJV81ZrFF9F8crJzwWRyU0Jarmtf/AU5ksy33sQOCAAAAAElFTkSuQmCC"
    print(vc.get_code(base))