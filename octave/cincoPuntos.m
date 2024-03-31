function cincoPuntos(h, x, y)
            disp("x    f(x)   f'(x)")
    for i=1:length(x)
        if or( i == 1, i == 2)
            try
                fprintf("%4.0f   %4.5f   %5.0f\n", x(i), y(i), 1/(12*h)*(-25*y(i) + 48*y(i+1) -36*y(i+2) +16*y(i+3) - 3*y(i+4)))
            catch  
                disp("Dada la cantidad de datos, no se puede calcular la aproximacion\n")
            end
        elseif or( i==length(x), i==length(x)-1)
            try
                fprintf("%4.0f   %4.5f   %5.0f\n", x(i), y(i), -1/(12*h)*(-25*y(i) + 48*y(i-1) -36*y(i-2) +16*y(i-3) - 3*y(i-4)))
            catch
                disp("Dada la cantidad de datos, no se puede calcular la aproximacion\n")
            end
        else
            try
                fprintf("%4.0f   %4.5f   %5.0f\n", x(i), y(i), 1/(12*h)*(y(i-2) -8*y(i-1) +8*y(i+1) - y(i+2)))
            catch
                disp("Dada la cantidad de datos, no se puede calcular la aproximacion\n")
            end
        end
    end
end
