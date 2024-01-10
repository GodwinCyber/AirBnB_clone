#!/usr/bin/python3
"""Define the HBNBCommand Class"""
import cmd


class HBNBCommand(cmd.Cmd):
    """A command that interprete class thta inherit from cmd.Cmd"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def emtyline(self):
        """Do nothing when the empty line is entered"""
        pass

    def help_EOF(self):
        """show the help mesaage for EOF command"""
        print("EOF command to exit the program")

    def help_quit(self):
        """Show the help message for quit command"""
        print("Quit command to exit the program")

    def default(self, line):
        """called an input line when the command prefix is not recorgnied"""
        if line == '':
            return self.emptyline()
        else:
            return cmd.Cmd.default(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
