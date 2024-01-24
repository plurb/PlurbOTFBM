from colorama import Fore

from util.server import OTFBMServerContext
from fastapi.exceptions import HTTPException


def handle_server_error(error_code, message):
    if not OTFBMServerContext.active_context:
        return

    raise HTTPException(status_code=error_code, detail=message)


class OTFBMException(Exception):
    def __init__(self, message, error_data: dict):
        super().__init__(message)

        self.error_data = error_data

        handle_server_error(error_code=self.error_data["code"], message=self.error_data["message"])
        self.handle_cli_error()

    def handle_cli_error(self):
        if OTFBMServerContext.active_context:
            return

        # print statements go brr!
        print(Fore.RED + "Oops! Something went wrong!")
        print(Fore.RED + self.error_data["code"])
        print(Fore.RED + self.error_data["message"])
