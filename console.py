Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        args = parse(arg)
        if len(args) > 0 and args[0] not in HBNBCommand.classes:
            print(" class doesn't exist ")
        else:
            obj_list = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.class.name:
                    obj_list.append(obj.str())
                elif len(args) == 0:
                    obj_list.append(obj.str())
            print(obj_list)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        args = parse(arg)
        count = 0
        for obj in storage.all().values():
            if args[0] == obj.class.name:
                count += 1
        print(count)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        args = parse(arg)
        obj_dict = storage.all()

        if len(args) == 0:
            print(" class name missing ")
            return False
        if args[0] not in HBNBCommand.classes:
            print(" class doesn't exist ")
            return False
        if len(args) == 1:
            print(" instance id missing ")
            return False
        if "{}.{}".format(args[0], args[1]) not in obj_dict.keys():
            print(" no instance found ")
            return False
        if len(args) == 2:
            print(" attribute name missing ")
            return False
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print(" value missing ")
                return False

        if len(args) == 4:
            obj = obj_dict["{}.{}".format(args[0], args[1])]
            if args[2] in obj.class.dict.keys():
                val_type = type(obj.class.dict[args[2]])
                obj.dict[args[2]] = val_type(args[3])
            else:
                obj.dict[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = obj_dict["{}.{}".format(args[0], args[1])]
            for k, v in eval(args[2]).items():
                if (k in obj.class.dict.keys() and
                        type(obj.class.dict[k]) in {str, int, float}):
                    val_type = type(obj.class.dict[k])
                    obj.dict[k] = val_type(v)
                else:
                    obj.dict[k] = v
        storage.save()


if name == "main":
    HBNBCommand().cmdloop()
