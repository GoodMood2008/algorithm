-module(erl_121).
-compile(export_all).



maxProfit([]) -> 0;
maxProfit([H|T]) -> maxProf(T, H, 0).

maxProf([], _, MaxProf) -> MaxProf;
maxProf([H|T], MinPri, MaxProf) ->
    %io:format("~p ~p ~p\n", [MinPri, MaxProf, lists:max([MaxProf, H - MinPri])]),
    if 
        H < MinPri -> maxProf(T, H, MaxProf);
        true -> maxProf(T, MinPri, lists:max([MaxProf, H - MinPri]))
    end.
%maxProf([H|T], MinPri, MaxProf) when H < MinPri -> maxProf(T, H, MaxProf);
%maxProf([H|T], MinPri, MaxProf) -> maxProf(T, H, lists:max([MaxProf, H - MinPri])).



test() -> 
    5 = maxProfit([7,1,5,3,6,4]).