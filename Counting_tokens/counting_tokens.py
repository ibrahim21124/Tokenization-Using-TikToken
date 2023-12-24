# -*- coding: utf-8 -*-
# Counting_Tokens.py

# Installing Dependencies

import tiktoken
import os
import numpy as np
import sys
import pandas as pd

# Loading Data

# Add your Path over Here
path = sys.argv[1]

dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")

# prints all files
print(dir_list)

for file_list in dir_list:
  print(os.path.join(path, file_list))

data = []

for file_list in dir_list:
  with open(os.path.join(path, file_list), 'r') as file:
    data.append(file.read())

len(data)

# Comparing Tokens

cl100k_num_tokens_array = []
cl100k_num_token_bytes = []
p50k_num_tokens_array = []
p50k_num_token_bytes = []
r50k_num_tokens_array = []
r50k_num_token_bytes = []
encoders = ["r50k_base", "p50k_base", "cl100k_base"]

def compare_encodings(example_string: str) -> None:
    """Prints a comparison of three string encodings."""
    # for each encoding, check the number of tokens and token strings
    for encoding_name in encoders:
        encoding = tiktoken.get_encoding(encoding_name)
        token_integers = encoding.encode(example_string)
        num_tokens = len(token_integers)
        token_bytes = [encoding.decode_single_token_bytes(token) for token in token_integers]
        match encoding_name:
          case 'r50k_base':
            r50k_num_tokens_array.append(num_tokens)
            r50k_num_token_bytes.append(token_bytes)
          case 'p50k_base':
            p50k_num_tokens_array.append(num_tokens)
            p50k_num_token_bytes.append(token_bytes)
          case 'cl100k_base':
            cl100k_num_tokens_array.append(num_tokens)
            cl100k_num_token_bytes.append(token_bytes)
          case _:
            print("Incorrect Encoder")

for text in data:
  compare_encodings(text)

# Converting ByteStrings to Strings

cl100k_tokens = []

for texts in cl100k_num_token_bytes:
  cl100k_tokens.append([x.decode('utf-8') for x in texts])

p50k_tokens = []

for texts in p50k_num_token_bytes:
  p50k_tokens.append([x.decode('utf-8') for x in texts])

r50k_tokens = []

for texts in r50k_num_token_bytes:
  r50k_tokens.append([x.decode('utf-8') for x in texts])

#Converting to DataFrame

dir_list

data_frame = {
    "File Path" : path,
    "Name of the File" : dir_list,
    "CL100K Number Tokens" : cl100k_num_tokens_array,
    "CL100K Token Strings" : cl100k_tokens,
    "P50K Number Tokens" : p50k_num_tokens_array,
    "P50K Token Strings" : p50k_tokens,
    "R50K Number Tokens" : r50k_num_tokens_array,
    "R50K Token Strings" : r50k_tokens,
}

df = pd.DataFrame(data_frame)
df.to_csv('TestTokens.csv')