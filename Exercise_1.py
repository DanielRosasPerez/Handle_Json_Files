import json, csv, os

path = "home/user/Documents/candidates_documents/"
dictionary_paths = [f"{path}{dict_path}" for dict_path in os.listdir(path) if dict_path != ".ipynb_checkpoints"]

with open("user_data.tsv", 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter='\t')
                
    data_to_save = [("profile_id", "address")] # Placeholders. In this case, the name of the columns.
    
    for path in dictionary_paths:
        # Opening JSON file 
        json_file = open(f"{path}", encoding="utf-8")
        data = json.load(json_file)
        
        # Saving the "profile_id" and "the address" (when type = "work"), from the JSON files:
        flag, support_list = 0, list()
        for field in data:
            if field == "profile_id":
                support_list.append(data[field])
                flag += 1
            elif field == "document" and data[field][0]["type"] == "work":
                support_list.append(data[field][0]["address"]["full_address"])
                flag += 1
            if flag == 2:
                data_to_save.append(tuple(support_list))
                flag, support_list = 0, list()
    
    # Dumping the content inside the "tsv" file.
    for user_data in data_to_save:
        csv_writer.writerow([data_ for data_ in user_data])
    
    json_file.close()
    
"""
IN ORDER TO OPEN THE RESULTING FILE, PLEASE, MAKE RIGHT CLICK ON THE RESULTING FILE, THE GO TO PROPERTIES AND SPECIFY DIRECTLY THAT YOU WANT TO OPEN THIS FILE USING "EXCEL". IF YOU DON'T WANT TO DO THAT YOU CAN OPEN IT WITH "NOTEPAD". Thank you :)
"""