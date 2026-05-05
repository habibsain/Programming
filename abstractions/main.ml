(*sum a list*)
let rec sum (lst : int list) : int = 
  match lst with
  |[] -> 0
  |hd :: tl -> hd + sum tl;;


(*multiply a list*)
let rec prod (lst : int list) : int =
match lst with
|[] -> 1
|hd :: tl -> hd * prod tl;;
(*val prod : int list -> int = <fun>*)

(*append list to list*)
let rec append (x : int list) (y : int list): int list =
match x with
|[] -> y
|hd :: tl -> hd :: append tl y;;

(*Initial Concat strings*)

(*let rec concat (delimit : string) (lst : string list) : string =
match lst with 
|[] -> ""
|hd :: tl -> hd ^ delimit ^ concat delimit tl;;*)
(*This adds delimitter after the last element as well*)

(*Final concat function*)
let rec concat (delimit : string) (lst : string list) : string =
match lst with 
|[] -> "" (*This part is not required for recursion as call stops with single element list
But leaving this line results into error. As this is required to consider all possible cases of lists*)
|[hd] -> hd
|hd :: tl -> hd ^ delimit ^ concat delimit tl;;

