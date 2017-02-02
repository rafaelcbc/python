from calc import *

def test_soma():
	assert soma(2,2) == 4
	assert soma(3,4) == 7

def test_multiplicacao():
	assert multiplicacao(3,3) == 9
	assert multiplicacao(2,5) == 10

def test_subtracao():
	assert subtracao(5,2) == 3
	assert subtracao(0,4) == -4

def test_divisao():
	assert divisao(10,2) == 5
	assert divisao(8,4) == 2
