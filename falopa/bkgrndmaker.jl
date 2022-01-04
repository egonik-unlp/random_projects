#!/usr/bin/env julia 


using Plots, JLD, ColorSchemes, ArgParse


gr()



function parse_commandline()
    s = ArgParseSettings()
    @add_arg_table s begin
        "--vres"
        help = "vertical resolution of the generated map"
        arg_type = Int
        default = 1080
        "--hres"
        help = "horizontal resolution of the generated map"
        arg_type = Int
        default = 1920
        "--walkers", "-w"
        help="Sets the number of walkers"
        arg_type=Int
        default=10
        "--steps","-s"
        help = "number of steps taken by the walkers"
        arg_type = Int
        default = 1_000_000
        "--cmap"
        help = "Select cmap for the generated heatmap. A list is available at https://docs.juliaplots.org/latest/generated/colorschemes/"
        arg_type=Symbol
        default=:oslo


    end
    parse_args(s)    
end



function main()
    args=parse_commandline()
    global HEIGHT  = args["vres"]
    global WIDTH = args["hres"]
    global STEPS = args["steps"]
    global CMAP = args["cmap"] |> Symbol
    world=World(args["walkers"])
    for step ∈ 1:STEPS
        step!(world)
    end 
    @info """Running background generator with $WIDTH x $HEIGHT resolution, $STEPS steps and $(length(world.walkers)) walkers"""
    world

end


mutable struct RandomWalker
    position::Array{Int64,1}
    function RandomWalker()

        position=[rand(1:WIDTH) rand(1:HEIGHT)] |> vec
        new(position)
    end
end

mutable struct FixedRandomWalker ## Para debuggear
    position
    function FixedRandomWalker(pos)
        position=pos
        new(position)
    end
end



mutable struct World
    walkers::Array{Union{RandomWalker, FixedRandomWalker}}
    map::Array{Int64}
    function World(walkers)
        new([RandomWalker() for i ∈ 1:walkers], zeros(Int64, WIDTH,HEIGHT))
    end

    function World(positions::Array)
        new([FixedRandomWalker(pos) for pos in positions])
    end

    end
    



function move!(walker::Union{RandomWalker, FixedRandomWalker})
    δ=rand(-1:1,2)
    n_pos = sum(δ + walker.position .∉ [1:WIDTH, 1:HEIGHT]) != 0 ? [rand(1:WIDTH), rand(1:HEIGHT)] : δ + walker.position
    walker.position=n_pos 
    end

function step!(world::World)
    for walker ∈ world.walkers
        move!(walker)
        world.map[walker.position...] += 1
    end
end


###------> Main Program <-----###


world=main()



p=Plots.heatmap(
    world.map, 
    c= CMAP,
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

@info "Plot saved in ./plot_$rnd_str.png, Array saved in ./arr_$rnd_str.jld"