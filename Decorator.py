import datetime

class ILogger:
    """
    класс-интерфейс логирования
    """

    def message(self, severity, message):
        pass

    def restart(self):
        pass


class Logger(ILogger):
    """
    базовый класс логирования, функционал которого мы можем расширять с помощью классов-декораторов
    """

    def message(self, severity, message):
        print(severity, message)

    def restart(self):
        print('------ logger restarted ------')


class TimeLogger(ILogger):
    """
    класс логирования с временными метками, расширяет функционал базового класса, но при этом не наследует его
    """

    def __init__(self, logger):
        self.logger = logger

    def message(self, severity, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = ' - '.join([timestamp, message])
        self.logger.message(severity, message)

    def restart(self):
        self.logger.restart()


class FilterLogger(ILogger):
    """
    класс логирования с фильтрацией информационных сообщений, расширяет функционал базового класса, но при этом не наследует его
    """

    def __init__(self, logger):
        self.logger = logger

    def message(self, severity, message):
        if severity != 'Info':
            self.logger.message(severity, message)

    def restart(self):
        self.logger.restart()

if __name__ == "__main__":
    base_logger = Logger()
    time_logger = TimeLogger(base_logger)
    logger = FilterLogger(time_logger)

    base_logger.message('Info', 'System reboot is scheduled for 21:00 today')
    base_logger.message('Warning', 'System reboot scheduling will be deprecated after the next update')
    base_logger.restart()

    time_logger.message('Info', 'System reboot is scheduled for 21:00 today')
    time_logger.message('Warning', 'System reboot scheduling will be deprecated after the next update')
    time_logger.restart()

    logger.message('Info', 'System reboot is scheduled for 21:00 today')
    logger.message('Warning', 'System reboot scheduling will be deprecated after the next update')
    logger.message('Info', 'System will be rebooted in 30 minutes')
    logger.message('Error', 'System reboot is cancelled due to opened unsaved files')
    logger.restart()