class IHandler:
    """
    класс-интерфейс, по сути родитель всех используемых впоследствии обработчиков (handlers)
    """

    def handle(self, message):
        pass


class InfoHandler(IHandler):
    """
    обработчик информационных логов. если лог другого вида, то он передаётся следующему обработчику цепочки
    """

    def __init__(self, next):
        self.next = next

    def handle(self, message):
        if message.startswith("info"):
            print("INFO", message)
        else:
            self.next.handle(message)


class ErrorHandler(IHandler):
    """
    обработчик логов ошибок. если лог другого вида, то он передаётся следующему обработчику цепочки
    """

    def __init__(self, next):
        self.next = next

    def handle(self, message):
        if message.startswith("error"):
            print("ERROR", message)
        else:
            self.next.handle(message)


class FailureHandler(IHandler):
    """
    обработчик логов неисправностей. если лог другого вида, то он передаётся следующему обработчику цепочки
    """

    def __init__(self, next):
        self.next = next

    def handle(self, message):
        if message.startswith("failure"):
            print("FAILURE", message)
        else:
            self.next.handle(message)


class DefaultHandler(IHandler):
    """
    обработчик всех остальных типов логирования. данный обработчик заканчивает цепочку и не направляет к следующему.
    """

    def __init__(self):
        pass

    def handle(self, message):
        print("Unsupported message type", message)


class Logger:
    """
    класс логирования, собирает цепочку обязаннсотей.
    """

    def __init__(self, *args, default_handler = DefaultHandler()):
        self.handlers = {}
        self.handler = None
        self.handlers[0] = default_handler

        for i, handler in enumerate(*args[::-1], 1):
            if i == 1:
                self.handlers[i] = handler(default_handler)
            else:
                self.handlers[i] = handler(self.handlers[i-1])

        self.handler = self.handlers[list(self.handlers.keys())[-1]]

    def log(self, message):
        self.handler.handle(message)

    def add_handler(self, handler):
        self.handlers[list(self.handlers.keys()[-1])+1] = handler(list(self.handlers.values())[-1])
        return True

    def get_handlers(self):
        return self.handlers

if __name__ == '__main__':
    handlers = [InfoHandler, ErrorHandler, FailureHandler]
    logger = Logger(handlers)
    print(logger.get_handlers().items())
    logger.log("failure - prod destroyed")
    logger.log("info - new user logged in")
    logger.log("error - 404 not found")
    logger.log("warning - no backup files found")