import os
import tempfile
import unittest
from shutil import rmtree
from git_uploader import cmd_call, compare_local_and_remote, upload

remote_server = "dl-ubuntu"


class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        ...

    def setUp(self) -> None:
        self.cur_dir = tempfile.mkdtemp()
        print("local dir", self.cur_dir)
        os.chdir(self.cur_dir)
        cmd_call("git init")
        cmd_call("echo 1 > README.md && git add . && git commit -m 'init'")

    def tearDown(self) -> None:
        rmtree(self.cur_dir)

    def test_new_remote(self):
        basename = (os.path.basename(self.cur_dir))
        remote_dir = "/tmp/" + basename
        remote_dir2 = "/tmp/" + basename + "2"
        remote = "dl-ubuntu:" + remote_dir
        remote2 = "dl-ubuntu:" + remote_dir2

        # Init
        print("\n=== Test === ", "Init")
        upload(remote)
        self.assertTrue(compare_local_and_remote(remote_server, remote_dir))

        # No Args
        print("\n=== Test === ", "No Args")
        cmd_call("echo 2 > README2.md && git add . && git commit -m 'update2'")
        upload()
        self.assertTrue(compare_local_and_remote(remote_server, remote_dir))

        print("=== Test === ", "Change Remote")
        cmd_call("echo 3 > README2.md && git add . && git commit -m 'update3'")
        upload(remote2)
        self.assertTrue(compare_local_and_remote(remote_server, remote_dir2))


if __name__ == '__main__':
    unittest.main()
