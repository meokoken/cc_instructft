<!-- <div align="center">

  <img src="asset/a_vicuna_sticking_out_its_tongue_playfully.png" alt="gradio" width=300><br>
  <em>Janna and Heng Di's adventure with Vicuna</em>
</div> -->

# CoCo Finetuning Vicuna


## Contents 
- [Introduction](#introduction)
- [Creating dataset](#creating-dataset)
- [Instructions](#instructions)
- [Fine-tuning](#fine-tuning)
- [Demo](#demo)


## Introduction 

We want to be able to finetune [**Vicuna LLM**](https://chat.lmsys.org/) on documents to learn domain knowledge/words for question-answering (QA) purposes.

To achieve that, we plan to create a QA dataset to finetune the Vicuna base model.

## Creating dataset

In order to fine-tune the base model to be able to understand and answer queries based on army documents, we will need to create a QA dataset with relevant questions.

We are given the army documents in the form of a PDF file. 

### Instructions
1) Place your selected pdf files in pdf_files_chunk/pdf_files
2) Navigate to pdf_files_chunk/pdf_chunker.ipynb
3) Chunked file will be written in output.json
4) Convert output.json from json format to jsonl format, place the file in fastchat/eval/table
5) Navigate to fastchat/eval and follow README
6) Now, output.jsonl in table/answer folder contains vicunas response of question and answer pairs. 
7) Follow README in automate_vicuna_qa folder


## Fine-tuning
1) Place output json file of creating dataset in data folder
2) Run Updated_FineTuning_Notebook.ipynb


## Demo
1) Follow README in demo folder 





