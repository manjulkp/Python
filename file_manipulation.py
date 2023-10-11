import os

folder_original = '/Users/manjula/Desktop/'
folder_destination = '/Users/manjula/Desktop/Cleanup'

# create a new folder 
os.mkdir(folder_destination)

for entry in os.scandir(folder_original):
    # create path location
    location_original = os.path.join(folder_original , entry.name)
    location_destination = os.path.join(folder_destination , entry.name)
    #  move only files not folder
    if os.path.isfile(location_original):
        os.rename(location_original , location_destination)
    
