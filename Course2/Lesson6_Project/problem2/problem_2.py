"""
TASK2:
For this problem, the goal is to write code for finding all files under a directory
 (and all directories beneath it) that end with ".c"

Here is an example of a test directory listing:
./testdir
./testdir/subdir1
./testdir/subdir1/a.c
./testdir/subdir1/a.h
./testdir/subdir2
./testdir/subdir2/.gitkeep
./testdir/subdir3
./testdir/subdir3/subsubdir1
./testdir/subdir3/subsubdir1/b.c
./testdir/subdir3/subsubdir1/b.h
./testdir/subdir4
./testdir/subdir4/.gitkeep
./testdir/subdir5
./testdir/subdir5/a.c
./testdir/subdir5/a.h
./testdir/t1.c
./testdir/t1.h

you may want to use the following resources:

os.path.isdir(path)

os.path.isfile(path)

os.listdir(directory)

os.path.join(...)

Note: os.walk() is a handy Python method which can achieve this task very easily.
However, for this problem you are not allowed to use os.walk().
"""
import glob
import pathlib


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix is the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    return None


def find_files_glob(suffix, path) -> list:
    paths_list = []
    for path in glob.glob(path + '/**/' + suffix, recursive=True):
        print("path={}".format(path))
        paths_list.append(path)
    print("paths_list={}".format(paths_list))
    return paths_list


def find_files_pathlib(suffix, path) -> list:
    paths_list = []
    for path in pathlib.Path("testdir").rglob("*.c"):
        print("path={}".format(path))
        paths_list.append(path)
    print("paths_list={}".format(paths_list))
    return paths_list


def test_find_files_glob():
    print("->test_find_files_glob:start--------------------------------------------")
    result_list = find_files_glob("*.c", "testdir")
    assert len(result_list) == 4
    print("->test_find_files_glob: is finished...")


def test_find_files_pathlib():
    print("->test_find_files_pathlib:start--------------------------------------------")
    result_list = find_files_glob("*.c", "testdir")
    assert len(result_list) == 4
    print("->test_find_files_pathlib: is finished...")


def test():
    test_find_files_glob()
    test_find_files_pathlib()


test()
