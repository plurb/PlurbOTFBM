import pyray as rl

from fastapi import FastAPI


class ZephyrServerContext(FastAPI):
    """
    Singleton context manager. Ensures that there is only one active server, and ensures that CLI and FastAPI usage of
    the renderer throw the correct error message if there is an active server or not.
    """

    active_context: 'ZephyrServerContext' = None

    def __new__(cls):
        if cls.active_context is None:
            # create the server context
            cls.active_context = super(ZephyrServerContext, cls).__new__(cls)

        return cls.active_context

    def __init__(self):
        super().__init__()

        # Initialize raylib with hidden window
        rl.set_config_flags(rl.ConfigFlags.FLAG_WINDOW_HIDDEN)
        rl.init_window(0, 0, "test window")

