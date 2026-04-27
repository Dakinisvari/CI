% ===== FACTS =====

% Gender
male(john).
male(tom).
male(jim).
male(bob).
male(fred).
male(scott).
male(jack).
male(rich).
male(mike).
male(harry).

female(mary).
female(carol).
female(alice).
female(linda).
female(valerie).
female(barbara).
female(donna).
female(rachel).
female(jane).
female(cindy).

% ===== SPOUSE =====
spouse(john, mary).
spouse(mary, john).
spouse(tom, alice).
spouse(alice, tom).
spouse(linda, steve).
spouse(steve, linda).
spouse(fred, valerie).
spouse(valerie, fred).
spouse(barbara, scott).
spouse(scott, barbara).
spouse(jack, donna).
spouse(donna, jack).
spouse(rich, rachel).
spouse(rachel, rich).

% ===== PARENTS =====

father(john, carol).
father(john, tom).
father(john, linda).
father(john, jim).
father(jim, bob).
father(tom, barbara).
father(steve, jack).
father(steve, rich).
father(fred, jane).
father(scott, cindy).
father(jack, mike).
father(rich, harry).
father(tom, valerie).

mother(mary, carol).
mother(mary, tom).
mother(mary, linda).
mother(mary, jim).
mother(carol, patty).
mother(alice, barbara).
mother(alice, valerie).
mother(linda, jack).
mother(linda, rich).
mother(valerie, jane).
mother(barbara, cindy).
mother(donna, mike).
mother(rachel, harry).

% ===== RULES =====

% Parent
parent(X, Y) :- father(X, Y).
parent(X, Y) :- mother(X, Y).

sibling(X, Y) :-
    father(F, X), father(F, Y),
    mother(M, X), mother(M, Y),
    X \= Y.

% Brother
brother(X, Y) :-
    sibling(X, Y),
    male(X).

% Sister
sister(X, Y) :-
    sibling(X, Y),
    female(X).

% Grandparent
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

grandfather(X, Y) :-
    grandparent(X, Y),
    male(X).

grandmother(X, Y) :-
    grandparent(X, Y),
    female(X).

% Grandchildren
grandson(X, Y) :-
    grandparent(Y, X),
    male(X).

granddaughter(X, Y) :-
    grandparent(Y, X),
    female(X).

% Cousin
cousin(X, Y) :-
    parent(P1, X),
    parent(P2, Y),
    sibling(P1, P2),
    X \= Y.

% Uncle
uncle(X, Y) :-
    brother(X, P),
    parent(P, Y).

% Aunt
aunt(X, Y) :-
    sister(X, P),
    parent(P, Y).

% Nephew
nephew(X, Y) :-
    male(X),
    parent(P, X),
    sibling(P, Y).

% Niece
niece(X, Y) :-
    female(X),
    parent(P, X),
    sibling(P, Y).
