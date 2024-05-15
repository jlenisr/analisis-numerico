function p = gradient(A, b, x_0, v_1, iter, tol)
  for i = 1:iter
    t = innerProduct(v_1, b-A*x_0)/innerProduct(v_1, A*v_1);
    x = x_0 + t*v_1
    if A*x == b | infNorm(x-x_0)/infNorm(x) < tol
      break;
    end
    x_0 = x;
    v_1 = b - A*x;
  end

end

function ip = innerProduct(x,y)
  ip = x' * y;
end

function n = infNorm(A)
  n = max(sum(abs(A)));
end
