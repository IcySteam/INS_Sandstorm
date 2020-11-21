import os

directory = "C:\Program Files (x86)\Steam\steamapps\common\sandstorm\Insurgency\Mods\modio"
for modio_sub in os.listdir(directory):
    if os.path.isdir(directory):
        os.system("del \"" + directory + "\\" + modio_sub + "\\" + "filedata*.zip" + "\"")
        if len([modio_sub_sub for modio_sub_sub in os.listdir(directory + "\\" + modio_sub) if os.path.isdir(directory + "\\" + modio_sub + "\\" + modio_sub_sub)]) > 1:
            ctime_max = 0
            for modio_sub_sub in os.listdir(directory + "\\" + modio_sub):
                if os.path.isdir(directory + "\\" + modio_sub + "\\" + modio_sub_sub) and os.path.getctime(directory + "\\" + modio_sub + "\\" + modio_sub_sub) > ctime_max:
                    ctime_max = os.path.getctime(directory + "\\" + modio_sub + "\\" + modio_sub_sub)
            for modio_sub_sub in os.listdir(directory + "\\" + modio_sub):
                if os.path.isdir(directory + "\\" + modio_sub + "\\" + modio_sub_sub) and os.path.getctime(directory + "\\" + modio_sub + "\\" + modio_sub_sub) < ctime_max:
                    os.system("rmdir /s /q \"" + directory + "\\" + modio_sub + "\\" + modio_sub_sub + "\"")

#input()