%O2: ``maximum socialisation''
% Find a 10-week schedule with as few repeated pairs as possible 
group(G) :- groups(G).
group(G-1) :- group(G), G > 1.

student(N-1) :- students(N).
student(S-1) :- student(S), S > 0.

week(W) :- weeks(W).
week(W-1) :- week(W), W > 1.

% Search space: The set of all possible group assignments to all students in each of the weeks
% weeks.
{ student_week_group(P,W,G) : group(G)} = 1 :- student(P), week(W).

% C1: Each group has exactly groupSize students
{ student_week_group(P,W,G): student(P) } = S :- group(G), week(W), students_per_group(S).

% P1 and P2 meet during week W
meets(P1,P2,W) :- student_week_group(P1,W,G), student_week_group(P2,W,G), P1 < P2.
:~ #count { W : meets(P1,P2,W) } > 1, student(P1), student(P2), P1 < P2. [1,P1,P2]
  
#show student_week_group/3.