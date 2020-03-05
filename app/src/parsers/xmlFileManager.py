from .fileManager import FileManager
from tfgproject.settings import VPN_DIRECTORY
import xml.etree.ElementTree as et
import os


class XMLFileManager(FileManager):
    def check_directory(self):
        """
        Checks if there are VPN XML files to parse and returns a list with the names

        Returns
        -------
        list
            a list with all the names of the XML files
        """
        return os.listdir(VPN_DIRECTORY)

    def delete_files(self, files):
        """
        Deletes from the "to do" directory the files parsed

        Parameters
        ----------
        files : list
            all the files that have been parsed
        """
        for file in files:
            os.remove(os.path.join(VPN_DIRECTORY, file))

    @staticmethod
    def get_roots(files):
        """
        Gets the roots of the files

        Parameters
        ----------
        files : list
            all the files that are going to be parsed
        """
        return [et.parse(os.path.join(VPN_DIRECTORY, file)).getroot() for file in files]
