import sys


class Logger(object):
    def __init__(self, fileN='Default.log'):
        self.terminal = sys.stdout
        self.log = open(fileN, 'a')

    def write(self, message):
        '''print实际相当于sys.stdout.write'''
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

sys.stdout = Logger('./test.txt')  # 调用print时相当于Logger().write()

print("bbbb")

# 每次调用print都相当于调用Logger().write()，然后做了print本该做的事，打印到控制台，然后将内容保存到指定文件。