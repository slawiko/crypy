from crypy.substitution_cipher import SubstitutionCipher


def test_vigener():
	cp = SubstitutionCipher(alphabet='АБВГДЕ ЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', key='ЛКВЪФЯЕЩШИАЫЗМГД НУЬХЭЖТРОЁЧПЙБЮЦС')
	assert cp.decrypt('КЭФЯХЯЕДЛЕФ ЬЗЯЕФЭГЛХБ') == 'БУДЕТЕ НА ДОСКЕ ДУМАТЬ'
	assert cp.encrypt('БУДЕТЕ НА ДОСКЕ ДУМАТЬ') == 'КЭФЯХЯЕДЛЕФ ЬЗЯЕФЭГЛХБ'
