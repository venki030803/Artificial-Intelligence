printlist([]).
printlist([X|List]) :- write(X),nl, printlist(List).
