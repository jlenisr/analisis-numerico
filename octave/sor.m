function p = sor(A, b, x_0, iter, tol)
  D = diag(diag(A));
  fprintf("D = \n")
  disp(D)
  L = D- tril(A);
  fprintf("L = \n")
  disp(L)
  U = D - triu(A);
  fprintf("U = \n")
  disp(U)
  fprintf("w más optimo: ")
  w = optimezeW(L, U, D);
  disp(w)
  for i=1:iter
    x = inv(D-w*L)*((1-w)*D + w*U)*x_0 + w*inv(D-w*L)*b
    if A*x - b == zeros(length(A), 1) | infNorm(x - x_0)/infNorm(x) < tol  
      break;
    end
    x_0 = x;
  end
  
end

function w = optimezeW(L,U,D)
  Tj = inv(D)*(L+U);
  Tjratio = max(abs(eig(Tj)));
  w = 2/(sqrt(1-(Tjratio)^2) + 1);
end

function n = infNorm(A)
  n = max(sum(abs(A)));
end
