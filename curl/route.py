from flask import Flask

app = Flask(__name__)

student_list = ['rajesh', 'vijay', 'mani']

@app.route('/add/<string:name>',methods =['POST'])
def add(name):
    student_list.append(name)
    return f"new student {student_list}"

@app.route('/getall',methods =['GET'])
def allDetail():
    list = " "
    for name in student_list:
        list += (name +" ")
    return list

@app.route('/delete/<string:name>',methods=['DELETE'])
def delete(name):
    if name in student_list:
       student_list.remove(name)
       return f"{student_list}"
    else:
        return f"deleted"


if __name__ == '__main__':
     app.run(port=3000)
