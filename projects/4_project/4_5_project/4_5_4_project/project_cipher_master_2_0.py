class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    # def cipher(self, original_text, shift):
    #     # Метод должен возвращать зашифрованный текст
    #     # с учетом переданного смещения shift.
    #     ch_result = ''
    #     original_text = str.lower(original_text)

    #     for char in original_text:
    #         if char in self.alphabet:
    #             index = self.alphabet.find(char)
    #             new_index = (index + shift) % len(self.alphabet)
    #             ch_result += self.alphabet[new_index]
    #         else:
    #             ch_result += char

    #     return ch_result

    # def decipher(self, cipher_text, shift):
    #     # Метод должен возвращать исходный текст
    #     # с учётом переданного смещения shift.
    #     dch_result = ''
    #     chipher_text = str.lower(cipher_text)

    #     for char in chipher_text:
    #         if char in self.alphabet:
    #             index = self.alphabet.find(char)
    #             new_index = (index - shift) % len(self.alphabet)
    #             dch_result += self.alphabet[new_index]
    #         else:
    #             dch_result += char

    #     return dch_result

    def process_text(self, text, shift, is_encrypt):
        result = ''
        text = str.lower(text)

        for char in text:
            if char in self.alphabet:
                index = self.alphabet.find(char)
                if is_encrypt:
                    new_index = (index + shift) % len(self.alphabet)
                elif not is_encrypt:
                    new_index = (index - shift) % len(self.alphabet)
                result += self.alphabet[new_index]
            else:
                result += char

        return result


# cipher_master = CipherMaster()
# print(cipher_master.cipher(
#     original_text=('Однажды ревьюер принял проект с первого раза, '
#                    'с тех пор я его боюсь'),
#     shift=2
# ))
# print(cipher_master.decipher(
#     cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
#     shift=-3
# ))

# Проверка:
cipher_master = CipherMaster()
print(cipher_master.process_text(
    text=('Однажды ревьюер принял проект с первого раза, '
          'с тех пор я его боюсь'),
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
))
