using Plots, JLD, ColorSchemes


gr()


if isempty(ARGS)
    WIDTH=1920
    HEIGHT=1080
    STEPS=500000000
else
    WIDTH,HEIGHT,STEPS=ARGS
end


mutable struct RandomWalker
    position::Array{Int64,1}
    function RandomWalker()

        position=[rand(1:WIDTH) rand(1:HEIGHT)] |> vec
        new(position)
    end
end

mutable struct FixedRandomWalker
    position
    function FixedRandomWalker(pos)
        position=pos
        new(position)
    end
end



mutable struct World
    walkers::Array{RandomWalker}
    map::Array{Int64}
    function World(walkers)
        new([RandomWalker() for i ∈ 1:walkers], zeros(Int64, WIDTH,HEIGHT))
    end
    
    end



function move!(walker::Union{RandomWalker, FixedRandomWalker})
    δ=rand(-1:1,2)
    n_pos = sum(δ + walker.position .∉ [1:WIDTH, 1:HEIGHT]) != 0 ? [rand(1:WIDTH), rand(1:HEIGHT)] : δ + walker.position
    walker.position=n_pos
    n_pos, rand(1:256) 
    end

function step!(world::World)
    for walker ∈ world.walkers
        pos, val = move!(walker)
        world.map[pos...]+=val
    end
end
###------> Main Program <-----###

world=World(2)



for step ∈ 1:STEPS
    step!(world)
end

p=Plots.heatmap(
    world.map, 
    c= :oslo,
    legend=:none,
    border=:none, 
    axis=nothing,
    size=(1920,1080),
    dpi=500,
    levels=1000
    )

rnd_str=rand(1:200)

Plots.savefig(p,"plot_$rnd_str")
save("arr_$rnd_str.jld", "mapa", world.map)