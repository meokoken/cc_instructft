# Chunking of PDF files 

## Purpose 

Large Language Models (LLMs) have input token limits. 

In order to feed in the PDF files for the LLM to generate Question-Answer (QA) pairs for us, we will need to reduce the PDF files into small chunks to fit the input token size limit.

## Methodology

1. Convert the pdf files into an image
2. Use Optical Character Recognition (OCR) to extract the text from the image 
3. Use LangChain to chunk the text 
4. Loop through each text, while adding a basic prompt that will tell the LLM to generate QA pairs, and append it to a list