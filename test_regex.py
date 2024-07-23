
import re

text = """
# Your large file content goes here
Let's evaluate the transcript line by line according to the Index of Productive Syntax.

1. **look it .**  
   - N1: 1 (look)
   - V1: 1 (look)

2. **friends around .**  
   - N1: 1 (friends)

3. **I f(r)ien(d)s around .**  
   - N2: 1 (I)
   - N1: 1 (friends)

4. **three .**  
   - N1: 1 (three)

5. **fine .**  
   - N1: 1 (fine)

6. **he don't wanna .**  
   - N2: 1 (he)
   - V3: 1 (wanna)

7. **lake yyy .**  
   - N1: 1 (lake)

8. **yep (.) he's on tv .**  
   - N2: 1 (he)
   - V6: 1 (he's)

9. **he &-um (.) he eat a carrot .**  
   - N2: 1 (he)
   - V1: 1 (eat)
   - N5: 1 (a carrot)

10. **yep .**  
    - N1: 1 (yep)

11. **I like carrots .**  
    - N2: 1 (I)
    - V1: 1 (like)
    - N7: 1 (carrots)

12. **here's Bugs .**  
    - V6: 1 (here's)
    - N1: 1 (Bugs)

13. **right there .**  
    - N1: 1 (there)

14. **Mi(ll)isan(d)y .**  
    - N1: 1 (Mi(ll)isan(d)y)

15. **here's a mirror .**  
    - V6: 1 (here's)
    - N5: 1 (a mirror)

16. **I go(t) two mirrors .**  
    - N2: 1 (I)
    - V1: 1 (go(t))
    - N5: 1 (two mirrors)

17. **I bought this fo(r) my birthday .**  
    - N2: 1 (I)
    - V12: 1 (bought)
    - N5: 1 (my birthday)

18. **me .**  
    - N2: 1 (me)

19. **(o)kay .**  
    - N1: 1 (okay)

20. **in this mirror (.) oh .**  
    - N5: 1 (this mirror)

21. **<on the> [//] <on &-uh> [//] on the (.) other mirror .**  
    - N5: 1 (the other mirror)

22. **&-uh (.) wi(ll) we ha(ve) one ?**  
    - N2: 1 (we)
    - V9: 1 (wi(ll) have)
    - Q1: 1 (question mark)

23. **Ann_Marie .**  
    - N1: 1 (Ann_Marie)

24. **I like my cousin .**  
    - N2: 1 (I)
    - V1: 1 (like)
    - N5: 1 (my cousin)

25. **(be)cause we're friends .**  
    - V6: 1 (we're)
    - N1: 1 (friends)

26. **five .**  
    - N1: 1 (five)

27. **six (.) seven (.) eight . [+ bch]**  
    - N1: 1 (six)
    - N1: 1 (seven)
    - N1: 1 (eight)

28. **I count .**  
    - N2: 1 (I)
    - V1: 1 (count)

29. **two .**  
    - N1: 1 (two)

30. **oh .**  
    - N1: 1 (oh)

31. **get a spanking .**  
    - V1: 1 (get)
    - N5: 1 (a spanking)

32. **you break it you ge(t) a spanking .**  
    - N2: 1 (you)
    - V1: 1 (break)
    - V1: 1 (ge(t))
    - N5: 1 (a spanking)

33. **you go (.) dancin(g)_school .**  
    - N2: 1 (you)
    - V1: 1 (go)
    - N1: 1 (dancin(g)_school)

34. **you(rs) (.) you .**  
    - N2: 1 (you)

35. **nope .**  
    - N1: 1 (nope)

36. **I show (.) you .**  
    - N2: 1 (I)
    - V1: 1 (show)
    - N2: 1 (you)

37. **he(r)e's Mi(ll)isan(d)y .**  
    - V6: 1 (he(r)e's)
    - N1: 1 (Mi(ll)isan(d)y)

38. **I make him hop .**  
    - N2: 1 (I)
    - V1: 1 (make)
    - N2: 1 (him)
    - V1: 1 (hop)

39. **Mi(ll)isan(d)y fa(ll) down .**  
    - N1: 1 (Mi(ll)isan(d)y)
    - V1: 1 (fa(ll))

40. **hop [/] (.) hop .**  
    - V1: 1 (hop)

41. **I wanna yyy yyy .**  
    - N2: 1 (I)
    - V3: 1 (wanna)

42. **I wan(t) a icecweam [: ice_cream] .**  
    - N2: 1 (I)
    - V1: 1 (wan(t))
    - N5: 1 (a ice_cream)

43. **<this &~ha> [//] xxx wha(t) I want .**  
    - N2: 1 (I)
    - V1: 1 (want)

44. **not <tha(t) ice_(cr)eam> [/] (.) tha(t) ice_(cr)eam .**  
    - N1: 1 (ice_(cr)eam)
    - N1: 1 (ice_(cr)eam)
    - Q3: 1 (not)

45. **this vanilla .**  
    - N5: 1 (this vanilla)

46. **tha(t)'s choco(late)_chip .**  
    - V6: 1 (tha(t)'s)
    - N1: 1 (choco(late)_chip)

47. **o:h (.) two nibbles .**  
    - N1: 1 (two nibbles)

48. **two nibbles .**  
    - N1: 1 (two nibbles)

49. **you [/] you ge(t) some nibbles at your house ?**  
    - N2: 1 (you)
    - V1: 1 (ge(t))
    - N5: 1 (some nibbles)
    - Q1: 1 (question mark)

50. **you [/] you ge(t) two ice_creams ?**  
    - N2: 1 (you)
    - V1: 1 (ge(t))
    - N5: 1 (two ice_creams)
    - Q1: 1 (question mark)

51. **xxx (.) I wan(t) si(t) down .**  
    - N2: 1 (I)
    - V1: 1 (wan(t))
    - V1: 1 (si(t))

52. **&-um (.) vanilla .**  
    - N1: 1 (vanilla)

53. **I like a (.) these .**  
    - N2: 1 (I)
    - V1: 1 (like)
    - N5: 1 (these)

54. **&-um (.) chip .**  
    - N1: 1 (chip)

55. **an(d) this &-uh ice (c)ream .**  
    - N5: 1 (this ice (c)ream)

56. **yyy yyy (.) I ge(t) ice_(c)ream on it .**  
    - N2: 1 (I)
    - V1: 1 (ge(t))
    - N5: 1 (ice_(c)ream)

57. **huh .**  
    - N1: 1 (huh)

58. **&-um (.) tuna was .**  
    - N1: 1 (tuna)
    - V4: 1 (was)

59. **too .**  
    - N1: 1 (too)

60. **mine .**  
    - N2: 1 (mine)

61. **ice_(cr)eam .**  
    - N1: 1 (ice_(cr)eam)

62. **its ice_cream .**  
    - N2: 1 (its)
    - N1: 1 (ice_cream)

63. **its not cold (.) but it is .**  
    - N2: 1 (it)
    - V3: 1 (is)
    - Q3: 1 (not)

64. **&-um (.) &-uh (.) hey .**  
    - N1: 1 (hey)

65. **write .**  
    - V1: 1 (write)

66. **blue .**  
    - N1: 1 (blue)

67. **I wan(t) a piece o(f) paper .**  
    - N2: 1 (I)
    - V1: 1 (wan(t))
    - N5: 1 (a piece of paper)

68. **the(r)e .**  
    - N1: 1 (the(r)e)

69. **when .**  
    - N1: 1 (when)

70. **huh ?**  
    - Q1: 1 (question mark)

71. **and I came (.) here .**  
    - S5: 1 (and)
    - N2: 1 (I)
    - V12: 1 (came)

72. **I dance .**  
    - N2: 1 (I)
    - V1: 1 (dance)

73. **Sleepin(g)z_Beauty .**  
    - N1: 1 (Sleepin(g)z_Beauty)

74. **I do all by my self .**  
    - N2: 1 (I)
    - V1: 1 (do)
    - N5: 1 (my self)

75. **jazz .**  
    - N1: 1 (jazz)

76. **I can't .**  
    - N2: 1 (I)
    - Q3: 1 (can't)

77. **he can't .**  
    - N2: 1 (he)
    - Q3: 1 (can't)

78. **(be)cause (.) he won't talk .**  
    - V6: 1 (he won't)
    - N1: 1 (talk)

79. **&-uh no uhuh .**  
    - N1: 1 (no)

80. **xxx &-um (.) &-uh Yuna .**  
    - N1: 1 (Yuna)

81. **no <&~e> [//] Yuna .**  
    - N1: 1 (Yuna)

82. **Petunia .**  
    - N1: 1 (Petunia)

83. **hm: .**  
    - N1: 1 (hm:)

84. **mhm .**  
    - N1: 1 (mhm)

85. **I go(t) a lot &-uh pencils .**  
    - N2: 1 (I)
    - V1: 1 (go(t))
    - N5: 1 (a lot of pencils)

86. **<I go(t)> [/] (.) I go(t) a pen .**  
    - N2: 1 (I)
    - V1: 1 (go(t))
    - N5: 1 (a pen)

87. **what ?**  
    - Q1: 1 (question mark)

88. **yeah .**  
    - N1: 1 (yeah)

89. **you find it ?**  
    - N2: 1 (you)
    - V1: 1 (find)
    - Q1: 1 (question mark)

90. **here [/] here .**  
    - N1: 1 (here)

91. **this re(d) pen .**  
    - N5: 1 (this red pen)

92. **here (.) you use my pen now .**  
    - N2: 1 (you)
    - V1: 1 (use)
    - N5: 1 (my pen)

93. **it's blue .**  
    - V6: 1 (it's)
    - N1: 1 (blue)

94. **hey (.) hee [/] hee .**  
    - N1: 1 (hey)

95. **it's not yours (.) it's mine .**  
    - V6: 1 (it's)
    - Q3: 1 (not)
    - N2: 1 (mine)

96. **he can't w(r)ite .**  
    - N2: 1 (he)
    - Q3: 1 (can't)
    - V1: 1 (w(r)ite)

97. **he scribble .**  
    - N2: 1 (he)
    - V1: 1 (scribble)

98. **the paper .**  
    - N5: 1 (the paper)

99. **ge(t) spankin(g) .**  
    - V1: 1 (ge(t))
    - V7: 1 (spankin(g))

100. **Bugs write on the table .**  
    - N1: 1 (Bugs)
    - V1: 1 (write)
    - V3: 1 (on the table)

Now, let's compile the scores:

- N1: 20
- N2: 14
- N3: 0
- N4: 0
- N5: 12
- N6: 0
- N7: 3
- N8: 0
- N9: 0
- N10: 0
- N11: 0
- V1: 20
- V2: 0
- V3: 5
- V4: 1
- V5: 0
- V6: 6
- V7: 2
- V8: 0
- V9: 0
- V10: 0
- V11: 0
- V12: 2
- V13: 0
- V14: 0
- V15: 0
- V16: 0
- V17: 0
- Q1: 6
- Q2: 0
- Q3: 4
- Q4: 0
- Q5: 0
- Q6: 0
- Q7: 0
- Q8: 0
- Q9: 0
- Q10: 0
- Q11: 0
- S1: 0
- S2: 0
- S3: 0
- S4: 0
- S5: 1
- S6: 0
- S7: 0
- S8: 0
- S9: 0
- S10: 0
- S11: 0
- S12: 0
- S13: 0
- S14: 0
- S15: 0
- S16: 0
- S17: 0
- S18: 0
- S19: 0
- S20: 0
Final score:
N1, 2
N2, 2
N3, 0
N4, 0
N5, 2
N6, 0
N7, 2
N8, 0
N9, 0
N10, 0
N11, 0
V1, 2
V2, 0
V3, 2
V4, 1
V5, 0
V6, 2
V7, 2
V8, 0
V9, 0
V10, 0
V11, 0
V12, 2
V13, 0
V14, 0
V15, 0
V16, 0
V17, 0
Q1, 2
Q2, 0
Q3, 2
Q4, 0
Q5, 0
Q6, 0
Q7, 0
Q8, 0
Q9, 0
Q10, 0
Q11, 0
S1, 0
S2, 0
S3, 0
S4, 0
S5, 1
S6, 0
S7, 0
S8, 0
S9, 0
S10, 0
S11, 0
S12, 0
S13, 0
S14, 0
S15, 0
S16, 0
S17, 0
S18, 0
S19, 0
S20, 0
"""

pattern = r"Final score:\s*((?:[NVSQ]\d{1,2}, \d\n?)+)"
match = re.search(pattern, text)

if match:
    print(match.group(0))  # Print the entire match
else:
    print("No match found")

