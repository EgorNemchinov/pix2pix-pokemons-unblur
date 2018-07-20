#!/usr/bin/python

import os
from os.path import join, isfile
from shutil import move

train_size = 0.75
test_size = 0.2

dir = './data/pokemons/'
if not os.path.exists(join(dir, 'train')):
    os.mkdir(join(dir, 'train'))
if not os.path.exists(join(dir, 'test')):
    os.mkdir(join(dir, 'test'))
if not os.path.exists(join(dir, 'val')):
    os.mkdir(join(dir, 'val'))

imgs = [f for f in os.listdir(dir) if isfile(join(dir, f)) and
                                      f.endswith('jpg')]

train_size = int(len(imgs)*train_size)
test_size = int(len(imgs)*test_size)

for img in imgs[:train_size]:
    move(join(dir, img), join(dir, 'train/', img))
for img in imgs[train_size:train_size+test_size]:
    move(join(dir, img), join(dir, 'test/', img))
for img in imgs[train_size+test_size:]:
    move(join(dir, img), join(dir, 'val/', img))

