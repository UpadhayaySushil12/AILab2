% Define the goal state
goal([1, 2, 3, 4, 5, 6, 7, 8, 0]).

% Calculate Manhattan distance as the heuristic function
manhattan_distance([], [], 0).
manhattan_distance([H|T1], [G|T2], Distance) :-
    H = 0,
    manhattan_distance(T1, T2, Distance).
manhattan_distance([H|T1], [G|T2], Distance) :-
    H \= 0,
    nth0(Index1, [1,2,3,4,5,6,7,8,0], H), % Goal positions of tiles
    nth0(Index2, [1,2,3,4,5,6,7,8,0], G),
    Row1 is Index1 // 3, Col1 is Index1 mod 3,
    Row2 is Index2 // 3, Col2 is Index2 mod 3,
    AbsRow is abs(Row1 - Row2), AbsCol is abs(Col1 - Col2),
    PartialDistance is AbsRow + AbsCol,
    manhattan_distance(T1, T2, RemainingDistance),
    Distance is PartialDistance + RemainingDistance.

% Move the blank tile (0) in the puzzle
move([0, B, C, D, E, F, G, H, I], [B, 0, C, D, E, F, G, H, I]).  % Blank moves right
move([B, 0, C, D, E, F, G, H, I], [0, B, C, D, E, F, G, H, I]).  % Blank moves left
move([B, C, 0, D, E, F, G, H, I], [B, 0, C, D, E, F, G, H, I]).  % Blank moves up
move([B, C, D, 0, E, F, G, H, I], [B, C, D, E, 0, F, G, H, I]).  % Blank moves down
move([B, C, D, E, 0, F, G, H, I], [B, C, D, E, F, 0, G, H, I]).  % Blank moves right
move([B, C, D, E, F, 0, G, H, I], [B, C, D, E, F, G, 0, H, I]).  % Blank moves left

% A* Search
astar(Start, Path, Cost) :-
    goal(Goal),
    astar_search([node(Start, [], 0, Cost)], [], Path, Goal).

% Base case: Goal state reached
astar_search([node(State, Path, _, Cost)|_], _, FinalPath, State) :-
    reverse([State|Path], FinalPath),
    format('Solution Found with cost ~w: ~w', [Cost, FinalPath]).

% Recursive case: Expand node
astar_search([node(State, Path, G, _)|RestOpen], Closed, FinalPath, Goal) :-
    findall(node(NextState, [State|Path], NewG, F),
            (   move(State, NextState),
                \+ member(NextState, Path),
                \+ member(NextState, Closed),
                NewG is G + 1,
                manhattan_distance(NextState, Goal, H),
                F is NewG + H
            ),
            Successors),
    append(RestOpen, Successors, NewOpen),
    sort(4, @=<, NewOpen, SortedOpen), % Sort open list by F-value
    astar_search(SortedOpen, [State|Closed], FinalPath, Goal).
