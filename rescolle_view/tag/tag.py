# coding: utf-8

from django.conf import settings
import MeCab


class Tokenizer:

    def __init__(self):
        self.keywords = []
        self.delimiter = ','
        self.tagger = MeCab.Tagger('-d {}'.format(settings.MECAB_DICT_DIR))

    def get_tokens(self, text):
        self.tagger.parse('')
        node = self.tagger.parseToNode(text)
        tokens = []
        while node:
            if node.feature.split(self.delimiter)[0] not in ('助詞', '記号', '接頭詞') and node.surface != '':
                tokens.append({'surface': node.surface, 'part_of_speech': node.feature})
            node = node.next
        return tokens

