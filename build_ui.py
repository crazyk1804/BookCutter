from glob import glob
import os
import pathlib


if __name__ == '__main__':
    # path_ui = pathlib.Path('gui', 'ui')
    path_ui = pathlib.Path('book_cutter_app', 'gui', 'ui')
    for entry in path_ui.glob('*.ui'):
        path_entry = str(entry)
        # print(path_entry[:-3])
        os.system(f'pyuic6 -x {path_entry} -o {path_entry[:-3]}.py')
        print(f'{path_entry} has converted')

    print('end')