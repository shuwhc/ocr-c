from types import ModuleType


def search_submodules(module, identifier):
    assert isinstance(module, ModuleType)
    ret = None
    for attr in dir(module):
        if attr == identifier:
            ret = '.'.join((module.__name__, attr))
            break
        else:
            submodule = getattr(module, attr)
            if isinstance(submodule, ModuleType):
                ret = search_submodules(submodule, identifier)
    return ret

if __name__ == '__main__':
    import cv2
    print (cv2.__version__)
    print search_submodules(cv2, 'RNG')