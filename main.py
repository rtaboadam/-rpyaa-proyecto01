#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Universidad Nacional Autónoma de México
# Facultad de Ciencias
# Reconocimiento de Patrones y Aprendizaje Automatizado

import csv
import json

TRAIN_SET    = 'resources/shuttle.trn'
TRAIN_LENGTH = 43500
TEST_SET     = 'resources/shuttle.tst'
TEST_LENGTH  = 14500

def do_with_data(pathfile,callback):
	"""\
	Función para que lea parte de los datos y ejecute
	un callback con ellos
	"""
	with open(pathfile,'rb') as csvfile:
		datareader = csv.reader(csvfile,delimiter=' ')
		return callback(datareader)

def main():
	print "Hello, world!!!"

if __name__ == '__main__':
	main()