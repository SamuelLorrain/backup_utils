from pathlib import Path
from typing import List
import subprocess
import logging
from config import RSYNC_LIST

RSYNC_COMMAND = "rsync"
GLOBAL_RSYNC_OPTION = ('-a', '-p', '-r', '-v')

logging.basicConfig(
    filename='log.log',
    encoding='utf-8',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s: %(message)s'
)


class Rsync:
    src: str
    dst: str
    rsync_options: List

    def __init__(self, **kwargs):
        self.src = kwargs['src']
        self.path_src = Path(self.src)
        if not self.path_src.exists():
            logging.warning(f"source {self.src} is not a valid folder/file")
        self.dst = kwargs['dst']
        self.path_dst = Path(self.dst)
        # if not self.path_dst.():
        #     print(
        #       f"Error, destination {self.dst} is not a valid folder/file"
        #     )
        self.rsync_options = kwargs.get('rsync_options', GLOBAL_RSYNC_OPTION)
        # TODO check for existing rsync_options ?

    def __call__(self):
        process = subprocess.Popen([
            RSYNC_COMMAND,
            *self.rsync_options,
            str(self.path_src),
            str(self.path_dst)
        ], stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return_code = process.wait()
        if stdout:
            for i in stdout.split(b'\n'):
                print(i.decode('utf8'))
        # logging.debug(stdout) if stdout else None
        logging.error(stderr) if stderr else None

        if return_code != 0:
            logging.error("ERROR, rsync for "
                  f"'{RSYNC_COMMAND} {self.rsync_options} {self.src} {self.dst}' "
                  "failed!")
        if return_code == 0:
            logging.debug("rsync for "
                  f"'{RSYNC_COMMAND} {self.rsync_options} {self.src} {self.dst}' "
                  "success!")


def create_rsync_list(dict_list):
    return [Rsync(**entry) for entry in dict_list]


if __name__ == '__main__':
    rsync_list = create_rsync_list(RSYNC_LIST)
    for entry in rsync_list:
        entry()
