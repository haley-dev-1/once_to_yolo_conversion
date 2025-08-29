import json
import os

# define our class annotations to take ONCE -> YOLO format
YOLO_CLASSES = {
    "Car" : 0,
    "Bus": 1,
    "Truck": 2,
    "Pedestrian": 3,
    "Cyclist": 4
}

# used to grab .json in each camera
def iterate_over_directory(dir):
    json_files_in_path = []
    # get each sequence directory (e.g. 000076) 
    #print("list directories within dir:", os.listdir(dir), "that need access")
    for subdir in os.listdir(dir):
        full_path = os.path.join(dir, subdir) # creates access to the sequences' json
        #print(full_path) # works, prints full path
        for file in os.listdir(full_path):
            full_file_path = os.path.join(full_path, file)
            if file.endswith(".json"):
                #print(file, "accessed!")
                json_files_in_path.append(file)
                
                ''' '''
                convert_annos_to_yolo(full_file_path) # go into file 
                ''' '''

    print("jsons accessed in ",dir, " and ready for altering: ", json_files_in_path,"\n")
    return json_files_in_path 

# this is called on a per-json-file basis
def convert_annos_to_yolo(path):
    with open(path, 'r') as convertee_file:
        data = json.load(convertee_file) # file data all loaded in

        # loop over data on per-frame basis and see if there is an annos
    if "annos" not in data:
        print("- - - - > Skipping ", path, " - - - > no annos field")
        return
    else:
        boxes_2d = data["annos"]["boxes_2d"]
        print(boxes_2d)

    # # find and load in info from boxes_2d

    return

def manage_output_directory(path):
    # print(os.getcwd())
    if(os.path.isdir("output")):
        # print("we have that directory") # works
        # clear contents of output
        return
    else:
        # print("no!!!!!!")
        # we need to:
            # add output to path
            # copy original paths with the correct jsons per 
        return
        

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

    # read in json files
    once_train_dir = "data/train/train_infos/data/" # This needs to be iterated over
    once_val_dir = "data/val/val_infos/data/"
    
    once_train_jsons = iterate_over_directory(once_train_dir) # return list of json files
    once_val_jsons = iterate_over_directory(once_val_dir) # return list of json

    '''for each json, we use our map and replace each instance of '''
    # convert_annos_to_yolo_format(once_train_jsons) # go into each json
    



    # How do I obtain x_center, y_center, bbox (2d) from once_train and once_val
    #iterate_over_for_2d_info(once_train_json) # print camera + 2dbox info
    #convert_2d_box_to_yolo()

    # we need to convert 2d box info to yolo format
    
    # need to replace the 2d bounding box info for ONCE with the list from convert_2d_box_to_yolo()


    # managing output directories
    manage_output_directory(once_train_dir)


if __name__ == "__main__":
    main()
