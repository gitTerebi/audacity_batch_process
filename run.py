import pipeclient
import os

client = pipeclient.PipeClient()


def run_fast_scandir(dir, ext):  # dir: str, ext: list
    subfolders, files = [], []

    for f in os.scandir(dir):
        if f.is_dir():
            subfolders.append(f.path)
        if f.is_file():
            if (os.path.getsize(f.path) > 4000):
                if os.path.splitext(f.name)[1].lower() in ext:
                    files.append(f.path.replace('\\', r'\\'))

    for dir in list(subfolders):
        sf, f = run_fast_scandir(dir, ext)
        subfolders.extend(sf)
        files.extend(f)
    return subfolders, files


def limit(in_folder, out_folder, limit):
    subfolders, files = run_fast_scandir(in_folder, [".ogg"])
    in_folder = in_folder.replace('\\', r'\\')
    out_folder = out_folder.replace('\\', r'\\')

    # root export
    if not os.path.isdir(out_folder):
        os.makedirs(out_folder)

    # make our sub folders
    for folder in subfolders:
        newFolder = folder.replace(in_folder, out_folder)
        if not os.path.isdir(newFolder):
            os.makedirs(newFolder)

    count = 1
    for file in files:
        newFile = file.replace(in_folder, out_folder)
        client.write("RemoveTracks")
        client.write('Import2: Filename="' + file + '"')
        client.write("SelectAll")
        client.write("Limiter: gain-L=0 gain-R=0 hold=10 makeup=No thresh=" + str(limit) + " type=HardLimit")
        client.write('Export2: Filename="' + newFile + '"')
        print(newFile)
        print(str(count) + "/" + str(len(files)))
        count += 1


limit('c:\folder',
      'c:\out-folder', -1)
