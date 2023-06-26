import json
# command to convert to an array of json format 
# jq -n '[inputs]' <test_convert.jsonl >out2.json

def convert_ans_to_finetune_form(filename):
    with open(filename,'r',encoding="utf8") as file:
        ori_array = json.loads(file.read())

    #to be a dictionary of lists. 
    #These lists contain items which are either questions
    #or answers received by vicuna
    new_dict = {} 
        
    for i in range(len(ori_array)):
        text = str(ori_array[i]["text"])
        list = text.split("\n")
        new_dict[str(i)] = list

    #to be a list of lists
    #each list item consists of 1 question and answer pair
    #purpose of loop is to combine related question and answers together
    new_question_and_ans_list = []
    for key,value in new_dict.items():
        for list_index in range(int(len(value)/2)):
            question_index = list_index * 2 
            answer_index = list_index * 2 + 1
            ques_and_ans_list = [value[question_index], value[answer_index]]
            new_question_and_ans_list.append(ques_and_ans_list)

    # to convert to final list with question and answer pairs as items
    final_json_list = []
    for item in new_question_and_ans_list:
        item_dict = {}
        item_dict["question"] = item[0][13:]
        item_dict["answer"] = item[1][8:]
        item_dict_json = json.dumps(item_dict)
        final_json_list.append(item_dict_json)
    
    return final_json_list







# print(convert_ans_to_finetune_form("convertjson.json"))
# print(convert_ans_to_finetune_form("out.json"))
# print(convert_ans_to_finetune_form("test_ans_overnight.json"))
# print(convert_ans_to_finetune_form("answer_overnight.json"))



#lines taken out 129, 369, 458, 495, 513