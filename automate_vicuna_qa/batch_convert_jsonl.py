# 1) run this file first to convert all jsonl files in folder text_vicuna_answers to json files in the folder answers


import os 

directory = "text_vicuna_answers"

# iterate over files in
# that directory
for filename in os.listdir(directory):
    f1 = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f1) and filename.endswith('.jsonl'):
        f1 = f1.replace('\\' , '/')
        print(f1)
        dir_len = len(directory) + 1
        print(type(f1))
        ori_file_path =  f1
        new_file_path = "converted_vicuna_answers/" + f1[dir_len:-6] + ".json"
        print(new_file_path)
        os.system(f"jq -s . <{ori_file_path} > {new_file_path}")


