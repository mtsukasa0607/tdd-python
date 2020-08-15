import sys
def py2_or_py3():
    major = sys.version_info.major
    if major == 2:
        return 'Python 2'
    elif major == 3:
        return 'Python 3'
    else:
        return 'Neither'

print(py2_or_py3())
