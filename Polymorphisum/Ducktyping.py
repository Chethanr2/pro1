
class PyCharm:

    def execute(self):
        print("Execution")
        print("Compilation")

class Myediter:

    def execute(self):
        print("Spell check")
        print("Alignment")
        print("Execution")
        print("Compilation")

class Polymor:

    def Code(self,ide):
        ide.execute()

ide = Myediter()

ply = Polymor()
ply.Code(ide)
