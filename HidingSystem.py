

from subprocess import call

def hide(folder_path):
    call(["attrib", "+H", folder_path])


def unhide(folder_path):
    call(["attrib", "-H", folder_path])






