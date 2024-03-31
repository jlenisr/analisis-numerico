function tresPuntos(h, x, y)
            disp("    x       f(x)       f'(x)")
    for i=1:length(x)
        if i==1
            fprintf("%4.0f    %4.5f     %5.0f\n", x(i), y(i), 1/(2*h)*(4*y(i+1)-3*y(i)-y(i+2)))
        elseif i == length(x)
            fprintf("%4.0f    %4.5f     %5.0f\n", x(i), y(i), -1/(2*h)*(4*y(i-1)-3*y(i)-y(i-2)))
        else
            fprintf("%4.0f    %4.5f     %5.0f\n", x(i), y(i), 1/(2*h)*(y(i+1)-y(i-1)))
        end
    end
end