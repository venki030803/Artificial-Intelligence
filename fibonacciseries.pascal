fib(0, 1) :-
    !.
fib(n, f) :-
    fib(1, n, 1, 1, f).

fib(n, n, _, f, f) :-
    !.
fib(n0, n, f0, f1, f) :-
    n1 is n0 + 1,
    f2 is f0 + f1,
    fib(n1, n, f1, f2, f).
