%O2: ``maximum socialisation''
% Find a 10-lunch schedule with as few repeated pairs as possible 
group(G-1) :- groups(G).
group(G-1) :- group(G), G > 0.

student(N-1) :- students(N).
student(S-1) :- student(S), S > 0.

lunch(W-1) :- lunches(W).
lunch(W-1) :- lunch(W), W > 0.

% Search space: The set of all possible group assignments to all students in each of the lunches
% lunches.
{ student_lunch_group(P,W,G) : group(G)} = 1 :- student(P), lunch(W).

% C1: Each group has exactly groupSize students
{ student_lunch_group(P,W,G): student(P) } = S :- group(G), lunch(W), students_per_group(S).

% P1 and P2 meet during lunch W
meets(P1,P2,W) :- student_lunch_group(P1,W,G), student_lunch_group(P2,W,G), P1 < P2.
%:~ C=#count { W : meets(P1,P2,W) } > 1, student(P1), student(P2), P1 < P2. [C*C,P1,P2]
:~ C=#count { W : meets(P1,P2,W) }>1, student(P1), student(P2), P1 < P2. [1@C,P1,P2]
#show student_lunch_group/3.