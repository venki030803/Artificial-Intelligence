 predicates
        factorial(integer, real)
        go
        
    clauses
        go if
        write("Enter a positive integer number:"),
        readint(N),
        factorial(N,Result),
        write("Factorial of", N, "is=", Result).
        factorial(0, 1)
        factorial(N, Result) if N>0,
                        N1=N-1,
                        factorial(N1, Res),
                        Result=N*Res.
