class computer:

    def __init__(self,CPU, RAM):
        self.cpu = CPU
        self.ram = RAM

    def config(self):
        print ("config is ",self.cpu, self.ram)

    def company(self):
        print("computer class is belongs to Intel")

comp1 = computer('I8', 8)
comp2 = computer('I5', 12)


comp1.config()
comp2.config()