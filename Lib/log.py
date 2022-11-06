import logging
import os


class Log():
    def __init__(self, name, log_level=logging.INFO, log_path=".log") -> None:
        if os.path.exists(log_path) != True:
            os.mkdir(log_path)
        self.LOG = logging.getLogger(name)
        self.LOG.setLevel(log_level)
        path = os.path.join(f"{log_path}", f"{name}.log")
        self.F = logging.FileHandler(path, "a", encoding="utf-8")
        self.F.setFormatter(logging.Formatter('%(asctime)s:%(message)s'))
        self.LOG.removeHandler(self.F)
        self.LOG.addHandler(self.F)

    def Log(self):
        return self.LOG

    def info(self, msg, **kwargs):
        self.LOG.info(msg, **kwargs)

    def debug(self, msg, **kwargs):
        self.LOG.debug(msg, **kwargs)

    def error(self, msg, **kwargs):
        self.LOG.error(msg, **kwargs)

    def __del__(self):
        self.LOG.removeHandler(self.F)
