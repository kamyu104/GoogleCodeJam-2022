# [GoogleCodeJam 2022](https://codingcompetitions.withgoogle.com/codejam/archive/2022) ![Language](https://img.shields.io/badge/language-Python3-orange.svg) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE) ![Progress](https://img.shields.io/badge/progress-10%20%2F%2010-ff69b4.svg) ![Visitors](https://visitor-badge.laobi.icu/badge?page_id=kamyu104.googlecodejam.2022)

* Python3 solutions of Google Code Jam 2022. Solution begins with `*` means it will get TLE in the largest data set.
* Total computation amount > `10^8` is not friendly for Python3 to solve in 5 ~ 15 seconds.
* A problem was marked as `Very Hard` means that it was an unsolved one during the contest and may not be that difficult.

## Rounds

* [Code Jam 2021](https://github.com/kamyu104/GoogleCodeJam-2021)
* [Qualification Round](https://github.com/kamyu104/GoogleCodeJam-2022#qualification-round)
* [Round 1A](https://github.com/kamyu104/GoogleCodeJam-2022#qualification-round-1a)
* [Round 1B](https://github.com/kamyu104/GoogleCodeJam-2022#qualification-round-1b)

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
|C| [ASeDatAb](https://codingcompetitions.withgoogle.com/codejam/round/000000000087711b/0000000000acd29b)| [Python3](./Round%201B/asedatab.py3)| precompute: _O(8 * 2^8)_<br>runtime: _O(8 * 2^8)_ | _O(8 * 2^8)_ | Hard | | Precompute, Constructive Algorithms |
