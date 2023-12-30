import re 
import os

with open('text_dir/chunk1.txt', 'r') as f: 
    texts = f.readlines()

print(len(texts))

# Turning paragraph to sentences
'''def edit(input_file,output_file): 
    with open(input_file, 'r') as f: 
        paragraph = f.read()
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', paragraph)
    with open(output_file, 'w') as file: 
        file.write('\n'.join(sentences))

input_file = 'text/example.txt'
output_file = 'sentences.txt'

edit(input_file, output_file)'''

#Extract lines 
'''def extract_line(input_file, chunk_size, output_dir):
    with open(input_file, 'r') as file: 
        data = file.read()
    chunks = [data[i:i+chunk_size] for i in range(0,len(data), chunk_size) ] 
    if not os.path.exists(output_dir): 
        os.makedirs(output_dir)
    for i, chunk in enumerate(chunks): 
        output_file = os.path.join(output_dir, f'chunk{i+1}.txt')
        with open(output_file, 'w') as f: 
            f.write(chunk)
input_file = 'sentences.txt'
chunk_size = 5000000
output_dir = 'text_dir'

extract_line(input_file, chunk_size, output_dir)'''

