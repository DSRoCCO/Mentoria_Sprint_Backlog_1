"""Person Class"""

class Person:
    def __init__(self):
        pass

    def set_name(self, name):
        self.name = name

    def set_job(self, job):
        self.job = job

"""driver code"""
if __name__=="__main__":
    charly = Person()
    charly.set_name('Charly')
    charly.set_job('Dev')

    print(charly.name == 'Charly')
    print(charly.job == 'Dev')
