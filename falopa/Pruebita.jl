### A Pluto.jl notebook ###
# v0.14.8

using Markdown
using InteractiveUtils

# ╔═╡ ea94b04d-6754-4371-ab39-7a72578e3db0
using PlutoUI

# ╔═╡ 239a63e5-eafb-4474-9449-4c52dd72ae97
using Plots

# ╔═╡ bb242dbd-d741-4ae2-a89d-91a69a12fa37
md"""
# Entrega 1, curso Julia


Debido a que no encontré un ejemplo asociado a mi tema de investigación (no trabajo en bioinformática) decidí recrear [este](https://github.com/egonik-unlp/random_projects/blob/master/falopa/falopisima.py) script para generar imagenes para fondos de pantalla y similares mediante random walkers, originalmente escrito en Python.


"""


# ╔═╡ 412217b0-d887-11eb-28dd-e18225384c9b
struct World
	shape::NamedTuple
	map::Array
	function World(shape::NamedTuple)
		new(shape,zeros(shape.x, shape.y))
	end
end


# ╔═╡ ca4cb1c0-d2b1-4c35-98d2-824b1350705d
mutable struct Walker
	world::World
	position::Array
	function Walker(world::World)
		new(world,rand(1:world.shape.x,2))
	end
end

# ╔═╡ a4c06573-ec86-4fa3-bca0-031c54620185
function new_position(walker::Walker, world::World)
	walker.position+=rand(-1:1, 2)
	try
		world.map[walker.position...] += 1
	catch y
		if isa(y, BoundsError)
			walker= Walker(world)
			world.map[walker.position...] += 1
		end
	end
end
	

# ╔═╡ 84ed7486-4969-41a7-8d76-6b34cec04e4b
function genesis(shape::NamedTuple,n_walkers::Int, steps) 
	p=0
	world = World(shape)
	walkers = [Walker(world) for n in 1:n_walkers]
	for step in 1:steps
		for walker in walkers
			new_position(walker,world)
		end
	end
	world
end

# ╔═╡ 4b5903ae-d9ce-4a5a-8613-71d55eee03bc
w = genesis((x=1000,y=1000),10,1000000)

# ╔═╡ 2e7fe31e-c8bd-451e-b747-8967cfd4d818
heatmap(w.map, legend=:none, axis=nothing, dpi=300, size=(1920,1080), fmt=:png)

# ╔═╡ 8c61665f-a834-4b58-b7a7-0cab2d28910d
savefig("scrsvr.png") 

# ╔═╡ Cell order:
# ╟─bb242dbd-d741-4ae2-a89d-91a69a12fa37
# ╠═ea94b04d-6754-4371-ab39-7a72578e3db0
# ╠═239a63e5-eafb-4474-9449-4c52dd72ae97
# ╠═ca4cb1c0-d2b1-4c35-98d2-824b1350705d
# ╠═412217b0-d887-11eb-28dd-e18225384c9b
# ╠═84ed7486-4969-41a7-8d76-6b34cec04e4b
# ╠═a4c06573-ec86-4fa3-bca0-031c54620185
# ╠═4b5903ae-d9ce-4a5a-8613-71d55eee03bc
# ╠═2e7fe31e-c8bd-451e-b747-8967cfd4d818
# ╠═8c61665f-a834-4b58-b7a7-0cab2d28910d
