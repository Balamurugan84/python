# # overriding
# class sample:
#     test1 = "hi"
#     test2 = "hello"
#
#     def txt(self):
#         print("hi...")
#
#     def tst(self):
#         print("hello")
#
#
# class sam(sample):
#   def tst(self):
#         print("wellcome")
#
#
# test = sam()
# test.tst()
# # calling some other function
# test.txt()

# overloading

class cal:
    def calci(self,a):
        print(a)
    def calci(self,a,b):
        print(a+b)
    def calci(self,a,b,c):
         print(a+b+c)

c=cal()
c.calci(4,b=0,c=0)


# import datetime as t
#
# date =t.date.today()
# print(date)
#
# time =t.datetime.today()
# print(time)




