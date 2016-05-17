# -*- coding: utf-8 -*-

key = '0F66EEF9BEDD6C499DFEFFC54CFED0F4F10A72F33596DCC12769ABAF3D316EA4'
open_text = '7E9D165AC2568B1B'
D_ParamSet = [[0xF, 0xC, 0x2, 0xA, 0x6, 0x4, 0x5, 0x0, 0x7, 0x9, 0xE, 0xD, 0x1, 0xB, 0x8, 0x3],
              [0xB, 0x6, 0x3, 0x4, 0xC, 0xF, 0xE, 0x2, 0x7, 0xD, 0x8, 0x0, 0x5, 0xA, 0x9, 0x1],
              [0x1, 0xC, 0xB, 0x0, 0xF, 0xE, 0x6, 0x5, 0xA, 0xD, 0x4, 0x8, 0x9, 0x3, 0x7, 0x2],
              [0x1, 0x5, 0xE, 0xC, 0xA, 0x7, 0x0, 0xD, 0x6, 0x2, 0xB, 0x4, 0x9, 0x3, 0xF, 0x8],
              [0x0, 0xC, 0x8, 0x9, 0xD, 0x2, 0xA, 0xB, 0x7, 0x3, 0x6, 0x5, 0x4, 0xE, 0xF, 0x1],
              [0x8, 0x0, 0xF, 0x3, 0x2, 0x5, 0xE, 0xB, 0x1, 0xA, 0x4, 0x7, 0xC, 0x9, 0xD, 0x6],
              [0x3, 0x0, 0x6, 0xF, 0x1, 0xE, 0x9, 0x2, 0xD, 0x8, 0xC, 0x4, 0xB, 0xA, 0x5, 0x7],
              [0x1, 0xA, 0x6, 0x8, 0xF, 0xB, 0x0, 0x4, 0xC, 0x3, 0x5, 0x9, 0x7, 0xD, 0x2, 0xE]]

int_key = int(key, 16)
int_open_text = int(open_text, 16)

bin_key = bin(int_key)[2:].zfill(256)
bin_open_text = bin(int_open_text)[2:].zfill(64)

A = [bin_open_text[32:]]
B = [bin_open_text[:32]]


class GOST_28147_89:
	def __init__(self, paramset, key):
		self.paramset = paramset
		self.key = bin(int(key, 16))[2:].zfill(256)
		self.K = []

	@staticmethod
	def split_key(key):
		list = []
		for i, k in zip(range(0, 225, 32), range(32, 257, 32)):
			list.append(key[i:k])
		list += list[:8]
		list += list[:8]
		list += list[24:15:-1]
		return list

	def f(self, A, K):
		X = bin(int(A, 2) ^ int(K, 2))[2:].zfill(32)
		list = []
		counter = 0
		result = ''
		for i, k in zip(range(0, 29, 4), range(4, 33, 4)):
			list.append(X[i:k])
		for i in list[::-1]:
			result += bin(self.paramset[counter][int(i, 2)])[2:].zfill(4)
			counter += 1
		result = result[11:] + result[:11]
		return result

	def encode(self, open_text):
		return self.simple_replacement(open_text, self.split_key(self.key))

	def decode(self, cipher_text):
		return self.simple_replacement(cipher_text, self.split_key(self.key)[::-1])

	def simple_replacement(self, open_text, K):
		A = [open_text[32:]]
		B = [open_text[:32]]
		for i in range(32):
			A.append(bin(int(B[i], 2) ^ int(self.f(A[i], K[i]), 2))[2:].zfill(32))
			B.append(A[i])
		return A[32] + B[32]

	@staticmethod
	def bin_to_hex(bin):
		return hex(int(bin, 2))


# tests
def test():
	GOST = GOST_28147_89(D_ParamSet, key)
	bin_cipher_text = GOST.encode(bin_open_text)

	print(GOST_28147_89.bin_to_hex(bin_cipher_text))
	new_bin_cipher_text = '0111010111000100000111110000000000100000100110111111011110101011'
	print(GOST_28147_89.bin_to_hex(new_bin_cipher_text))
	new_open_text = GOST.decode(new_bin_cipher_text)
	print(GOST_28147_89.bin_to_hex(new_open_text))
	print(GOST_28147_89.bin_to_hex(
		'0100111101100110111011101111100110111110110111010110110001001001100111011111111011111111110001010100110011111110110100001111010011110001000010100111001011110011001101011001011011011100110000010010011101101001101010111010111100111101001100010110111010100100'))
	new_bin_key = '0100111101100110111011101111100110111110110111010110110001001001100111011111111011111111110001010100110011111110110100001111010011110001000010100111001011110011001101011001011011011100110000010010011101101001101010111010111100111101001100010110111010100100'
	GOST2 = GOST_28147_89(D_ParamSet, new_bin_key)
	bin_cipher_text = GOST.encode(new_open_text)
	print(GOST.bin_to_hex(bin_cipher_text))


test()
