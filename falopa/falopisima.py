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
        self.map=np.zeros((1080,1920))



class Walker:
    def __init__(self, world: World) -> None:
        self.location = np.random.randint(0,world.map.shape[0], size = 2)
    def walk(self, world) -> World:
        self.location += np.random.choice([-1,0,1], 2)
        try:
            world.map[tuple(self.location)] += np.random.randint(0,100)
        except IndexError:
            nloc = tuple(np.random.randint(0,world.map.shape[0], size = 2))
            world.map[nloc] += np.random.randint(100)
        return world
        


def main():
    world = World()
    walkers = [Walker(world) for _ in range(3)]
    for _ in range (2000000):
        for walker in walkers:
            world = walker.walk(world)
    np.savetxt('random_map_{}.txt'.format(np.random.randint(0,1000)), world.map)
    return world




def plot(world):
    fig, ax = plt.subplots(1,1, figsize = (16,9), dpi=600)
    ax.imshow(world.map, cmap = 'plasma')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('falopita_{}.png'.format(np.random.randint(2000)))    
    


if __name__=="__main__":
    j=main()
    plot(j)
    #plt.imshow(j.map)