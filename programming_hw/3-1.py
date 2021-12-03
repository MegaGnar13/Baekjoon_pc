from urllib.request import urlopen
import re


class Dictionary:
    def __init__(self):
        self.my_dict = {}
        with open("mydictionary.txt","rt") as f:
            file_content = f.read().splitlines()
        for i in file_content:
            k=i.split(":")
            self.my_dict[k[0]]=k[1]

        return

    def find(self, word, ip="10.150.4.67"):
        with urlopen("http://"+ip+"/dict.html?query="+word) as u:
            dic_word=u.read().decode("utf-8")
        result = re.findall("<tr><td>Definition: </td><td>([a-z,A-z,;,., ]+)",dic_word)
        return result[0]

    def add_dictionary(self, document):
        char=",."
        for i in range(len(char)):
            document = document.replace(char[i],"")
        words=document.split(" ")
        words=list(set(words))
        for j in words:
            meaning = self.find(j)
            self.my_dict[j] = meaning

        return

    def save_dictionary(self):
        with open("mydictionary.txt", "wt") as f:
            for word in self.my_dict:
                print(word+":"+self.my_dict[word],file=f)
        return

    def show_dictionary(self):
        result=[]
        for word in self.my_dict:
            result.append(word)
        result.sort()
        return result


if __name__ == '__main__':
    my = Dictionary()
    print(my.find('problem'))
    print(my.show_dictionary())
    my.add_dictionary("first, solve the problem. then, write the code.")
    print(my.show_dictionary())
    my.save_dictionary()