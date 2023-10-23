drop table if exists table;
create table if not exists table(A int,
B int,C int,
D int,E int,
F int,G int,
H int,
n int);

WITH RECURSIVE table(A,B,C,D,E,F,G,H,n) AS (VALUES (1,1,1,1,1,1,1,1,1)
  UNION ALL  SELECT mod(n/1,8)+1,mod(n/8,8)+1,mod(n/64,8)+1,mod(n/512,8)+1,mod(n/4096,8)+1,mod(n/32768,8)+1,mod(n/262144,8)+1,mod(n/2097152,8)+1,n+1 from table WHERE table.n < 16777216
)select A,B,C,D,E,F,G,H from table
WHERE A NOT IN (B, B-1, B+1, C, C-2, C+2, D, D-3, D+3, E, E-4, E+4, F, F-5, F+5, G, G-6, G+6, H, H-7, H+7) and
      B NOT IN (C, C-1, C+1, D, D-2, D+2, E, E-3, E+3, F, F-4, F+4, G, G-5, G+5, H, H-6, H+6) and
      C NOT IN (D, D-1, D+1, E, E-2, E+2, F, F-3, F+3, G, G-4, G+4, H, H-5, H+5) and
      D NOT IN (E, E-1, E+1, F, F-2, F+2, G, G-3, G+3, H, H-4, H+4) and
      E NOT IN (F, F-1, F+1, G, G-2, G+2, H, H-3, H+3) and
      F NOT IN (G, G-1, G+1, H, H-2, H+2) and
      G NOT IN (H, H-1, H+1)