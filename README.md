# [GoogleCodeJam 2022](https://codingcompetitions.withgoogle.com/codejam/archive/2022) ![Language](https://img.shields.io/badge/language-Python3-orange.svg) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE) ![Progress](https://img.shields.io/badge/progress-22%20%2F%2022-ff69b4.svg) ![Visitors](https://visitor-badge.laobi.icu/badge?page_id=kamyu104.googlecodejam.2022)

* Python3 solutions of Google Code Jam 2022. Solution begins with `*` means it will get TLE in the largest data set.
* Total computation amount > `10^8` is not friendly for Python3 to solve in 5 ~ 15 seconds.
* A problem was marked as `Very Hard` means that it was an unsolved one during the contest and may not be that difficult.

## Rounds

* [Code Jam 2021](https://github.com/kamyu104/GoogleCodeJam-2021)
* [Qualification Round](https://github.com/kamyu104/GoogleCodeJam-2022#qualification-round)
* [Round 1A](https://github.com/kamyu104/GoogleCodeJam-2022#round-1a)
* [Round 1B](https://github.com/kamyu104/GoogleCodeJam-2022#round-1b)
* [Round 1C](https://github.com/kamyu104/GoogleCodeJam-2022#round-1c)
* [Round 2](https://github.com/kamyu104/GoogleCodeJam-2022#round-2)
* [Round 3](https://github.com/kamyu104/GoogleCodeJam-2022#round-3)

## Qualification Round
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Punched Cards](https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4621b)| [Python3](./Qualification%20Round/punched_cards.py3)| _O(R * C)_ | _O(1)_ | Easy | | Array |
|B| [3D Printing](https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4672b)| [Python3](./Qualification%20Round/three_d_printing.py3)| _O(1)_ | _O(1)_ | Easy | | Math |
|C| [d1000000](https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a46471)| [PyPy3](./Qualification%20Round/d1000000.py3) [Python3](./Qualification%20Round/d1000000-2.py3)| _O(NlogN)_ | _O(1)_ | Easy | | Sort |
|D| [Chain Reactions](https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a45ef7)| [Python3](./Qualification%20Round/chain_reactions.py3) [Python3](./Qualification%20Round/chain_reactions2.py3) |  _O(N)_ | _O(N)_ | Medium | | Topological Sort, Greedy |
|E| [Twisty Little Passages](https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a45fc0)| [Python3](./Qualification%20Round/twisty_little_passages.py3) [Python3](./Qualification%20Round/twisty_little_passages2.py3) |  _O(min(K, N))_ | _O(min(K, N))_ | Hard | | Probability, Importance Sampling |

## Round 1A
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Double or One Thing](https://codingcompetitions.withgoogle.com/codejam/round/0000000000877ba5/0000000000aa8e9c)| [Python3](./Round%201A/double_or_one_thing.py3)| _O(\|S\|)_ | _O(1)_ | Easy | | String |
|B| [Equal Sum](https://codingcompetitions.withgoogle.com/codejam/round/0000000000877ba5/0000000000aa8fc1)| [Python3](./Round%201A/equal_sum.py3) [Python3](./Round%201A/equal_sum2.py3) | _O(N)_ | _O(1)_ | Medium | | Math, Constructive Algorithms |
|C| [Weightlifting](https://codingcompetitions.withgoogle.com/codejam/round/0000000000877ba5/0000000000aa9280)| [Python3](./Round%201A/weightlifting.py3)| _O(E^2 * W + E^3)_ | _O(E^2 + W)_ | Hard | | DP |

## Round 1B
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Pancake Deque](https://codingcompetitions.withgoogle.com/codejam/round/000000000087711b/0000000000acd59d)| [Python3](./Round%201B/pancake_deque.py3)| _O(N)_ | _O(1)_ | Easy | | Greedy |
|B| [Controlled Inflation](https://codingcompetitions.withgoogle.com/codejam/round/000000000087711b/0000000000accfdb)| [Python3](./Round%201B/controlled_inflation.py3) | _O(N * P)_ | _O(1)_ | Medium | | DP |
|C| [ASeDatAb](https://codingcompetitions.withgoogle.com/codejam/round/000000000087711b/0000000000acd29b)| [Python3](./Round%201B/asedatab.py3) [Python3](./Round%201B/asedatab2.py3) [Python3](./Round%201B/asedatab3.py3) | _O(L * 2^L)_ | _O(L)_ | Hard | | Precompute, BFS, Topological Sort, Constructive Algorithms 

## Round 1C
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Letter Blocks](https://codingcompetitions.withgoogle.com/codejam/round/0000000000877b42/0000000000afe6a1)| [Python3](./Round%201C/letter_blocks.py3)| _O(N * L)_ | _O(N)_ | Easy | | String |
|B| [Squary](https://codingcompetitions.withgoogle.com/codejam/round/0000000000877b42/0000000000afdf76)| [Python3](./Round%201C/squary.py3) | _O(N)_ | _O(1)_ | Medium | | Math, Constructive Algorithms |
|C| [Intranets](https://codingcompetitions.withgoogle.com/codejam/round/0000000000877b42/0000000000afeb38)| [Python3](./Round%201C/intranets.py3) [Python3](./Round%201C/intranets2.py3) | precompute: _O(MAX_M)_<br>runtime: _O(1)_ | _O(MAX_M)_ | Hard | |  Inclusion‐Exclusion Principle, Combinatorics, Catalan Number |

## Round 2
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Spiraling Into Control](https://codingcompetitions.withgoogle.com/codejam/round/00000000008778ec/0000000000b15a74)| [Python3](./Round%202/spiraling_into_control.py3)| _O(N)_ | _O(1)_ | Easy | | Constructive Algorithms, Greedy, Math |
|B| [Pixelated Circle](https://codingcompetitions.withgoogle.com/codejam/round/00000000008778ec/0000000000b158f7)| [Python3](./Round%202/pixelated_circle.py3) | _O(R)_ | _O(1)_ | Medium | | Math |
|C| [Saving the Jelly](https://codingcompetitions.withgoogle.com/codejam/round/00000000008778ec/0000000000b158f8)| [PyPy3](./Round%202/saving_the_jelly.py3)| _O(N^2 * sqrt(N))_ | _O(N^2)_ | Medium | | Bipartite Matching, Hopcroft-Karp Algorithm |
|D| [I, O Bot](https://codingcompetitions.withgoogle.com/codejam/round/00000000008778ec/0000000000b15167)| [Python3](./Round%202/io_bot.py3)| _O(NlogN)_ | _O(N)_ | Hard | | DP, Prefix Sum, Hash Table |

## Round 3
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Revenge of GoroSort](https://codingcompetitions.withgoogle.com/codejam/round/00000000008779b4/0000000000b45189)| [Python3](./Round%203/revenge_of_gorosort.py3)| _O(K * N)_ | _O(N)_ | Easy | | Math, Expected Value, Trial and Error |
|B| [Duck, Duck, Geese](https://codingcompetitions.withgoogle.com/codejam/round/00000000008779b4/0000000000b45244)| [PyPy3](./Round%203/duck_duck_geese.py3) [C++](./Round%203/duck_duck_geese.cpp) | _O(NlogN)_ | _O(N)_ | Medium | | Segment Tree |
|C| [Mascot Maze](https://codingcompetitions.withgoogle.com/codejam/round/00000000008779b4/0000000000b44a4f)| [Python3](./Round%203/mascot_maze.py3)| _O(N)_ | _O(N)_ | Medium | | Topological Sort, Greedy |
|D| [Win As Second](https://codingcompetitions.withgoogle.com/codejam/round/00000000008779b4/0000000000b4518a)| [Python3](./Round%203/win_as_second.py3)| _O(NlogN)_ | _O(N)_ | Hard | | Sprague-Grundy Theorem, Trial and Error, Precompute |
