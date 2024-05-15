function [x,it,t,r_h] = jacobi (A,b,x0,maxit,tol)
 tic();
 it=0;
 x=x0;
 n=length(A(:,1));
 while(it<maxit)
 for i=1:n
 x(i)=(b(i)-A(i,1:i-1)*x0(1:i-1)-A(i,i+1:n)*x0(i+1:n))/A(i,i);
 endfor
 r_h(it+1)=norm(x-x0,Inf);
 if (r_h(it+1)<tol)
 break;
 endif
 x0=x;
 it=it+1;
 endwhile
 t=toc();
endfunction