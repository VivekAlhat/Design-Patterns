class Logger(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("creating new instance")
            cls._instance = super(Logger, cls).__new__(cls)
        else:
            print("instance already exists")
        return cls._instance


first_logger = Logger()
second_logger = Logger()

if first_logger == second_logger:
    print("both are same loggers")
