#!/usr/bin/python3
"""
Console for AirBnB clone project
"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def emptyline(self):
        """Do nothing when empty line is entered"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True

    def do_create(self, line):
        """Create a new instance of BaseModel"""
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] not in models.classes:
                print("** class doesn't exist **")
            else:
                new_instance = models.classes[args[0]]()
                new_instance.save()
                print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] not in models.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in models.storage.all():
                    print("** no instance found **")
                else:
                    print(models.storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] not in models.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in models.storage.all():
                    print("** no instance found **")
                else:
                    del models.storage.all()[key]
                    models.storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances"""
        if not line:
            print([str(obj) for obj in models.storage.all().values()])
        else:
            args = line.split()
            if args[0] not in models.classes:
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in models.storage.all().values()
                       if type(obj).__name__ == args[0]])

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] not in models.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in models.storage.all():
                    print("** no instance found **")
                elif len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    obj = models.storage.all()[key]
                    attr_name = args[2]
                    attr_val = args[3]
                    setattr(obj, attr_name, attr_val)
                    obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
