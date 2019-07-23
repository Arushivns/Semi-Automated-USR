# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from isc_parser import Parser
import csv
parser = Parser(lang='hin')
text = "लड़के ने दो नयी किताबें  खरीदी थी|"
text = text.split()
print(text)

tree = parser.parse(text)
print('\n'.join(['\t'.join(node) for node in tree]).encode("utf-8"))
