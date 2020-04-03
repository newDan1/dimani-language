
import re
import time

class Interpreter:
    def __init__(self, text:str):
        self.text = text
        self.tokens_string_list = self.text.split()
        self.commands = {
            ':':'PRINT',
            '+':'ADD',
            '-':'SUBTRACT',
            'wait':'WAIT',
        }
        self.tokens = {
            r'[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]':'INTEGER',
        }

    def run(self):
        self.command = self.tokens_string_list[0]
        self.args = self.tokens_string_list[1:]
        self.command_compiled = self._get_command_type(self.command)
        self._run_command(self.command_compiled, *self.args)

    def PRINT(self, *values):
        print(*values)

    def ADD(self, *values):
        try:
            print(int(values[0]) + int(values[1]))
        except Exception:
            self._error()

    def SUBTRACT(self, *values):
        try:
            print(int(values[0]) - int(values[1]))
        except Exception:
            self._error()

    def WAIT(self, *values):
        time.sleep(int(values[0])/1000)

    def _get_command_type(self, token:str):
        token_type = self.commands.get(token, '_error')
        return token_type

    def _error(self, *args):
        raise Exception('Error parsing code.')

    def _run_command(self, command:str, *args):
        try:
            getattr(self, command)(*args)
        except Exception as e:
            print("\tError")

    def __str__(self):
        return self.text

def run_from_file(filename:str):
    try:
        if not filename.endswith(".dimi"):
            raise Exception("File '{}' is not a dimani (.dimi) file.".format(filename))
        f = open(filename, 'r')
        for line in f.readlines():
            inter = Interpreter(line.strip())
            inter.run()
    except Exception as e:
        print("No such file '{}' or is not a dimani (.dimi) file.".format(filename))

def main():
    while True:
        text = input(">>> ")
        if text == "exit":
            break
        interp = Interpreter(text)
        interp.run()

if __name__ == "__main__":
    # main()
    run_from_file('test2.dimi')