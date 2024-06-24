# This Python file uses the following encoding: utf-8
import os,sys
sys.path.append("../Python_less/")
import pytest

from Lesson4 import f,countNsort,topWord,lessLetter


def test_f():
    # Генерация массива определенной длины из элементов массива
    nameList = ['Vasya','Fedor','Sasha']
    assert len(f(nameList,20)) == 20


def test_countNsort():
    # Вычисление повторяющихся элементов
    integer_list = [34,54,34,54,34,54,34,54,34]
    assert countNsort(integer_list) == [(34, 5), (54, 4)]

def test_lessLetter():
    # Выводит первую букву последнего элемента массива
    sortedDict = [('Vasya',44),('Fedor',33),('Sasha',11)]
    lessLetter(sortedDict)
    assert lessLetter(sortedDict) == 'S'

from Lesson5 import MassiveP,CanonicNum,SimpleNum

def test_MassiveP():
    # Simple Num, simple test
    listP = MassiveP()
    if 47 in listP:
        print('Test OK')
    else: print('Test Failed')

def test_2_SimpleNum():
    # Пустой массив если число составное
    assert SimpleNum(50) == []

