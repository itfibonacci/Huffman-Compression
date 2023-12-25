from frequency_counter import frequency_counter
from priority_queue import priority_queue
from huffman_tree import HuffmanTree

from heapq import heappop

def main():

	txt_file = "135-0.txt"
	#txt_file = "./small_sample.txt"

	frequencies = frequency_counter(txt_file)

	heaped_frequencies = priority_queue(frequencies)
	print(len(heaped_frequencies))
	
	huffman_tree = HuffmanTree()
	huffman_tree.build_tree(heaped_frequencies=heaped_frequencies)
	codes_dict = huffman_tree.build_codes_dict()
	huffman_encoded_text = text_to_codes(txt_file, codes_dict)
	encoded_file = encode(txt_file, codes_dict)
	
	with open(encoded_file) as e_file:
		encoded_string = e_file.read()
	
	encoded_giant_text = code_to_text(encoded_string, codes_dict)

	output_file = f"original_{txt_file}"
	
	with open(output_file, 'w') as outfile:
		outfile.write(encoded_giant_text)
	
	#print(code_to_text(huffman_encoded_text, codes_dict))

def text_to_codes(txt_file, codes_dict):
	result = ""
	with open(txt_file) as file:
		for line in file:
			for char in line:
				result += f"{codes_dict[char]}"
	return result

def encode(txt_file, codes_dict):
	output_file = f"encoded_{txt_file}"
	with open(txt_file) as file:
		with open(output_file, 'w') as outfile:
			for line in file:
				encoded_line = ''.join(codes_dict[char] for char in line)
				outfile.write(encoded_line)
	return output_file

#def decode( huffman_encoded_text_file, char_to_code_dict ):

def code_to_text( huffman_encoded_text, char_to_code_dict):
	# gonna try with a sliding window approach
	code_to_char_dict = {code: char for char, code in char_to_code_dict.items()}
	result = ""
	window_start = 0
	window_end = 1

	while window_end < len(huffman_encoded_text):
		if huffman_encoded_text[window_start:window_end+1] in code_to_char_dict:
			result += code_to_char_dict[huffman_encoded_text[window_start:window_end+1]]
			window_start = window_end + 1
			window_end = window_start + 1
			continue
		window_end += 1

	return result

if __name__ == "__main__":
	main()
