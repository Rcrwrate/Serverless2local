import logging
import os


class Log():
    def __init__(self, name, log_level=logging.INFO, log_path=".log") -> None:
        if os.path.exists(log_path) != True:
            os.mkdir(log_path)
        self.LOG = logging.getLogger(name)
        self.LOG.setLevel(log_level)
        path = os.path.join(f"{log_path}",f"{name}.log")
        F = logging.FileHandler(path, "a", encoding="utf-8")
        F.setFormatter(logging.Formatter('%(asctime)s:%(message)s'))
        self.LOG.addHandler(F)

    def Log(self):
        return self.LOG