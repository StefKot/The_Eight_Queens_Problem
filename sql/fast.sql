with numbered_rows as (
    select ROW_NUMBER() over (order by a) as rn
    from generate_series(1, 8) as a
),
     all_combinations AS (
         select a, b, c, d, e, f, g, h.rn as h
         from (select  a, b, c, d, e, f, g.rn as g
               from (select a, b, c, d, e, f.rn as f
                     from (select a, b, c, d, e.rn as e
                           from (select a, b, c, d.rn as d
                                 from (select a, b, c.rn as c
                                       from (select a.rn as a, b.rn as b
                                             from numbered_rows a cross join numbered_rows b
                                             where a.rn not in (b.rn - 1, b.rn, b.rn + 1) ) ab cross join numbered_rows c
                                        where ab.a not in (c.rn, c.rn + 2, c.rn - 2)
                                          and ab.b not in (c.rn, c.rn + 1, c.rn - 1) ) abc cross join numbered_rows d
                                 where abc.a not in (d.rn, d.rn + 3, d.rn - 3)
                                   and abc.b not in (d.rn, d.rn + 2, d.rn - 2)
                                   and abc.c not in (d.rn, d.rn + 1, d.rn - 1) ) abcd cross join numbered_rows e
                           where abcd.a not in (e.rn, e.rn + 4, e.rn - 4)
                             and abcd.b not in (e.rn, e.rn + 3, e.rn - 3)
                             and abcd.c not in (e.rn, e.rn + 2, e.rn - 2)
                             and abcd.d not in (e.rn, e.rn + 1, e.rn - 1)) abcde cross join numbered_rows f
                     where abcde.a not in (f.rn, f.rn + 5, f.rn - 5)
                       and abcde.b not in (f.rn, f.rn + 4, f.rn - 4)
                       and abcde.c not in (f.rn, f.rn + 3, f.rn - 3)
                       and abcde.d not in (f.rn, f.rn + 2, f.rn - 2)
                       and abcde.e not in (f.rn, f.rn + 1, f.rn - 1)) abcdef cross join numbered_rows g
                where abcdef.a not in (g.rn, g.rn + 6, g.rn - 6)
                 and abcdef.b not in (g.rn, g.rn + 5, g.rn - 5)
                 and abcdef.c not in (g.rn, g.rn + 4, g.rn - 4)
                 and abcdef.d not in (g.rn, g.rn + 3, g.rn - 3)
                 and abcdef.e not in (g.rn, g.rn + 2, g.rn - 2)
                 and abcdef.f not in (g.rn, g.rn + 1, g.rn - 1)) abcdefg cross join numbered_rows h
          where abcdefg.a not in (h.rn, h.rn + 7, h.rn - 7)
           and abcdefg.b not in (h.rn, h.rn + 6, h.rn - 6)
           and abcdefg.c not in (h.rn, h.rn + 5, h.rn - 5)
           and abcdefg.d not in (h.rn, h.rn + 4, h.rn - 4)
           and abcdefg.e not in (h.rn, h.rn + 3, h.rn - 3)
           and abcdefg.f not in (h.rn, h.rn + 2, h.rn - 2)
           and abcdefg.g not in (h.rn, h.rn + 1, h.rn - 1)
     )

select *
from all_combinations;