from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

class OverwriteStorage(FileSystemStorage):

    def _open(self, name, mode='rb'):
        return File(open(self.path(name), mode))
    
    def get_available_name(self, name, max_length=None):
        return name

    def _save(self, name, content):
        # here, you should implement how the file is to be saved
        # like on other machines or something, and return the name of the file.
        # In our case, we just return the name, and disable any kind of save
        if self.exists(name):
            self.delete(name)
            
        return super(OverwriteStorage, self)._save(name, content)
    

    
