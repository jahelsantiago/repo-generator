from repo_generator.io import temporary_directory
import os

@temporary_directory
def test_tempo_directory_parent():
    current_directory_name = os.path.basename(os.getcwd())
    assert current_directory_name == "temp"


def test_returns_values():

    @temporary_directory
    def get_parent_dir_name():
        current_directory_name = os.path.basename(os.getcwd())
        return current_directory_name
    
    parent_dir_name = get_parent_dir_name()
    assert parent_dir_name == "temp"
        
    
def test_files_are_deleted():

    @temporary_directory
    def create_file():
        with open("test.txt", "w") as f:
            f.write("test")
        os.mkdir("test_dir")
        os.chdir("test_dir")
        with open("test.txt", "w") as f:
            f.write("test1")
    
    create_file()
    assert not os.path.exists("temp/test.txt")
    assert not os.path.exists("temp/test_dir/test.txt")



    
    