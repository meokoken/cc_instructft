# Converting vicuna's response to formatted QA pairs to finetune the model
## Purpose
- The code for fine-tuning the vicuna model must take in a JSON file format with question and answer pairs instead of JSONL format given by vicunas response
- This file will be able to help convert our output into a JSON file to be used for fine-tuning.

## Methodology
1) place jsonl file/files containing vicuna response in text_vicuna_answers folder
2) run batch_convert_jsonl.py to convert all jsonl files in text_vicuna_answers folder to json format
3) run json_folder_to_json_notext.py to get a jsonl file of neatly formatted question and answer pairs. The answers will be saved in myfile.jsonl.
4) convert myfile.jsonl to json using the command below
   ```bash
   jq -s . <myfile.jsonl > answer.json
   ```
