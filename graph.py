import matplotlib.pyplot as b
query = ['chennai','madurai','tanjavur','andhra','neelagiri','kerala']
values=[42,11,14,31,19,16]
b.pie(values,labels=query,autopct='%.f')
b.show()