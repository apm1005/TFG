from .VPNParser import VPNParser
from .windowsParser import WindowsParser


class Parser:
    """
    Facade pattern.

    Class that analyzes content from the logs of each app and provides data for the database.
    """

    def __init__(self):
        self.__vpn_parser = VPNParser()
        self.__windows_parser = WindowsParser()
        # next parsers

    def parse(self):
        """
        Parses the data and stores it in the database.
        """
        self.__vpn_parser.parse()
        self.__windows_parser.parse()
        # next parsers
