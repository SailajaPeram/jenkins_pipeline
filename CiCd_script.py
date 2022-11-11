import os
class HelloWorld:
    def validate(self):
        self.input = "Hello How are you"
        print("1")
        # self.input=os.environ.get("Enter the input")
        print("2")
        k = self.input.split()
        if (k[0].lower() == "hello"):
            print("success")
        else:
            print("fail")

obj=HelloWorld()
obj.validate()


