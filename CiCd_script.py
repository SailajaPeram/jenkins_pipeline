import os
class HelloWorld:
    def validate(self):
        print("1")
        self.input=os.environ["input"]
        print("2")
        k = self.input.split()
        if (k[0].lower() == "hello"):
            print("success")
        else:
            print("fail")

obj=HelloWorld()
obj.validate()


