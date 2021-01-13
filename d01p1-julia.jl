f = open("d01p1-input.txt")
data = read(f, String)
close(f)
# map(x->parse(Float64,x),data)
for x in data
	for y in data
		#if parse(Int64,x) + parse(Int64, y) == 2020: print(x,y)
        print(x,y)
        end
    end
end
