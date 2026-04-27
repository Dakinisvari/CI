calculator :-
    repeat,
    nl, write('--- Calculator ---'), nl,
    write('1. Addition'), nl,
    write('2. Subtraction'), nl,
    write('3. Multiplication'), nl,
    write('4. Division'), nl,
    write('5. Modulus'), nl,
    write('6. Exit'), nl,
    write('Enter your choice (followed by a dot): '),
    read(Choice),
    process(Choice),
    Choice == 6, !. % Terminates the repeat loop when choice is 5
process(6) :-
    write('Exiting...'), nl, !.
process(Choice) :-
    member(Choice, [1, 2, 3, 4, 5]),
    write('Enter first number : '), read(N1),
    write('Enter second number : '), read(N2),
    calculate(Choice, N1, N2), !.
process(_) :-
    write('Invalid choice, please try again.'), nl.
calculate(1, N1, N2) :-
    Res is N1 + N2, format('~w + ~w = ~w~n', [N1, N2, Res]).
calculate(2, N1, N2) :-
    Res is N1 - N2, format('~w - ~w = ~w~n', [N1, N2, Res]).
calculate(3, N1, N2) :-
    Res is N1 * N2, format('~w * ~w = ~w~n', [N1, N2, Res]).
calculate(4, N1, N2) :-
    (N2 \= 0 ->
        (Res is N1 / N2, format('~w / ~w = ~w~n', [N1, N2, Res]))
    ;
        write('Error: Division by zero is not allowed.'), nl
    ).
calculate(5, N1, N2) :-
    Res is N1 % N2, format('~w % ~w = ~w~n', [N1, N2, Res]).
