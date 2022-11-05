from Controler.Plugin import Manager

@Manager.registerEvent("/err")
def err(msg):
    raise Exception("")

    