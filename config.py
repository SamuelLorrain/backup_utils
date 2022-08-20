
"""
Put your src/dst folders/files to backup here,
you can also put rsync option as a third argument:
Example:
RSYNC_LIST = [
    {'src': './a', 'dst': './b'},
    {'src': './c/', 'dst': './d', 'rsync_options': ('-a', '-p')},
]

Be careful, the src option follows rsync/BSD convention,
meaning that ./a is different than ./a/, see rsync(1) man for
more informations.
"""
RSYNC_LIST = [
]
