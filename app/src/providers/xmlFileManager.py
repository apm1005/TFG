from .fileManager import FileManager
from tfgproject.settings import VPN_DIRECTORY_SRC, VPN_DIRECTORY_DST
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
        return os.listdir(VPN_DIRECTORY_SRC)

    def move_files(self, files):
        """
        Deletes from the "to do" directory the files parsed

        Parameters
        ----------
        files : list
            all the files that have been parsed
        """
        for file in files:
            try:
                os.rename(os.path.join(VPN_DIRECTORY_SRC, file), os.path.join(VPN_DIRECTORY_DST, file))
            except FileExistsError:
                print(f'File "{file}" already exists in "{VPN_DIRECTORY_DST}" and won\'t be moved!')

    @staticmethod
    def get_roots(files):
        """
        Gets the roots of the files

        Parameters
        ----------
        files : list
            all the files that are going to be parsed
        """
        return [et.parse(os.path.join(VPN_DIRECTORY_SRC, file)).getroot() for file in files]
