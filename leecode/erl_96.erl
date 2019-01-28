-module(erl_96).
-compile(export_all).


numTrees(N) when N < 2 -> N;
numTrees(N) -> getNumTrees(N).

getNumTrees(0) -> 1;
getNumTrees(1) -> 1;
getNumTrees(N) -> tempNumTree(N, N, 0).

tempNumTree(0, _, R) -> R;
tempNumTree(M, N, R) ->
    tempNumTree(M - 1, N, R + getNumTrees(M - 1) * getNumTrees(N - M)).


numTrees1(N) when N < 2 -> N;
numTrees1(N) -> dpNumTree(1, N, [1, 1]).

dpNumTree(N, N, L) -> lists:nth(erlang:length(L), L);
dpNumTree(M, N, L) -> 
    R = lists:sum(lists:zipwith(fun(X, Y) -> X * Y end, L, lists:reverse(L))),
    dpNumTree(M + 1, N, L ++ [R]).


test() -> 
    5 = numTrees(3).