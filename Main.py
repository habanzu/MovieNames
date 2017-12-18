import os, re



def get_size(start_path = '.'):
    if os.path.isfile(start_path):
        return os.path.getsize(start_path)
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def get_size_readable(start_path='.'):
    pre = {1e12: 'T', 1e9: 'G', 1e6: 'M', 1e3: 'K'}
    res = get_size(start_path)
    for k,v in pre.items():
        if res > k:
            return '{}{}'.format(round(res/k, 1), v)

def move():
    treshold = 10 * 2**30

    os.chdir(path_bad)
    names = os.listdir()
    for name in names:
        if get_size(name) > treshold:
            os.rename(path_bad + name, path + name)
    os.chdir(path)
    names =os.listdir()
    for name in names:
        if get_size(name) < treshold:
            os.rename(path + name, path_bad + name)


path = r"/run/media/habanzu/DECKARDCAIN/Filme"
path_bad = r"/run/media/habanzu/DECKARDCAIN/Filme/Bad Quality/"
pattern = r"(?:([^-]+)-)+?([^-]+)"

os.chdir(path)
names = os.listdir()
names_with_size = {}

for name in names:
    result = name.split('-')
    result = ' '.join(result)
    os.rename(name, result)
    print('{} {}'.format(get_size_readable(result), result))


move()

