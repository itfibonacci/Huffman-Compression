#!/opt/homebrew/Caskroom/miniconda/base/bin/python3
#https://codingchallenges.fyi/challenges/challenge-huffman

# start by building a frequency counter
import time

def frequency_counter(filename):
	frequencies = {}
	with open(filename) as file:
		for line in file:
			for char in line:
				if char in frequencies:
					frequencies[char] += 1
				else:
					frequencies[char] = 1
	end = time.time()
	return frequencies
