class VigenerCipher:
	def __init__(self, alphabet, key):
		self.alphabet = alphabet
		self.key = key
		self.__key_index_list = []
		for char in self.key:
			self.__key_index_list.append(alphabet.index(char))

	def decrypt(self, cipher_text):
		if cipher_text is not None:
			plain_text = ''
			i = 0
			for char in cipher_text:
				if self.alphabet.index(char) - self.__key_index_list[i] >= 0:
					plain_text += self.alphabet[self.alphabet.index(char) - self.__key_index_list[i]]
				else:
					plain_text += self.alphabet[self.alphabet.index(char) - self.__key_index_list[i] + len(self.alphabet)]
				i += 1
				if i >= len(self.key):
					i = 0
			return plain_text
		else:
			return None

	def encrypt(self, plain_text):
		if plain_text is not None:
			cipher_text = ''
			i = 0
			for char in plain_text:
				if self.alphabet.index(char) + self.__key_index_list[i] < len(self.alphabet):
					cipher_text += self.alphabet[self.alphabet.index(char) + self.__key_index_list[i]]
				else:
					cipher_text += self.alphabet[self.alphabet.index(char) + self.__key_index_list[i] - len(self.alphabet)]
				i += 1
				if i >= len(self.key):
					i = 0
			return cipher_text
		else:
			return None
