from Lib.log import Log
import traceback
l = Log("Plugin", log_level=40)


class Plugin():
    def __init__(self) -> None:
        self.Plugin = {}

    def register(self, path):
        try:
            __import__(path)
        except Exception as e:
            l.error(f"[Register][ERROR]\t\t{path} Load Failed\t\t{e.args}\n{traceback.format_exc()}")
        else:
            l.info(f"[Register][INFO]\t\t{path} Load Success")

    def registerEvent(self, route):
        def run(func):
            self.Plugin[route] = func
        return run


Manager = Plugin()
