from string import ascii_lowercase

a=list(ascii_lowercase)

def find_key(plaintext, ciphertext):
    i=0
    while plaintext[i] not in a:
        i+=1
    return ord(ciphertext[i])-ord(plaintext[i])


def decrypt(ciphertext, key):
    result=[]
    for i in ciphertext:
        if i in a:

            if ord(i)-key<97:

                result.append(chr(ord(i)-key+26))
            else:
                result.append(chr(ord(i) - key))
        else:
            result.append(i)
    b = ''.join(result)
    return b


if __name__ == '__main__':
    plain_text = 'hello, world'
    cipher_text = 'khoor, zruog'

    c1 = 'iluvw, vroyh wkh sureohp. wkhq, zulwh wkh frgh. - mrkq mrkqvrq'
    c2 = 'zlwkrxw uhtxluhphqwv ru ghvljq, surjudpplqj lv wkh duw ri dgglqj exjv wr dq hpswb whaw iloh. - orxlv vubjohb'
    c3 = 'frpsxwhuv duh jrrg dw iroorzlqj lqvwuxfwlrqv, exw qrw dw uhdglqj brxu plqg. - grqdog nqxwk'
    c4 = 'dozdbv frgh dv li wkh jxb zkr hqgv xs pdlqwdlqlqj brxu frgh zloo eh d ylrohqw svbfkrsdwk zkr nqrzv zkhuh brx olyh. - mrkq zrrgv'

    key = find_key(plain_text, cipher_text)


    print(f'key : {key}')
    print(decrypt(c1, key))
    print(decrypt(c2, key))
    print(decrypt(c3, key))
    print(decrypt(c4, key))