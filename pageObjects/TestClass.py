class TestClass:

    def __init__(self, arg_name, arg_title):
        self.name = arg_name
        self.title = arg_title

    def display_info(self):
        return_value = f'Hello {self.title} {self.name}!'
        return return_value


object_testclass = TestClass(arg_name='Malvika', arg_title='Ms')
output = object_testclass.display_info()
print(output)
