RealTriangles = 0
%x = [3 4 10; 1 1 3]
%y = []
for j =1:3
    for i = 1:3:length(x)
    
        set = [x(i,j), x(i+1,j), x(i+2,j)]
        if ((set(1) + set(2) > set(3)) && (set(1) + set(3) > set(2)) && (set(2) + set(3) > set(1)))
            RealTriangles = RealTriangles +1;
        end
    end

end

    
RealTriangles
