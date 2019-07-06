# @auth:haoliang
# class F:
#     def f1 (self):
#         print('F.f1')
#
#     def f2 (self):
#         print('F.f2')
#
# class S(F):
#     def s1(self):
#         print('S.s1')
#
#     def s2(self):
#         print('S.s2')
#
#         super(S, self).f1()
#         F.f2(self)
#
#
# obj = S()
# obj.s1()
# obj.s2()


# class RequestHandler:
#     def serve_forever(self):
#         print('RequestHandler.serve_forever')
#         self.process_request()
#
#     def process_request(self):
#         print('RequestHandler.process_request')
#
# class Minx:
#     def process_request(self):
#         print('Minx.process_request')
#
#
# class Son(Minx,RequestHandler):
#     pass
#
# obj = Son()
# obj.serve_forever()



class ber:

    def city(self):
        cun = '中国'

    def __init__(self,names):

        self.name = names


print(ber.cun)



























