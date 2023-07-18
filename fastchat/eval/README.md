# Evaluations

This directory contains end-to-end pipelines for AI-enhanced evaluation. We will introduce the evaluation pipeline and the data format in this document.

## Generate Answers

### Vicuna and other models

To generate answers with Vicuna or other models, specify path to the model checkpoint, a desired model ID and run:
```bash
python get_model_answer.py --model-id [MODEL-ID] --model-path /model/path --question-file table/question.jsonl --answer-file table/answer/answer.jsonl --num-gpus [NUM-GPUS]
```
Then the answers to the questions will be saved in `table/answer/answer.jsonl`.
Note: we assume the model can be loaded with a single GPU.

### Vicuna 13B with our sample model script
```bash
python get_model_answer.py --model-id vicuna-13b --model-path  ../../../13B --question-file table/question.jsonl --answer-file table/answer/answer.jsonl --num-gpus 4
```

## Visualize Results

You can generate the data for the webpage by running:

```bash
python eval/generate_webpage_data_from_table.py
```

Then you can serve a static website in `webpage` to see the results.