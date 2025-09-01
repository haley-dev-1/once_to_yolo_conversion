import json
import os
import shutil
import time

# define our class annotations to take ONCE -> YOLO format
YOLO_CLASSES = {
    "Car" : 0,
    "Bus": 1,
    "Truck": 2,
    "Pedestrian": 3,
    "Cyclist": 4
}

# used to grab .json in each camera
def iterate_over_directory(type, dir, cwd):
    json_files_in_path = []
    for subdir in os.listdir(dir):

        # creates output directories ( /000076_output/ ) for each json
        full_path = os.path.join(dir, subdir) # train_infos/data are being iterated over # creates access to the sequences' json
        dynamic_string_reassign = type + "/" + subdir
        new_path = "output/"+dynamic_string_reassign
        os.makedirs(new_path)

        file_name_dynamic = os.path.join(new_path, "output.txt")
        with open(file_name_dynamic, 'w') as f:
            f.write("yo it workd thats crazy")
        
        # within each in new_path i need to create a file     

        for file in os.listdir(full_path):
            full_file_path = os.path.join(full_path, file)
            # if there is a valid file
            if file.endswith(".json"):
                json_files_in_path.append(file)
                # print(convert_annos_to_yolo(full_file_path)) # go into file, returns names
                convert_annos_to_yolo(full_path, file) # go into file, returns names (for now!)

    print("jsons accessed in ",dir, " and ready for altering: ", json_files_in_path,"\n")
    return json_files_in_path 

# this is called on a per-json-file basis
def convert_annos_to_yolo(full_path, file):
    path = os.path.join(full_path, file)
    with open(path, 'r') as convertee_file:
        data = json.load(convertee_file) # file data all loaded in
        # print(data)

        frames = data.get("frames")
        annos = frames[0].get("annos")
        names = annos.get("names")

        # names has a list of names, i eant to dynamically grab that
        YOLO_ANNOTATION = []
        for name in names:
            YOLO_ANNOTATION.append(YOLO_CLASSES[name]) # returns number per

        # print(YOLO_ANNOTATION)
        # replace

    return names

def manage_output_directory(path):
    # print(os.getcwd())
    out_dir = os.path.join(path, "output")
    if(os.path.isdir("output")):
        shutil.rmtree(out_dir)
        print("We already had that directory \n ... Deleted so we can replace file contents") # works
        manage_output_directory(path)
    else:
        print("Creating directory")
        os.makedirs(out_dir)

    # Next, we load the directories with the frame_id/YOLO txt for each object

        

# get each camera's 2dbox information
def iterate_over_for_2d_info(data):
        # for cam, box_2d in data["annos"]["boxes_2d"].items():
        #     print("camera: {cam}")
            
        #     for box in box_2d:
        #         print("box: {box_2d}")
        return 
        
def convert_2d_box_to_yolo(x_center, y_center, bbox):
        # YOLO: class_id x_center y_center width height
        # x_center = x_center_pixels / image_width
        # y_center = y_center_pixels / image_height
        # width = box_width_pixels / image_width
        # height = box_height_pixels / image_height
        # return [x_center, y_center, width, height]
        return

def create_yolo_annos():
    # TODO implement
    return

def main():

    print("\nCurrent:", os.getcwd(), "\n")

    manage_output_directory(os.getcwd())


    # read in json files
    once_train_dir = "data/train/train_infos/data/" # This needs to be iterated over
    once_val_dir = "data/val/val_infos/data/"
    
    once_train_jsons = iterate_over_directory("train", once_train_dir, os.getcwd()) # return list of json files
    once_val_jsons = iterate_over_directory("val", once_val_dir, os.getcwd()) # return list of json

    #print(once_train_jsons)
    for file in once_train_jsons:
        # print(file)
        
        # 1. Grab number of frame Ids
        
        #  
        # 2. For each frame Id within frames, we need to convert the annos, then create this file with yolo annos instead     

        ''' for each json, we use our map and replace each instance of '''


    # convert_annos_to_yolo_format(once_train_jsons) # go into each json
    



    # How do I obtain x_center, y_center, bbox (2d) from once_train and once_val
    #iterate_over_for_2d_info(once_train_json) # print camera + 2dbox info
    #convert_2d_box_to_yolo()

    # we need to convert 2d box info to yolo format
    
    # need to replace the 2d bounding box info for ONCE with the list from convert_2d_box_to_yolo()


    # managing output directories


if __name__ == "__main__":
    main()
