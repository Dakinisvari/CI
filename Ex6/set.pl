set :-
    repeat,
    nl, write('--- Set Operations Menu ---'), nl,
    write('1. Is Member?'), nl,
    write('2. Union'), nl,
    write('3. Intersection'), nl,
    write('4. Is Subset?'), nl,
    write('5. Difference (A - B)'), nl,
    write('6. Cardinality (Size)'), nl,
    write('7. Is Equivalent?'), nl,
    write('8. Exit'), nl,
    write('Choice (with dot): '), read(Choice),
    process(Choice),
    Choice == 8, !.
process(8) :- write('Exiting...'), nl, !.
process(Choice) :-
    member(Choice, [2, 3, 4, 5, 7]),
    write('Enter Set A : '), read(A),
    write('Enter Set B : '), read(B),
    do_op(Choice, A, B), !.
process(1) :-
    write('Enter Set: '), read(S),
    write('Enter Element: '), read(E),
    (member(E, S) -> write('Yes, it is a member.'); write('No, it is not.')), nl, !.
process(6) :-
    write('Enter Set: '), read(S),
    length(S, L), format('Cardinality is: ~w~n', [L]), !.
process(_) :- write('Invalid choice.'), nl.
do_op(2, A, B) :- union(A, B, R), format('Union: ~w~n', [R]).
do_op(3, A, B) :- intersection(A, B, R), format('Intersection: ~w~n', [R]).
do_op(4, A, B) :- (subset(A, B) -> write('A is a subset of B.'); write('A is NOT a subset.')), nl.
do_op(5, A, B) :- subtract(A, B, R), format('Difference: ~w~n', [R]).
do_op(7, A, B) :-
    (subset(A, B), subset(B, A) -> write('Sets are equivalent.'); write('Sets are NOT equivalent.')), nl.
