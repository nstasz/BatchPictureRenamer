from tkinter import *
import tkinter as tk 
import os
import shutil

window = Tk()
window.geometry("940x600+100+100")
window.resizable(width=True, height=True)
window.title("Batch Image Renamer - v. 0.9 by Norbert Staszak")


start_offset_x = 10
start_offset_y = 60

textbox_width = 180
textbox_height = 200

offset_grid_position_x = 0
offset_grid_position_y = 0

grid_spacing_constant_x = 30
grid_spacing_constant_y = 30

offset_y_label_constant = -20

quote = """DEXX-000007
DEXX-000008
DEXX-000009
DEXX-000010
DEXX-000011
DEXX-000012
DEXX-000013
DEXX-000014"""

quote_skus_supplier = """a_0001
a_0002
a_0004
a_0007
a_0008
a_00019
a_00051
a_000421""" 

quote_batchids = """20180817-811-2c
20420818-812-2b
20420818-812-1a
20420818-812-1a
20420818-812-4a
20420818-812-2c
20420818-812-2b
20420818-812-1a"""

#quote_batchids = ""

Label_Path= tk.Label(window, text="Path for Images Directory", borderwidth=0, font=("Helvetica", 10))
Label_Path.place(x = start_offset_x, y = start_offset_x)

Text_Path = Entry(window)
Text_Path.place(x = start_offset_x+150+10, y = start_offset_x, width=250)
#Text_Path.insert(0,"C:\\Users\\Norbert\\Desktop\\Pictures Present Times 2018-08-24")

current_script_path = os.path.realpath(__file__)
script_local_name = current_script_path.split("\\")[-1]
desired_length = len(current_script_path)-len(script_local_name)-1 #-1, because you want to erase the last "\" sign
current_script_path=current_script_path[0:desired_length]
Text_Path.insert(0,current_script_path)






Label_SKUsOur = tk.Label(window, text="Our SKUs", borderwidth=0, bg="black", fg="white", font=("Helvetica", 10))
Label_SKUsOur.place(x = start_offset_x+offset_grid_position_x, y = start_offset_y+offset_grid_position_y+offset_y_label_constant, width=textbox_width)

Text_SKUsOur = Text(window,font=("Deja Vu Sans Mono", 9))
Text_SKUsOur.place(x = start_offset_x+offset_grid_position_x, y = start_offset_y+offset_grid_position_y, height=textbox_height, width=textbox_width)
Scrollbar_SKUsOur = Scrollbar(window)
Scrollbar_SKUsOur.place(x = start_offset_x+textbox_width+offset_grid_position_x, y = start_offset_y+offset_grid_position_y, height=textbox_height)
Scrollbar_SKUsOur.config(command=Text_SKUsOur.yview)
Text_SKUsOur.config(yscrollcommand=Scrollbar_SKUsOur.set)
Text_SKUsOur.insert(END, quote)

offset_grid_position_x = 1*(grid_spacing_constant_x+(textbox_width))
offset_grid_position_y = 0*(grid_spacing_constant_y+(textbox_height))



Label_SKUsSupplier = tk.Label(window, text="Supplier SKUs", borderwidth=0, bg="black", fg="white", font=("Helvetica", 10))
Label_SKUsSupplier.place(x = start_offset_x+offset_grid_position_x, y = start_offset_y+offset_grid_position_y+offset_y_label_constant, width=textbox_width)

Text_SKUsSupplier = Text(window,font=("Courier New", 9))
Text_SKUsSupplier.place(x = start_offset_x+offset_grid_position_x, y = start_offset_y+offset_grid_position_y, height=textbox_height, width=textbox_width)
Scrollbar_SKUsSupplier = Scrollbar(window)
Scrollbar_SKUsSupplier.place(x = start_offset_x+textbox_width+offset_grid_position_x, y = start_offset_y+offset_grid_position_y, height=textbox_height)
Scrollbar_SKUsSupplier.config(command=Text_SKUsSupplier.yview)
Text_SKUsSupplier.config(yscrollcommand=Scrollbar_SKUsSupplier.set)
Text_SKUsSupplier.insert(END, quote_skus_supplier)

offset_grid_position_x = 2*(grid_spacing_constant_x+(textbox_width))
offset_grid_position_y = 0*(grid_spacing_constant_y+(textbox_height))


Label_BatchIDs = tk.Label(window, text="Batch ID for each SKU", borderwidth=0, bg="black", fg="white", font=("Helvetica", 10))
Label_BatchIDs.place(x = start_offset_x+offset_grid_position_x, y = start_offset_y+offset_grid_position_y+offset_y_label_constant, width=textbox_width)

Text_BatchIDs = Text(window,font=("Courier New", 9))
Text_BatchIDs.place(x = start_offset_x+offset_grid_position_x, y = start_offset_y+offset_grid_position_y, height=textbox_height, width=textbox_width)
Scrollbar_BatchIDs = Scrollbar(window)
Scrollbar_BatchIDs.place(x = start_offset_x+textbox_width+offset_grid_position_x, y = start_offset_y+offset_grid_position_y, height=textbox_height)
Scrollbar_BatchIDs.config(command=Text_BatchIDs.yview)
Text_BatchIDs.config(yscrollcommand=Scrollbar_BatchIDs.set)
Text_BatchIDs.insert(END, quote_batchids)

offset_grid_position_x = 0*(grid_spacing_constant_x+(textbox_width))
offset_grid_position_y = 1*(grid_spacing_constant_y+(textbox_height))

##### 2ND ROW

Label_Inbound = tk.Label(window, text="Supplier SKUs in Inbound dir", borderwidth=0, bg="yellow", fg="black", font=("Helvetica", 10))
Label_Inbound.place(x = start_offset_x+offset_grid_position_x, y = start_offset_y+offset_grid_position_y+offset_y_label_constant, width=textbox_width)

Text_Inbound = Text(window,font=("Courier New", 9))
Text_Inbound.place(x = start_offset_x+offset_grid_position_x, y = start_offset_y+offset_grid_position_y, height=textbox_height, width=textbox_width)
Scrollbar_Inbound = Scrollbar(window)
Scrollbar_Inbound.place(x = start_offset_x+textbox_width+offset_grid_position_x, y = start_offset_y+offset_grid_position_y, height=textbox_height)
Scrollbar_Inbound.config(command=Text_Inbound.yview)
Text_Inbound.config(yscrollcommand=Scrollbar_Inbound.set)

offset_grid_position_x = 1*(grid_spacing_constant_x+(textbox_width))
offset_grid_position_y = 1*(grid_spacing_constant_y+(textbox_height))


Label_Approved = tk.Label(window, text="Supplier SKUs in Approved dir", borderwidth=0, bg="lightgreen", fg="black", font=("Helvetica", 10))
Label_Approved.place(x = start_offset_x+offset_grid_position_x, y = start_offset_y+offset_grid_position_y+offset_y_label_constant, width=textbox_width)

Text_Approved = Text(window,font=("Courier New", 9))
Text_Approved.place(x = start_offset_x+offset_grid_position_x, y = start_offset_y+offset_grid_position_y, height=textbox_height, width=textbox_width)
Scrollbar_Approved = Scrollbar(window)
Scrollbar_Approved.place(x = start_offset_x+textbox_width+offset_grid_position_x, y = start_offset_y+offset_grid_position_y, height=textbox_height)
Scrollbar_Approved.config(command=Text_Approved.yview)
Text_Approved.config(yscrollcommand=Scrollbar_Approved.set)



offset_grid_position_x = 2*(grid_spacing_constant_x+(textbox_width))
offset_grid_position_y = 1*(grid_spacing_constant_y+(textbox_height))


Label_Shared = tk.Label(window, text="Supplier SKUs in both dirs", borderwidth=0, bg="lightblue", fg="black", font=("Helvetica", 10))
Label_Shared.place(x = start_offset_x+offset_grid_position_x, y = start_offset_y+offset_grid_position_y+offset_y_label_constant, width=textbox_width)

Text_Shared = Text(window,font=("Courier New", 9))
Text_Shared.place(x = start_offset_x+offset_grid_position_x, y = start_offset_y+offset_grid_position_y, height=textbox_height, width=textbox_width)
Scrollbar_Shared = Scrollbar(window)
Scrollbar_Shared.place(x = start_offset_x+textbox_width+offset_grid_position_x, y = start_offset_y+offset_grid_position_y, height=textbox_height)
Scrollbar_Shared.config(command=Text_Shared.yview)
Text_Shared.config(yscrollcommand=Scrollbar_Shared.set)

##### ROW 2,5: Labels with length

label_variable_found_inbound = StringVar()
label_variable_found_approved = StringVar()
label_variable_found_shared = StringVar()

label_variable_found_inbound.set("Found: 0")
label_variable_found_approved.set("Found: 0")
label_variable_found_shared.set("Found: 0")

offset_grid_position_x = 0*(grid_spacing_constant_x+(textbox_width))
offset_grid_position_y = 2*(grid_spacing_constant_y+(textbox_height))-20
Label_Found_Inbound = tk.Label(window, textvariable=label_variable_found_inbound, borderwidth=0, fg="black", font=("Helvetica", 10))
Label_Found_Inbound.place(x = start_offset_x+offset_grid_position_x, y = start_offset_y+offset_grid_position_y+offset_y_label_constant, width=textbox_width)

offset_grid_position_x = 1*(grid_spacing_constant_x+(textbox_width))
offset_grid_position_y = 2*(grid_spacing_constant_y+(textbox_height))-20
Label_Found_Approved = tk.Label(window, textvariable=label_variable_found_approved, borderwidth=0, fg="black", font=("Helvetica", 10))
Label_Found_Approved.place(x = start_offset_x+offset_grid_position_x, y = start_offset_y+offset_grid_position_y+offset_y_label_constant, width=textbox_width)

offset_grid_position_x = 2*(grid_spacing_constant_x+(textbox_width))
offset_grid_position_y = 2*(grid_spacing_constant_y+(textbox_height))-20
Label_Found_Shared = tk.Label(window, textvariable=label_variable_found_shared, borderwidth=0, fg="black", font=("Helvetica", 10))
Label_Found_Shared.place(x = start_offset_x+offset_grid_position_x, y = start_offset_y+offset_grid_position_y+offset_y_label_constant, width=textbox_width)

##### LOG

offset_grid_position_x = 3*(grid_spacing_constant_x+(textbox_width))
offset_grid_position_y = 0*(grid_spacing_constant_y+(textbox_height))


Label_Log = tk.Label(window, text="Log", borderwidth=0, bg="lightgrey", fg="black", font=("Helvetica", 10))
Label_Log.place(x = start_offset_x+offset_grid_position_x, y = start_offset_y+offset_grid_position_y+offset_y_label_constant, width=textbox_width*1.5)

Text_Log = Text(window,font=("Helvetica", 9), wrap=tk.WORD)
Text_Log.place(x = start_offset_x+offset_grid_position_x, y = start_offset_y+offset_grid_position_y, height=textbox_height*2+grid_spacing_constant_y, width=textbox_width*1.5)
Scrollbar_Log = Scrollbar(window)
Scrollbar_Log.place(x = start_offset_x+textbox_width*1.5+offset_grid_position_x, y = start_offset_y+offset_grid_position_y, height=textbox_height*2+grid_spacing_constant_y)
Scrollbar_Log.config(command=Text_Log.yview)
Text_Log.config(yscrollcommand=Scrollbar_Log.set)


### BUTTON START SCRIPTS
def retrieve_dir_path():
	dir_path_local = Text_Path.get()
	dir_path_local = dir_path_local.replace("\\", "/")
	print(dir_path_local)
	return dir_path_local
	
def retrieve_input(local_textbox,get_batch_id_short):
	local_string = local_textbox.get("1.0",'end-1c')
	local_list = []
	for eachline in local_string.splitlines():
		if get_batch_id_short == True:
			eachline=eachline[len(eachline)-2:len(eachline)] #only the number (that is, hopefully, 1, 2 or 4) and the letter are stored here
		local_list.append(eachline)
	return local_list
def test_for_equal_string_length(list1,list2):
	if len(list1) == len(list2):
            print("Same length of lists (SKU Our, SKU Supplier).\n")
            Text_Log.insert(END,"Same length of lists (SKU Our, SKU Supplier).\n")
            return True
	else:
            print("The strings are not of equal length.\n")
            Text_Log.insert(END,"The strings are not of equal length.\n")
            return False
		
def test_for_batch_ids_length(a,b):
    if a == b:
        print("Correct length of Batch IDs.\n")
        Text_Log.insert(END,"Correct length of Batch IDs.\n")
        return True, False #second False for no error
    elif a != b:
        if b == 0:
            print("No Batch IDs used, some functions are disabled.\n")
            Text_Log.insert(END,"No Batch IDs used, some functions are disabled.\n")
            return False, False
        else:
            print("Error: More than 0 Batch IDs, but not equal to number of SKUs.\n")
            Text_Log.insert(END,"Error: More than 0 Batch IDs, but not equal to number of SKUs.\n")
            return False, True

def finding_path_of_dir(path_script):
    inbound=""
    approved=""
    for dir_names in os.listdir(path_script):
        if ("2"  in dir_names) or ("Inbound"  in dir_names) or ("inbound"  in dir_names):
            inbound = path_script+"\\"+dir_names
        if ("4"  in dir_names) or ("Approved"  in dir_names) or ("approved"  in dir_names):
            approved = path_script+"\\"+dir_names                
    return inbound,approved

def check_if_batch_id_is_present (batch_list, batch_character):
    batch_character=batch_character[0:0]
    if batch_character in batch_list:
        print("Working with Batch ID type "+batch_character+".\n")
        Text_Log.insert(END,"Working with Batch ID type "+batch_character+".\n")
        return True
    else:
        return False

def check_correspondance_batch_id_and_dir(batch_character,dir1,dir2):
    print("Directory 1: "+dir1)
    print("Directory 2: "+dir2)
    if (len(dir1) > 8) or (len(dir2)> 8): #it ought to be greater than the names of the dirnames
        print("Found directory corresponding with Batch ID type "+batch_character+".\n")
        Text_Log.insert(END,"Found directory corresponding with Batch ID type "+batch_character+".\n")
        return True
    else:
        print("Did not find the directory corresponding with Batch ID type "+batch_character+".\n")
        Text_Log.insert(END,"Did not find the directory corresponding with Batch ID type "+batch_character+".\n")
        error_did_not_find_dir()
        return False

def error_did_not_find_dir():
        print("ERROR: The necessary dir was not found.\n")
        Text_Log.insert(END,"ERROR: The necessary dir was not found.\n")

def finding_content_of_dir(local_path):
    local_list = []

    for root, dirs, files in os.walk(local_path):  
        for filename in files:
            local_list.append(filename)
    print(local_path+": "+str(local_list))
    return local_list
 
def remove_file_extension(local_list):
    new_product_list =[]
    new_extension_list = []
    for picture in local_list:
        suffix = picture.split(".")[-1]   #-1 = from the end
        suffix = suffix
        desired_length = len(picture)-len(suffix)-1 #-1, because I want to erase the "." character
        picture=picture[0:desired_length]
        new_product_list.append(picture)
        new_extension_list.append(suffix)
    print("without file extension: "+str(new_product_list))
    print("suffixes found: "+str(new_extension_list)) 
    return new_product_list,new_extension_list

def remove_modmood_extension(local_list):
    new_list =[]
    for picture in local_list:
        if "_mod" in picture:
            picture=picture[0:len(picture)-4]
        if "_mood" in picture:
            picture=picture[0:len(picture)-5]   
        new_list.append(picture)
    print("without modmood extension: "+str(new_list))    
    return new_list

def remove_number_extension(local_list):
    new_list =[]
    for picture in local_list:
        if "_" in picture:
            suffix = picture.split("_")[-1]   #-1 = from the end
            desired_length = len(picture)-len(suffix)-1 #-1, because I want to erase the "_" character
            picture=picture[0:desired_length]
        new_list.append(picture)
    print("without number extension: "+str(new_list))    
    return new_list

def remove_duplicate_picture_names(local_list):
    new_list =[]
    list_length = len(local_list)
    for i in range(list_length):
        if i > 0:
            if not local_list[i-1] == local_list[i]:
                new_list.append(local_list[i])
        else: #if i = 0, for the first one
            new_list.append(local_list[i])
    return new_list
 	
 	
def finding_shared_skus(list1,list2):
    new_list = []
    for sku in list1:
        if sku in list2:
            new_list.append(sku)
    return new_list
 	
def display_directory_in_box(boxname,listname):
    for member in listname:
        boxname.insert(END,str(member)+"\n")


### Creating subdirs
def check_dirs_for_batch_id_create_subdirs(local_path,list_input, list_found, list_batch_short, list_batch_full):
    print("test")
#    for item in range(len(list_input)):
#        if list_input[item] in list_found:
#            new_subdir = local_path+"\\"+list_batch_short[item]+" TMP "+list_batch_full[item]
#            if not os.path.isdir(new_subdir):
#                os.makedirs(new_subdir)
### RENAMING SCRIPTS
            
            
            
def rename_products(source_type,local_path, full_files_list, skus_in_files, skus_in_files_with_duplicates, file_no_image_ext, ext_list, input_ww, input_supplier, batch_id_short, batch_id_full, any_batch_ids):
    last_file_sku=""
    last_file_int=1
    list_renamed=[]
    for i in range(len(full_files_list)):
        if skus_in_files_with_duplicates[i] in input_supplier:

            current_index = input_supplier.index(skus_in_files_with_duplicates[i])
            if any_batch_ids == True:
                bici = batch_id_short[current_index]
            old_file_name = local_path+"\\"+full_files_list[i]
            dir_naming_exception = False
               
            #new_file_dir = local_path+"\\"+batch_id_short[current_index]+" TMP "+batch_id_full[current_index]+"\\"
            new_file_sku = input_ww[current_index]
            if last_file_sku == new_file_sku:
                new_file_int = last_file_int+1
            else:
                new_file_int = 1
                Text_Log.insert(END,"Found: "+skus_in_files_with_duplicates[i]+"\n")
            if any_batch_ids == True:    
                if source_type == "inbound":
                    if new_file_int > 1: #in the Inbound dir there should be max. 1 pic per SKU - otherwise it should not be there
                        if bici[0:1] != "2":
                            path_for_additional_pics_in_inbound = local_path+"\\Upload later "+batch_id_short[current_index]+" TMP "+batch_id_full[current_index]+"\\"
                            if not os.path.isdir(path_for_additional_pics_in_inbound):
                                os.makedirs(path_for_additional_pics_in_inbound)
                            new_file_dir = path_for_additional_pics_in_inbound
                            dir_naming_exception = True
                
                    if bici[0:1] == "2": # there should be no batch id "2x" pics in the inbound dir
                        path_for_approved_pics_in_inbound = local_path+"\\Wrong dir "+batch_id_short[current_index]+" TMP "+batch_id_full[current_index]+"\\"
                        if not os.path.isdir(path_for_approved_pics_in_inbound):
                            os.makedirs(path_for_approved_pics_in_inbound)
                        new_file_dir = path_for_approved_pics_in_inbound
                        dir_naming_exception = True
                    
            last_file_sku = new_file_sku
            last_file_int = new_file_int
            this_file=file_no_image_ext[i]
            print(this_file[len(this_file)-3:len(this_file)])
            if (this_file[len(this_file)-3:len(this_file)] == "mod") or (this_file[len(this_file)-4:len(this_file)] == "mood"):
                print("found a mod")
                new_file_suffix ="_"+str(new_file_int)+"_mod."+ext_list[i]
            else:
                new_file_suffix ="_"+str(new_file_int)+"."+ext_list[i]
            
            if any_batch_ids == True:
                if source_type == "approved":

                    if bici[0:1] == "1": # if there are inbounds in the approved directory, they are probably mods
                        path_for_inbound_pics_in_approved = local_path+"\\Inbound moods "+batch_id_short[current_index]+" TMP "+batch_id_full[current_index]+"\\"
                        if not os.path.isdir(path_for_inbound_pics_in_approved):
                            os.makedirs(path_for_inbound_pics_in_approved)
                        new_file_dir = path_for_inbound_pics_in_approved
                        if not "mod" in new_file_suffix:
                            new_file_suffix ="_"+str(new_file_int+1)+"_mod."+ext_list[i]
                        dir_naming_exception = True
           
                if dir_naming_exception == False:   
                    new_file_dir = local_path+"\\"+batch_id_short[current_index]+" TMP "+batch_id_full[current_index]+"\\"
                    if not os.path.isdir(new_file_dir):
                        os.makedirs(new_file_dir)
            else: 
                    new_file_dir = local_path+"\\"+"TMP"+"\\"
                    if not os.path.isdir(new_file_dir):
                        os.makedirs(new_file_dir)                
            new_file_name = new_file_dir+new_file_sku+new_file_suffix
            old_file_name = old_file_name.replace("\\", "/")
            new_file_name = new_file_name.replace("\\", "/")
            if os.path.isfile(new_file_name) == False:
                shutil.copy(old_file_name, new_file_name)
            if skus_in_files_with_duplicates[current_index] not in list_renamed:
                list_renamed.append(skus_in_files_with_duplicates[current_index])
        else:
            Text_Log.insert(END,"File "+file_no_image_ext[i]+" not in the list.\n")
    return(list_renamed)

def display_not_renamed(input_supplier,list1,list2):
    list_renamed = list1+list2
    print(list_renamed)
    for eachline in input_supplier:
        if eachline not in list_renamed:
            Text_Log.insert(END,"Not renamed: "+eachline+"\n")   
        
###Button Scripts
        
def btn_clear_path():
    Text_Path.delete(0,END)
    
####
####
#### MAIN SEQUENCING HERE####
####
####
def btn_start_click():
    path = retrieve_dir_path()
    #RETRIEVE INPUTS
    input1 = retrieve_input(Text_SKUsOur,False)
    input2 = retrieve_input(Text_SKUsSupplier,False)
    input3_short = retrieve_input(Text_BatchIDs,True)
    input3_full = retrieve_input(Text_BatchIDs,False)
    
    #Check if the lengths of three inputs are OK.
    if test_for_equal_string_length(input1,input2) == True:
        number_of_skus = len(input1)
    else:
        return
    
    all_batch_ids_bool,is_error = test_for_batch_ids_length(len(input1),len(input3_short))
    if is_error == True:
        return
    #Search for directories
    path_inbound, path_approved = finding_path_of_dir(path)
    
    
    #Check if specific Batch IDs are present, then check if the corresponding directories are present
    boolean_batchid_1 = check_if_batch_id_is_present(input3_short,"1")
    boolean_batchid_2 = check_if_batch_id_is_present(input3_short,"2")
    boolean_batchid_4 = check_if_batch_id_is_present(input3_short,"4")
    
    
    if boolean_batchid_1 == True:
        boolean_corresponding_dir_found = check_correspondance_batch_id_and_dir("1",path_inbound,"")
    if boolean_batchid_2 == True:
        boolean_corresponding_dir_found = check_correspondance_batch_id_and_dir("2",path_approved,"")
    if boolean_batchid_4 == True:
        boolean_corresponding_dir_found = check_correspondance_batch_id_and_dir("4",path_inbound,path_approved)
        
    
    #Define lists	
    list_inbound_full = finding_content_of_dir(path_inbound)
    list_approved_full = finding_content_of_dir(path_approved)
	
    list_inbound_all_pictures_without_file_extension,list_inbound_extensions = remove_file_extension(list_inbound_full)		
    list_approved_all_pictures_without_file_extension,list_approved_extensions = remove_file_extension(list_approved_full)

    list_inbound_all_pictures_without_modmood_extension = remove_modmood_extension(list_inbound_all_pictures_without_file_extension)		
    list_approved_all_pictures_without_modmood_extension = remove_modmood_extension(list_approved_all_pictures_without_file_extension)

    list_inbound_all_pictures_without_any_extensions = remove_number_extension(list_inbound_all_pictures_without_modmood_extension)		
    list_approved_all_pictures_without_any_extensions = remove_number_extension(list_approved_all_pictures_without_modmood_extension)

    list_inbound_skus = remove_duplicate_picture_names(list_inbound_all_pictures_without_any_extensions)		
    list_approved_skus = remove_duplicate_picture_names(list_approved_all_pictures_without_any_extensions)
	
    list_shared_without_any_exentions = finding_shared_skus(list_inbound_skus,list_approved_skus)

    display_directory_in_box(Text_Inbound,list_inbound_skus)
    display_directory_in_box(Text_Approved,list_approved_skus)
    display_directory_in_box(Text_Shared,list_shared_without_any_exentions)
    label_variable_found_inbound.set("Found: "+str(len(list_inbound_skus)))
    label_variable_found_approved.set("Found: "+str(len(list_approved_skus)))
    label_variable_found_shared.set("Found: "+str(len(list_shared_without_any_exentions)))
    

        ####RENAMING PART OF THE CODE

    
    ### Checking which pictures are in which dir (inbounds in approved, approved in inbounds etc.)
    check_dirs_for_batch_id_create_subdirs(path_inbound, input2, list_inbound_skus, input3_short, input3_full)
    check_dirs_for_batch_id_create_subdirs(path_approved, input2, list_approved_skus, input3_short, input3_full)
    ## - Rename
    Text_Log.insert(END,"\n\nRenaming INBOUND directory...\n")
    list_renamed_inbound=rename_products("inbound",path_inbound, list_inbound_full, list_inbound_skus, list_inbound_all_pictures_without_any_extensions, list_inbound_all_pictures_without_file_extension, list_inbound_extensions, input1, input2, input3_short, input3_full,all_batch_ids_bool)
    
    Text_Log.insert(END,"\nRenaming APPROVED directory...\n")
    list_renamed_approved=rename_products("approved",path_approved, list_approved_full, list_approved_skus, list_approved_all_pictures_without_any_extensions, list_approved_all_pictures_without_file_extension, list_approved_extensions, input1, input2, input3_short, input3_full,all_batch_ids_bool)   
    
    #Display what was not renamied
    display_not_renamed(input2,list_renamed_inbound,list_renamed_approved)


        
Btn_Clear_Path = tk.Button(window, text ="Clear path",  bd=2, command=btn_clear_path)
offset_grid_position_x = 2*(grid_spacing_constant_x+(textbox_width))
Btn_Clear_Path.place(x = start_offset_x+offset_grid_position_x, y = start_offset_x, width=textbox_width/2)

Btn_Start = tk.Button(window, text ="START",  bd=2, bg="lightgreen",command=btn_start_click)
offset_grid_position_x = 3*(grid_spacing_constant_x+(textbox_width))
Btn_Start.place(x = start_offset_x+offset_grid_position_x, y = start_offset_x,width=textbox_width*1.5)


window.mainloop(0)
