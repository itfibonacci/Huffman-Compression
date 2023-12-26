from frequency_counter import frequency_counter
from priority_queue import priority_queue
from huffman_tree import HuffmanTree

from heapq import heappop
from argparse import ArgumentParser

import binascii

def main():
	parser = ArgumentParser()
	parser.add_argument("txt_file", help="The text file to be encoded")
	args = parser.parse_args()
	txt_file = args.txt_file

	# frequencies will be the dictionary of the number of occurences for each character.
	# For example: {'a': 122, 'b': 11}
	frequencies = frequency_counter(txt_file)

	# Heapified representation of all the items in the above dictionary as huffman nodes
	heaped_frequencies = priority_queue(frequencies)
	
	# create a HuffmanTree instance
	huffman_tree = HuffmanTree()
	
	# in place changes the passed heapified frequencies of huffman nodes into a
	# huffman tree structured representation
	huffman_tree.build_tree(heaped_frequencies=heaped_frequencies)
	
	# store the dictionary of the char to codes built by the huffman tree method
	# the dictionary looks like this: {'s': '0000', 'i': '0001' ...}
	# so a character and the binary value that the huffman algorithm has assigned it
	char_to_codes_dict = huffman_tree.build_codes_dict()
	
	# Encode the huffman representation into a file then Store the name of the file that has the
	# huffman representation of the initial text passed to it.
	encoded_file = encode(txt_file, char_to_codes_dict)

	with open(encoded_file, 'rb') as e_file:
		encoded_string = e_file.read()
	
	encoded_giant_text = decode(encoded_string, char_to_codes_dict)

	output_file = f"original_{txt_file}"
	
	with open(output_file, 'w') as outfile:
	 	outfile.write(encoded_giant_text)
	
	#print(decode(huffman_encoded_text, char_to_codes_dict))

def encode(txt_file, char_to_codes_dict):
	output_file = f"encoded_{txt_file}"
	with open(txt_file) as file:
		with open(output_file, 'wb') as outfile:
			for line in file:
				encoded_line = ''.join(char_to_codes_dict[char] for char in line)
				binary_encoded_line = int(encoded_line, 2).to_bytes((len(encoded_line) + 7) // 8, byteorder='big')
				#print(binascii.hexlify(binary_encoded_line))
				outfile.write(binary_encoded_line)
	return output_file

def decode( huffman_encoded_text, char_to_code_dict):
	# gonna try with a sliding window approach
	binary_string = ''.join(format(byte, '08b') for byte in huffman_encoded_text)
	code_to_char_dict = {code: char for char, code in char_to_code_dict.items()}
	result = ""
	window_start = 0
	window_end = 1

	while window_end < len(binary_string):
		if binary_string[window_start:window_end+1] in code_to_char_dict:
			result += code_to_char_dict[binary_string[window_start:window_end+1]]
			window_start = window_end + 1
			window_end = window_start + 1
			continue
		window_end += 1

	return result

if __name__ == "__main__":
	main()
