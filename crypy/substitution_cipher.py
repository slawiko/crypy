class AlphabetKeyLenError(Exception):
	def __init__(self, alphabet_len, key_len):
		print('Error: Alphabet len must be equal to the key len'.format(alphabet_len, key_len))


class SubstitutionCipher:
	def __init__(self, alphabet, key):
		if len(alphabet) != len(key):
			raise AlphabetKeyLenError(alphabet_len=len(alphabet), key_len=len(key))
		else:
			self.alphabet = alphabet
			self.key = key

	def encrypt(self, open_text):
		if open_text is not None:
			cipher_text = ''
			for char in open_text:
				try:
					index = self.alphabet.index(char)
					cipher_text += self.key[index]
				except ValueError:
					print('Error: alphabet must contains each char of plain text')
					return None
			return cipher_text
		else:
			return None

	def decrypt(self, cipher_text):
		if cipher_text is not None:
			plain_text = ''
			for char in cipher_text:
				try:
					index = self.key.index(char)
					plain_text += self.alphabet[index]
				except ValueError:
					print('Error: key must contains each char of cipher text')
					return None
			return plain_text
		else:
			return None
