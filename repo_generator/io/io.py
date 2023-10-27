import os
import functools
import shutil

TEMP_DIR_NAME = "temp"

def temporary_directory(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        This decorator Creates a temporary directory in the current directory, execute a function and delets the temporary directory after the function is executed.
        """
        
        path_to_temp = os.path.join(os.getcwd(), TEMP_DIR_NAME)
        
        create_dir_forced(path_to_temp)
        os.chdir(path_to_temp)
        
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            os.chdir("..")
            shutil.rmtree(path_to_temp, ignore_errors=True)
            raise e
        
        os.chdir("..")
        shutil.rmtree(path_to_temp, ignore_errors=True)
        return result  

        
    
    return wrapper

def create_dir_forced(path_to_dir):
    if os.path.exists(path_to_dir):
        shutil.rmtree(path_to_dir, ignore_errors=True)
    os.mkdir(path_to_dir)

    


        
