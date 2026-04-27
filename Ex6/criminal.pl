american(west).
enemy(nono,america).
has(nono,m1).
missile(m1).

%Missiles are weapons
weapon(X):-missile(X).

%Enemies of America are hostile
hostile(X):-enemy(X,america).

%West sells missiles to Nono
sells(west,nono,X):-
    missile(X),
    has(nono,X).

%Crime
criminal(X):-
    american(X),
    weapon(Z),
    hostile(Y),
    sells(X,Y,Z).
