# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:46:10 2019

@author: krystinsteelman
"""

import PokeType as PT
import importlib
from pprint import pprint
from itertools import permutations

importlib.reload(PT)

type_list = PT.TypeList()

type_list2 = ['normal']
type_list3 = []
for i in permutations(type_list,2):
    if list(i) not in type_list3 and list(i[::-1]) not in type_list3:
        type_list3.append(list(i))

def_list_2 = {}
def_list_half = {}
def_list_0 = {}
off_list_2 = {}
off_list_half = {}
off_list_0 = {}
poke_off = {}
poke_def = {}
off_list_2_2 = []
off_list_half_2 = []
off_list_0_2 = []
def_list_2_2 = []
def_list_half_2 = []
def_list_0_2 = []
enum_list = {}

for i,j in enumerate(type_list):
    enum_list[j]=i

for i in type_list:
    poketype = PT.PokeType([i])
    poketype.get_off()
    poketype.get_def()
    poketype.off_list()
    poketype.def_list()
    poke_off[i] = PT.str_weak.get(i)
    poke_off[i]['off'] = poketype.off_list
    poke_def[i] = PT.str_weak.get(i)
    poke_def[i]['def'] = poketype.def_list
    for key,value in poketype.off_list.items():
        if value == 2:
            off_list_2_2.append(enum_list.get(key))
            if key not in off_list_2.keys():
                off_list_2[key] = 1
            else:
                off_list_2[key] = 1+off_list_2.get(key)
        elif value == .5:
            off_list_half_2.append(enum_list.get(key))
            if key not in off_list_half.keys():
                off_list_half[key] = 1
            else:
                off_list_half[key] = 1+off_list_half.get(key)
        elif value == .25:
            off_list_0_2.append(enum_list.get(key))
            if key not in off_list_0.keys():
                off_list_0[key] = 1
            else:
                off_list_0[key] = 1+off_list_0.get(key)
    for key,value in poketype.def_list.items():
        if value == 2:
            def_list_2_2.append(enum_list.get(key))
            if key not in def_list_2.keys():
                def_list_2[key] = 1
            else:
                def_list_2[key] = 1+def_list_2.get(key)
        elif value == .5:
            def_list_half_2.append(enum_list.get(key))
            if key not in def_list_half.keys():
                def_list_half[key] = 1
            else:
                def_list_half[key] = 1+def_list_half.get(key)
        elif value == .25:
            def_list_0_2.append(enum_list.get(key))
            if key not in def_list_0.keys():
                def_list_0[key] = 1
            else:
                def_list_0[key] = 1+def_list_0.get(key)
    
for i in type_list3:
    poketype = PT.PokeType(i)
    poketype.get_off()
    poketype.get_def()
    poketype.off_list()
    poketype.def_list()
    for key,value in poketype.off_list.items():
        if value == 2:
            off_list_2_2.append(enum_list.get(key))
            if key not in off_list_2.keys():
                off_list_2[key] = 1
            else:
                off_list_2[key] = 1+off_list_2.get(key)
        elif value == .5:
            off_list_half_2.append(enum_list.get(key))
            if key not in off_list_half.keys():
                off_list_half[key] = 1
            else:
                off_list_half[key] = 1+off_list_half.get(key)
        elif value == .25:
            off_list_0_2.append(enum_list.get(key))
            if key not in off_list_0.keys():
                off_list_0[key] = 1
            else:
                off_list_0[key] = 1+off_list_0.get(key)
    for key,value in poketype.def_list.items():
        if value == 2:
            def_list_2_2.append(enum_list.get(key))
            if key not in def_list_2.keys():
                def_list_2[key] = 1
            else:
                def_list_2[key] = 1+def_list_2.get(key)
        elif value == .5:
            def_list_half_2.append(enum_list.get(key))
            if key not in def_list_half.keys():
                def_list_half[key] = 1
            else:
                def_list_half[key] = 1+def_list_half.get(key)
        elif value == .25:
            def_list_0_2.append(enum_list.get(key))
            if key not in def_list_0.keys():
                def_list_0[key] = 1
            else:
                def_list_0[key] = 1+def_list_0.get(key)