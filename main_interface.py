from Game.interface.app import RPGApp
from rich.traceback import install

install()


if __name__ == "__main__":
    app = RPGApp()
    app.mainloop()