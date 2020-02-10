from abc import ABC, abstractmethod


class FileManager(ABC):
    """
    File manager for logs
    """

    @abstractmethod
    def check_directory(self):
        """
        Checks if there are VPN XML files to parse and returns a list with the names

        Returns
        -------
        list
            a list with all the names of the XML files
        """
        pass

    @abstractmethod
    def delete_files(self, files):
        """
        Deletes from the "to do" directory the files parsed

        Parameters
        ----------
        files : list
            all the files that have been parsed
        """
        pass
