# Audacity Batch Process

Uses python and pipeclient to run batch process on audio files inside Audacity.

Script will run on parent folder, search through all subfolders and output processed audio files in same folder structure.

Example

limit('c:\folder','c:\out-folder', -1)

Will run audacity limiter (-1db) on all files and sub folders.

---

Audacity portion

client.write("RemoveTracks")
client.write('Import2: Filename="' + file + '"')
client.write("SelectAll")
client.write("Limiter: gain-L=0 gain-R=0 hold=10 makeup=No thresh=" + str(limit) + " type=HardLimit")
client.write('Export2: Filename="' + newFile + '"')
        
