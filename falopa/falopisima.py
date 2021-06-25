#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 20:23:07 2021

@author: gonik
"""
import numpy as np
import matplotlib.pyplot as plt 
class World:
    def __init__(self):
        self.map=np.zeros((2000,2000))



class Walker:
    def __init__(self, world: World) -> None:
        self.location = np.random.randint(0,world.map.shape[1], size = 2)
    def walk(self, world) -> World:
        self.location += np.random.choice([-1,1], 2)
        try:
            world.map[tuple(self.location)] = 1
        except IndexError:
            nloc = tuple(np.random.randint(0,world.map.shape[1], size = 2))
            world.map[nloc] = 1
        return world
        


def main():
    world = World()
    walkers = [Walker(world) for _ in range(3)]
    for _ in range (400000):
        for walker in walkers:
            world = walker.walk(world)
    return world


def plot(world):
    fig, ax = plt.subplots(1,1, figsize = (20,20))
    ax.imshow(world.map, cmap = 'viridis' )
    plt.axis('off')
    plt.savefig('falopita.png')    
    


if __name__=="__main__":
    j=main()
    plot(j)
    #plt.imshow(j.map)