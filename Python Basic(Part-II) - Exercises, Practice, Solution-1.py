# Napisz program Python, aby utworzyć wszystkie możliwe struny za pomocą 'a', 'e', 'i', 'o', 'u'. Znaków należy używać dokładnie raz.
import random
char_list = ['a','e','i','o','u']
random.shuffle(char_list)
print(''.join(char_list))
# iauoe


# Zapisz program Python, aby usunąć i wydrukować co trzeci numer z listy numerów, aż lista stanie się pusta.
def remove_nums(int_list):
  #list starts with 0 index
  position = 3 - 1 
  idx = 0
  len_list = (len(int_list))
  while len_list>0:
    idx = (position+idx)%len_list
    print(int_list.pop(idx))
    len_list -= 1
nums = [10,20,30,40,50,60,70,80,90]
remove_nums(nums)
# 30
# 60
# 90
# 40
# 80
# 50
# 20
# 70
# 10

# Napisz program Python, aby znaleźć unikalne trojaczki, których trzy elementy dają sumę zerową z tablicy n liczb całkowitych.
def three_sum(nums):
  result = []
  nums.sort()
  for i in range(len(nums)-2):
    if i> 0 and nums[i] == nums[i-1]:
      continue
    l, r = i+1, len(nums)-1
    while l < r:
      s = nums[i] + nums[l] + nums[r]
      if s > 0:
        r -= 1
      elif s < 0:
          l += 1
      else:
        # found three sum
        result.append((nums[i], nums[l], nums[r]))
        # remove duplicates
        while l < r and nums[l] == nums[l+1]:
          l+=1
          while l < r and nums[r] == nums[r-1]:
            r -= 1
            l += 1
            r -= 1
          return result

x = [1, -6, 4, 2, -1, 2, 0, -2, 0 ]
print(three_sum(x))
# [(-6, 2, 4)]


# Napisz program Python, aby utworzyć kombinację 3-cyfrowej kombinacji.
numbers = []
for num in range(1000):
  num=str(num).zfill(3)
print(num)
numbers.append(num)
# 999


# Napisz program Python, aby wydrukować długi tekst, przekonwertować ciąg na listę i wydrukować wszystkie słowa i ich częstotliwości.
string_words = '''United States Declaration of Independence
From Wikipedia, the free encyclopedia
The United States Declaration of Independence is the statement
adopted by the Second Continental Congress meeting at the Pennsylvania State
House (Independence Hall) in Philadelphia on July 4, 1776, which announced
that the thirteen American colonies, then at war with the Kingdom of Great
Britain, regarded themselves as thirteen independent sovereign states, no longer
under British rule. These states would found a new nation – the United States of
America. John Adams was a leader in pushing for independence, which was passed
on July 2 with no opposing vote cast. A committee of five had already drafted the
formal declaration, to be ready when Congress voted on independence.

John Adams persuaded the committee to select Thomas Jefferson to compose the original
draft of the document, which Congress would edit to produce the final version.
The Declaration was ultimately a formal explanation of why Congress had voted on July
2 to declare independence from Great Britain, more than a year after the outbreak of
the American Revolutionary War. The next day, Adams wrote to his wife Abigail: "The
Second Day of July 1776, will be the most memorable Epocha, in the History of America."
But Independence Day is actually celebrated on July 4, the date that the Declaration of
Independence was approved.

After ratifying the text on July 4, Congress issued the Declaration of Independence in
several forms. It was initially published as the printed Dunlap broadside that was widely
distributed and read to the public. The source copy used for this printing has been lost,
and may have been a copy in Thomas Jefferson's hand.[5] Jefferson's original draft, complete
with changes made by John Adams and Benjamin Franklin, and Jefferson's notes of changes made
by Congress, are preserved at the Library of Congress. The best-known version of the Declaration
is a signed copy that is displayed at the National Archives in Washington, D.C., and which is
popularly regarded as the official document. This engrossed copy was ordered by Congress on
July 19 and signed primarily on August 2.

The sources and interpretation of the Declaration have been the subject of much scholarly inquiry.
The Declaration justified the independence of the United States by listing colonial grievances against
King George III, and by asserting certain natural and legal rights, including a right of revolution.
Having served its original purpose in announcing independence, references to the text of the
Declaration were few in the following years. Abraham Lincoln made it the centerpiece of his rhetoric
(as in the Gettysburg Address of 1863) and his policies. Since then, it has become a well-known statement
on human rights, particularly its second sentence:

We hold these truths to be self-evident, that all men are created equal, that they are endowed by their
Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness.

This has been called "one of the best-known sentences in the English language", containing "the most potent
and consequential words in American history". The passage came to represent a moral standard to which
the United States should strive. This view was notably promoted by Abraham Lincoln, who considered the
Declaration to be the foundation of his political philosophy and argued that it is a statement of principles
through which the United States Constitution should be interpreted.

The U.S. Declaration of Independence inspired many other similar documents in other countries, the first
being the 1789 Declaration of Flanders issued during the Brabant Revolution in the Austrian Netherlands
(modern-day Belgium). It also served as the primary model for numerous declarations of independence across
Europe and Latin America, as well as Africa (Liberia) and Oceania (New Zealand) during the first half of the
19th century.'''

word_list = string_words.split()

word_freq = [word_list.count(n) for n in word_list]

print("String:\n {} \n".format(string_words))
print("List:\n {} \n".format(str(word_list)))
print("Pairs (Words and Frequencies:\n {}".format(str(list(zip(word_list, word_freq)))))
# ....


# Napisz program Python, aby policzyć liczbę każdego znaku danego tekstu pliku tekstowego.
# Wejścia:
# abc.txt -
# Dzień jedność Niemiec
# Z Wikipedii, wolnej encyklopedii
# Dzień jedności Niemiec (niemiecki: Tag der DeutschenEinheit) to narodowy dzień Niemiec, obchody święta publicznego, które odprawiono 3 października. It upamiętnia rocznicę zjednoczenia Niemiec w 1990 roku, kiedy cel zjednoczonej Niemiec, który powstał w połowie XIX wieku, został ponownie osiągnięty. Dlatego też nazwa nie odnosi się ani do ponownego zjednoczenia, ani do Unii, ale do jedności Niemiec. Dzień zjednoczenia Niemiec w dniu 3 października jest świętem narodowym Niemiec od 1990 r., kiedy to zjednoczenie zostało oficjalnie zakończone.
import collections
import pprint
file_input = input('File Name: ')
with open(file_input, 'r') as info:
  count = collections.Counter(info.read().upper())
  value = pprint.pformat(count)
print(value)
# File Name:  abc.txt
# Counter({' ': 93,
#          'E': 64,
#          'N': 45,
#          'A': 42,
#          'T': 40,
#          'I': 36,
#          'O': 31,
#          'R': 29,
#          'H': 25,
#          'D': 19,
#          'M': 17,
#          'Y': 17,
#          'L': 15,
#          'F': 15,
#          'U': 14,
#          'C': 13,
#          'G': 13,
#          'S': 12,
#          ',': 7,
#          'B': 6,
#          'W': 5,
#          '9': 5,
#          '.': 4,
#          'P': 4,
#          '1': 3,
#          '\n': 2,
#          '0': 2,
#          '3': 2,
#          ':': 1,
#          '-': 1,
#          'K': 1,
#          '(': 1,
#          ')': 1,
#          'V': 1})


# Napisz program Python, aby uzyskać listę lokalnie zainstalowanych modułów Python.
import pkg_resources
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
for m in installed_packages_list:
    print(m)
# asn1crypto==0.24.0
# beautifulsoup4==4.5.1
# biopython==1.71
# bkcharts==0.2
# bokeh==0.12.6
# cairocffi==0.9.0
# cairosvg==2.0.3
# certifi==2018.11.29
# cffi==1.11.5
# ...


# Zapisz program Python, aby sprawdzić sumę trzech elementów (każdy z tablicy) z trzech tablic jest równa wartości docelowej. Wydrukuj wszystkie trzy kombinacje elementów.
# Sample data:
# /*
# X = [10, 20, 20, 20]
# Y = [10, 20, 30, 40]
# Z = [10, 30, 40, 20]
# target = 70
# */
import itertools
from functools import partial
X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]
T = 70

def check_sum_array(N, *nums):
  if sum(x for x in nums) == N:
    return (True, nums)
  else:
      return (False, nums)
pro = itertools.product(X,Y,Z)
func = partial(check_sum_array, T)
sums = list(itertools.starmap(func, pro))

result = set()
for s in sums:
    if s[0] == True and s[1] not in result:
      result.add(s[1])
      print(result)
# {(10, 20, 40)}
# {(10, 20, 40), (10, 30, 30)}
# {(10, 20, 40), (10, 30, 30), (10, 40, 20)}
# {(10, 20, 40), (10, 30, 30), (20, 10, 40), (10, 40, 20)}
# {(10, 20, 40), (20, 20, 30), (10, 30, 30), (20, 10, 40), (10, 40, 20)}
# {(10, 20, 40), (10, 40, 20), (20, 10, 40), (10, 30, 30), (20, 20, 30), (20, 30, 20)}
# {(10, 20, 40), (10, 40, 20), (20, 10, 40), (20, 40, 10), (10, 30, 30), (20, 20, 30), (20, 30, 20)}


# Napisz program Python, aby utworzyć wszystkie możliwe permutacje z danego zbioru odrębnych liczb.
def permute(nums):
  result_perms = [[]]
  for n in nums:
    new_perms = []
    for perm in result_perms:
      for i in range(len(perm)+1):
        new_perms.append(perm[:i] + [n] + perm[i:])
        result_perms = new_perms
  return result_perms

my_nums = [1,2,3]
print("Original Cofllection: ",my_nums)
print("Collection of distinct numbers:\n",permute(my_nums))
# Original Cofllection:  [1, 2, 3]
# Collection of distinct numbers:
#  [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]]


# Napisz program Python, aby uzyskać wszystkie możliwe dwucyfrowe kombinacje liter z ciągu cyfr (od 1 do 9).
# string_maps = {
# „1”: „abc”,
# "2": "def",
# „3”: „ghi”,
# „4”: „jkl”,
# „5”: „mno”,
# „6”: „pqrs”,
# „7”: „tuv”,
# „8”: „wxy”,
# „9”: „z”
# }
def letter_combinations(digits):
    if digits == "":
        return []
    string_maps = {
        "1": "abc",
        "2": "def",
        "3": "ghi",
        "4": "jkl",
        "5": "mno",
        "6": "pqrs",
        "7": "tuv",
        "8": "wxy",
        "9": "z"
    }
    result = [""]
    for num in digits:
        temp = []
        for an in result:
            for char in string_maps[num]:
                temp.append(an + char)
        result = temp
    return result

digit_string = "47"
print(letter_combinations(digit_string))
digit_string = "29"
print(letter_combinations(digit_string))
# ['jt', 'ju', 'jv', 'kt', 'ku', 'kv', 'lt', 'lu', 'lv']
# ['dz', 'ez', 'fz']


# Napisz program Python, aby dodać dwa dodatnie liczby całkowite bez użycia operatora „+”.
# Uwaga: Aby dodać dwie liczby, należy użyć operacji bitowej.
def add_without_plus_operator(a, b):
    while b != 0:
        data = a & b
        a = a ^ b
        b = data << 1
    return a
print(add_without_plus_operator(2, 10))
print(add_without_plus_operator(-20, 10))
print(add_without_plus_operator(-10, -20))
# 12
# -10
# -30


# Napisz program Python, aby sprawdzić priorytet czterech operatorów (+, -, *, /).
from collections import deque
import re

__operators__ = "+-/*"
__parenthesis__ = "()"
__priority__ = {
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1,
}

def test_higher_priority(operator1, operator2):
    return __priority__[operator1] >= __priority__[operator2]

print(test_higher_priority('*','-'))
print(test_higher_priority('+','-'))
print(test_higher_priority('+','*'))
print(test_higher_priority('+','/'))
print(test_higher_priority('*','/'))
# True
# True
# False
# False
# True


# Napisz program Python, aby znaleźć cyfry nieobecne w danym numerze telefonu komórkowego.
def absent_digits(n):
  all_nums = set([0,1,2,3,4,5,6,7,8,9])
  n = set([int(i) for i in n])
  n = n.symmetric_difference(all_nums)
  n = sorted(n)
  return n
print(absent_digits([9,8,3,2,2,0,9,7,6,3]))
# [1, 4, 5]

# Napisz program Python, aby obliczyć sumę bezwzględnej różnicy wszystkich odrębnych par w danej tablicy (kolejność nie zmniejszająca się).

# Przykładowa tablica: [1, 2, 3]
# Wtedy wszystkie odrębne pary będą:
# 1 2
# 1 3
# 2 3
def sum_distinct_pairs(arr):
    result = 0
    i = 0
    while i<len(arr):
        result+=i*arr[i]-(len(arr)-i-1)*arr[i]
        i+=1
    return result
print(sum_distinct_pairs([1,2,3]))
print(sum_distinct_pairs([1,4,5]))
# 4
# 8


# Napisz program Python, aby znaleźć typ postępu (arytmetyczna progresja/postęp geometryczny) i następnego kolejnego członka danej trzech kolejnych członków sekwencji.
# Według Wikipedii, arytmetyczna progresja (AP) jest sekwencją liczb tak, że różnica pomiędzy dwoma kolejnymi członkami sekwencji jest stała. Na przykład sekwencja 3, 5, 7, 9, 11, 13, . . . to arytmetyczna progresja ze wspólną różnicą 2. Dla tego problemu ograniczymy się do arytmetycznej progresji, której wspólna różnica jest liczbą całkowitą niezerową. Z drugiej strony, postęp geometryczny (GP) jest sekwencją liczb, w której każdy termin po pierwszym znaleziony jest przez przeiniecie poprzedniego przez stałą niezerową liczbę zwaną wspólnym stosunkiem. Na przykład sekwencja 2, 6, 18, 54, . . . jest geometrycznym postępem o wspólnym stosunku 3. W związku z tym będziemy ...
# jest geometrycznym postępem o wspólnym stosunku 3. Dla tego problemu ograniczymy się do geometrycznego postępu, którego wspólny stosunek jest liczbą całkowitą różną od zera.
def ap_gp_sequence(arr):
  if arr[0]==arr[1]==arr[2]==0:
    return "Wrong Numbers"
  else:
    if arr[1]-arr[0]==arr[2]-arr[1]:
      n=2*arr[2]-arr[1]
      return "AP sequence, "+'Next number of the sequence: '+str(n)
    else:
      n=arr[2]**2/arr[1]
      return "GP sequence, " + 'Next number of the sequence:  '+str(n)

print(ap_gp_sequence([1,2,3]))
print(ap_gp_sequence([2,6,18]))
print(ap_gp_sequence([0,0,0]))
# AP sequence, Next number of the sequence: 4
# GP sequence, Next number of the sequence:  54.0
# Wrong Numbers


# Napisz program Python, aby wydrukować długość serii i serii z danego 3. Terminu, 3. Ostatniego terminu i sumy serii.
# Niech X i Y oznaczają odpowiednio trzeci i trzeci ostatni termin postępu arytmetycznego
# Tzn. X=A+2d i Y=A+(n-3)d gdzie a, d i n są tym, czego można się spodziewać.
# Należy pamiętać, że mamy podane X i Y
# Teraz mamy również sumę n terminów, tj. S=n2[2a+(n-1)d]
# Wyd. S=n2[(A+2d)+(A+(n-3)d)]
# WYD. S=N2[X+Y]
# Wyd=2SX+Y
# Po obliczeniu n, możemy podłączyć go z powrotem do wyrażenia Y.
# To da nam 2 równań w 2 niewiadomych (a i d), które możemy rozwiązać, aby określić pozostałe zmienne.
# X=A+2d i Y=A+(2SX+Y-3)d
# Odniesienie: https://bit.ly/2N2VM9f

# Input third term of the series: 3
# Input 3rd last term: 3
# Input Sum of the series: 15
# Length of the series: 5
# Series:
# 1 2 3 4 5
tn = int(input("Input third term of the series:"))
tltn = int(input("Input 3rd last term:"))
s_sum = int(input("Sum of the series:"))
n = int(2*s_sum/(tn+tltn))
print("Length of the series: ",n)


if n-5==0:
  d = (s_sum-3*tn)//6
else:
  d = (tltn-tn)/(n-5)

a = tn-2*d
j = 0
print("Series:")
for j in range(n-1):
  print(int(a),end=" ")
  a+=d
print(int(a),end=" ")
# Input third term of the series: 3
# Input 3rd last term: 6
# Sum of the series: 36
# Length of the series:  8
# Series:
# 1 2 3 4 5 6 7 8 


# Napisz program Python, aby znaleźć wspólne podziały pomiędzy dwoma liczbami w danej parze.
def ngcd(x, y):
    i=1
    while(i<=x and i<=y):
        if(x%i==0 and y%i == 0):
            gcd=i;
        i+=1
    return gcd;
def num_comm_div(x, y):
  n = ngcd(x, y)
  result = 0
  z = int(n**0.5)
  i = 1
  while( i <= z ):
    if(n % i == 0):
      result += 2 
      if(i == n/i):
        result-=1
    i+=1
  return result

print("Number of common divisors: ",num_comm_div(2, 4))
print("Number of common divisors: ",num_comm_div(2, 8))
print("Number of common divisors: ",num_comm_div(12, 24))
# Number of common divisors:  2
# Number of common divisors:  2
# Number of common divisors:  6


# 30 Napisz program Python, aby odwrócić cyfry danego numeru i dodać go do oryginału, jeśli suma nie jest palindrome powtórzyć tę procedurę.
# Uwaga: Palindrome to słowo, liczba lub inna sekwencja znaków, która czyta tak samo wstecz jak do przodu, jak np. madam czy racekar.
def rev_number(n):
  s = 0
  while True:
    k = str(n)
    if k == k[::-1]:
      break
    else:
      m = int(k[::-1])
      n += m
      s += 1
  return n 

print(rev_number(1234))
print(rev_number(1473))
# 5555
# 9339


# Napisz program Python, aby policzyć liczbę operacji przenoszenia dla każdego zestawu dodatkowych problemów.
# Zgodnie z Wikipedii " w podstawowej arytmetycznej, przeniesienie jest cyfrą, która jest przenoszona z jednej kolumny cyfr do innej kolumny o bardziej znaczących cyfrach. It jest częścią standardowego algorytmu, który umożliwia dodawanie numerów do siebie, rozpoczynając od skrajnie prawej cyfry i pracując po lewej stronie. Na przykład po dodaniu 6 i 7 do make 13 w tej samej kolumnie zapisywana jest wartość „3”, a wartość „1” w lewo”.
def carry_number(x, y):
  ctr = 0
  if(x == 0 and y == 0):
    return 0
  z = 0  
  for i in reversed(range(10)):
      z = x%10 + y%10 + z
      if z > 9:
        z = 1
      else:
        z = 0
      ctr += z
      x //= 10
      y //= 10
      
  if ctr == 0:
    return "No carry operation."
  elif ctr == 1:
    return ctr
  else:
    return ctr
print(carry_number(786, 457))
print(carry_number(5, 6))
# 3
# 1


# Napisz program Python, aby znaleźć wyżyny trzech najlepszych budynków w kolejności zstępującej z ośmiu budynków.
# Wejście:
# 0 ≤ wysokość budynku (liczba całkowita) ≤ 10,000
print("Input the heights of eight buildings:")
l = [int(input()) for i in range(8)]
print("Heights of the top three buildings:")
l = sorted(l)
print(*l[:4:-1], sep='\n')
# Input the heights of eight buildings:
#  25
#  35
#  15
#  16
#  30
#  45
#  37
#  39
# Heights of the top three buildings:
# 45
# 39
# 37


# Napisz program Python, aby obliczyć liczbę cyfr sumy dwóch podanych liczb całkowitych.
# Wejście:
# Każdy przypadek testowy składa się z dwóch nieujemnych liczb całkowitych x i y, oddzielonych spacją w linii.
# 0 ≤ x, y ≤ 1,000,000
print("Input two integers(a b): ")
a,b = map(int,input().split(" "))
print("Number of digit of a and b.:")
print(len(str(a+b)))
#  Input two integers(a b): 
#  5 7
# Number of digit of a and b.:
# 2


# Napisz program Python, aby sprawdzić, czy trzy podane długości (liczby całkowite) trzech boków tworzą prawy trójkąt. Drukuj „Tak”, jeśli strony tworzą prawy trójkąt, w przeciwnym razie wydrukuj „nie”.
# Wejście:
# Liczby całkowite oddzielone pojedynczą przestrzenią.
# 1 ≤ długość boku ≤ 1,000
print("Input three integers(sides of a triangle)")
int_num = list(map(int,input().split()))
x,y,z = sorted(int_num)
if x**2+y**2==z**2:
    print('Yes')
else:
    print('No')
# Input three integers(sides of a triangle)
#  8 6 7
# No



# Napisz program Python, który rozwiązuje równanie:
# ax+by=c
# dx+ey=f
# Wydrukować wartości x, y, gdzie a, b, c, d, podane są e i f.

# Wejście:
# a,b,c,d,e,f oddzielone pojedynczą przestrzenią.
# (-1,000 ≤ a,b,c,d,e,f ≤ 1,000)
# Wprowadzić wartość a, b, c, d, e, f:
# 5 8 6 7 9 4
# Wartości x i y:
# -2.000 2.000
print("Input the value of a, b, c, d, e, f:")
a, b, c, d, e, f = map(float, input().split())
n = a*e - b*d
print("Values of x and y:")
if n != 0:
    x = (c*e - b*f) / n
    y = (a*f - c*d) / n
    print('{:.3f} {:.3f}'.format(x+0, y+0))
# Input the value of a, b, c, d, e, f:
#  5 8 6 7 9 4
# Values of x and y:
# -2.000 2.000


# Napisz program Python, aby obliczyć kwotę długu w n miesiącach. Kwota kredytu wynosi 100,000 dolarów, a pożyczka dodaje 5% odsetek od długu i zaokrągla go do najbliższych 1,000 powyżej miesiąca na miesiąc.
# Wejście:
# Liczba całkowita n (0 ≤ n ≤ 100)
# Wprowadź liczbę miesięcy: 7
# Kwota długu: $144000
def round_n(n):
    if n%1000:
        return (1+n//1000)*1000
    else:
        return n
     
def compute_debt(n):
    if n==0: return 100000
    return int(round_n(compute_debt(n-1)*1.05))

print("Input number of months:")
result = compute_debt(int(input()))
print("Amount of debt: ","$"+str(result).strip())
# Input number of months:
#  7
# Amount of debt:  $144000


# Napisz program Python, który odczytuje liczbę całkowitą n i odnajduje liczbę kombinacji a,b,c i d (0 ≤ a,b,c,d ≤ 9) gdzie (a + b + c + d) będzie równa n.
# Wejście:
# n (1 ≤ n ≤ 50)
# Wprowadź numer(n): 15
# Liczba kombinacji: 592
import itertools
print("Input the number(n):")
n=int(input())
result=0
for (i,j,k) in itertools.product(range(10),range(10),range(10)):
    result+=(0<=n-(i+j+k)<=9)
print("Number of combinations:",result)
# Input the number(n):
#  15
# Number of combinations: 592


# Zapisz program Python, aby wydrukować liczbę liczb głównych, które są mniejsze lub równe danej liczbie całkowitej.
# Wejście:
# n (1 ≤ n ≤ 999,999)
# Wprowadź numer(n): 35
# Liczba liczb pierwszych, które są mniejsze lub równe n.: 11
primes = [1] * 500000
primes[0] = 0
 
for i in range(3, 1000, 2):
    if primes[i // 2]:
        primes[(i * i) // 2::i] = [0] * len(primes[(i * i) // 2::i])
 
print("Input the number(n):")
n=int(input())
if n < 4:
    print("Number of prime numbers which are less than or equal to n.:",n - 1)
else:
    print("Number of prime numbers which are less than or equal to n.:",sum(primes[:(n + 1) // 2]) + 1)
# Input the number(n):
#  35
# Number of prime numbers which are less than or equal to n.: 11


# Zapisz program, aby obliczyć promień i środkową współrzędną (x, y) okręgu, który jest zbudowany przez trzy punkty na powierzchni płaszczyzny.
# Wejście:
# x1, y1, x2, y2, x3, y3 oddzielone pojedynczą przestrzenią.
print("Input three coordinate of the circle:")
x1, y1, x2, y2, x3, y3 = map(float, input().split())
c = (x1-x2)**2 + (y1-y2)**2
a = (x2-x3)**2 + (y2-y3)**2
b = (x3-x1)**2 + (y3-y1)**2
s = 2*(a*b + b*c + c*a) - (a*a + b*b + c*c) 
px = (a*(b+c-a)*x1 + b*(c+a-b)*x2 + c*(a+b-c)*x3) / s
py = (a*(b+c-a)*y1 + b*(c+a-b)*y2 + c*(a+b-c)*y3) / s 
ar = a**0.5
br = b**0.5
cr = c**0.5 
r = ar*br*cr / ((ar+br+cr)*(-ar+br+cr)*(ar-br+cr)*(ar+br-cr))**0.5
print("Radius of the said circle:")
print("{:>.3f}".format(r))
print("Central coordinate (x, y) of the circle:")
print("{:>.3f}".format(px),"{:>.3f}".format(py))
# Input three coordinate of the circle:
#  9 3 6 8 3 6
# Radius of the said circle:
# 3.358
# Central coordinate (x, y) of the circle:
# 6.071 4.643


# Napisz program Python, aby sprawdzić, czy punkt (x,y) znajduje się w trójkącie, czy nie. Istnieje trójkąt utworzony przez trzy punkty.
# Wejście:
# x1,y1,x2,y2,x3,y3,xp,yp oddzielone pojedynczą przestrzenią.
print("Input x1,y1,x2,y2,x3,y3,xp,yp:")
x1,y1,x2,y2,x3,y3,xp,yp = map(float, input().split())
c1 = (x2-x1)*(yp-y1)-(y2-y1)*(xp-x1)
c2 = (x3-x2)*(yp-y2)-(y3-y2)*(xp-x2)
c3 = (x1-x3)*(yp-y3)-(y1-y3)*(xp-x3)
if (c1<0 and c2<0 and c3<0) or (c1>0 and c2>0 and c3>0):
    print("The point is in the triangle.")
else:
    print("The point is outside the triangle.")
# Input x1,y1,x2,y2,x3,y3,xp,yp:
#  2 3 4 5 6 8 7 1
# The point is outside the triangle


# Zapisz program Python, aby obliczyć i wydrukować sumę dwóch podanych liczb całkowitych (więcej niż lub równych zero). Jeśli podane liczby całkowite lub suma mają więcej niż 80 cyfr, należy wydrukować „przepełnienie”.
print("Input first integer:")
x = int(input())
print("Input second integer:")
y = int(input())
if x >= 10 ** 80 or y >= 10 ** 80 or x + y >= 10 ** 80:
    print("Overflow!")
else:
    print("Sum of the two integers: ",x + y)
# Input first integer:
#  25
# Input second integer:
#  22
# Sum of the two integers:  47


# Napisz program Python, który akceptuje sześć cyfr jako dane wejściowe i sortuje je w kolejności odwrotnej.
# Wejście:
# Wejście składa się z sześciu cyfr n1, N2, N3, N4, N5, n6 (-100000 ≤ n1, n2, n3, n4, n5, n6 ≤ 100000). Sześć cyfr jest oddzielonych spacją.
# Wprowadź sześć liczb całkowitych:
# 15 30 25 14 35 40
# Po sortowaniu wymienionych liczb całkowitych:
# 40 35 30 25 15 14
print("Input six integers:")
nums = list(map(int, input().split()))
nums.sort()
nums.reverse()
print("After sorting the said ntegers:")
print(*nums)
# Input six integers:
#  15 30 25 14 35 40
# After sorting the said ntegers:
# 40 35 30 25 15 14


# Napisz program Python, aby sprawdzić, czy dwa wiersze PQ i RS są równoległe. Cztery punkty to P(x1, y1), Q(x2, y2), R(x3, y3), S(x4, y4).
# Wejście:
# x1,y1,x2,y2,x3,y3,xp,yp oddzielone pojedynczą przestrzenią
print("Input x1,y1,x2,y2,x3,y3,xp,yp:")
x1, y1,x2, y2, x3, y3, x4, y4 = map(float, input().split())
print('PQ and RS are parallel.' if abs((x2 - x1)*(y4 - y3) - (x4 - x3)*(y2 - y1)) < 1e-10 else 'PQ and RS are not parallel')
# Input x1,y1,x2,y2,x3,y3,xp,yp:
#  2 5 6 4 8 3 9 7
# PQ and RS are not parallel


# Napisz program Python, aby znaleźć maksymalną sumę sąsiadującego następstwa z danej sekwencji liczb a1, a2, a3, ... i. Następstość jednego elementu jest również następstością ciągłą.

# Wejście:
# Można założyć, że 1 ≤ n ≤ 5000 i -100000 ≤ AI ≤ 100000.
# Numery wejściowe są oddzielone spacją.
# Wprowadź 0, aby zakończyć.
# Wprowadź liczbę kolejnych cyfr, które chcesz wprowadzić (0, aby wyjść): 3
# Numery wejściowe:
# 2
# 4
# 6
# Maksymalna suma wymienionych kolejnych następowań:
# 12 Wprowadź liczbę kolejnych cyfr, które chcesz wprowadzić (0, aby wyjść): 0
while True:
    print("Input number of sequence of numbers you want to input (0 to exit):")
    n = int(input())
    if n == 0:
        break
    else:
        A = []
        Sum = []
        print("Input numbers:") 
        for i in range(n):
            A.append(int(input()))
        Wa = 0
        for i in range(0,n):
            Wa += A[i]
            Sum.append(Wa)
        for i in range(0 , n):
            for j in range(0 , i):
                Num = Sum[i] - Sum[j]
                Sum.append(Num)
        print("Maximum sum of the said contiguous subsequence:")
        print(max(Sum))
# Input number of sequence of numbers you want to input (0 to exit):
#  3
# Input numbers:
#  2
#  4
#  6
# Maximum sum of the said contiguous subsequence:
# 12
# Input number of sequence of numbers you want to input (0 to exit):
#  0


# Napisz program Python, do którego czyta się datę (od 2016/1/1 do 2016/12/31) i drukuje dzień daty. 1 stycznia 2016, jest piątek. Należy pamiętać, że rok 2016 to rok przestępny.
# Wejście:
# Dwa urządzenia m i d oddzielone pojedynczą przestrzenią w linii, m ,d oznacza miesiąc i dzień.
from datetime import date
print("Input month and date (separated by a single space):")
m, d = map(int, input().split())
weeks = {1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday',7:'Sunday'}
w = date.isoweekday(date(2016, m, d))
print("Name of the date: ",weeks[w])
# Input month and date (separated by a single space):
#  5 15
# Name of the date:  Sunday


# Napisz program Python, który czyta tekst (tylko znaki alfabetyczne i spacje). i drukuje dwa słowa. Pierwszy to słowo, które pojawia się najczęściej w tekście. Drugi to słowo, które ma maksymalną liczbę liter.
# Uwaga: Słowo jest sekwencją liter oddzielonych spacjami.
# Wejście:
# Tekst jest podany w wierszu z następującym warunkiem:
# a. Liczba liter w tekście jest mniejsza lub równa 1000.
# b. Liczba liter w słowie jest mniejsza lub równa 32.
# c. jest tylko jedno słowo, które pojawia się najczęściej w danym tekście.
# d. jest tylko jedno słowo, które ma maksymalną liczbę liter w danym tekście.
# Tekst: Dziękujemy za komentarz i udział w ankiecie.
# Wynik: Twoje uczestnictwo.
# Wejście:
# Tekst: Dziękujemy za komentarz i udział w ankiecie.
# Wynik: Twoje uczestnictwo.
import collections
print("Input a text in a line.")
text_list = list(map(str, input().split()))
sc = collections.Counter(text_list)
common_word = sc.most_common()[0][0]
max_char = ""
for s in text_list:
    if len(max_char) < len(s):
        max_char = s
print("\nMost frequent text and the word which has the maximum number of letters.")
print(common_word, max_char)
# Input a text in a line.
#  Thank you for your comment and your participation.

# Most frequent text and the word which has the maximum number of letters.
# your participation.


# Zapisz program Python, który odczytuje n cyfr (podanych) wybranych od 0 do 9 i drukuje liczbę kombinacji, w których suma cyfr jest równa innej podanej liczbie (s). Nie należy używać tych samych cyfr w kombinacji.
# Wejście:
# Dwóch liczb całkowitych jako liczba kombinacji i ich suma za pomocą jednego miejsca w linii. Wprowadź 0 0, aby zakończyć.
import itertools
print("Input number of combinations and sum, input 0 0 to exit:")
while True:
  x, y = map(int, input(). split())
  if x == 0 and y == 0:
    break
  s = list(itertools.combinations(range(10), x))
  ctr = 0
  for i in s:
    if sum(i) == y:
            ctr += 1
 
print(ctr)
# Input number of combinations and sum, input 0 0 to exit:
#  5 6
#  2 4
#  0 0
# 2


# Napisz program Python, aby zastąpić ciąg „Python” słowem „Java”, a „Java” słowem „Python” w danym ciągu.
# Wejście:
# Litery angielskie (w tym jednobajtowe znaki alfanumeryczne, puste miejsca, symbole) są podawane w jednym wierszu. Długość wprowadzanego ciągu znaków wynosi 1000 lub mniej.
# Wprowadź tekst z dwoma słowami „Python” i „Java”
# Wyjście:
# Wymieniany ciąg znaków języka Python i Java w jednym wierszu.
print("Input a text with two words 'Python' and 'Java'")
text = input().split()
for i in range(len(text)):
    if "Python" in text[i]:n = text[i].index("Python");text[i] = text[i][:n] + "Java" + text[i][n + 6:]
    elif "Java" in text[i]:n = text[i].index("Java");text[i] = text[i][:n] + "Python" + text[i][n + 4:]
print(*text)
# Input a text with two words 'Python' and 'Java'
#  Python is popular than Java
# Java is popular than Python


# Napisz program Python, aby znaleźć różnicę pomiędzy największą liczbą całkowitą a najmniejszą liczbą całkowitą, która jest tworzona przez 8 liczb z zakresu od 0 do 9. Numer, który można zmienić, rozpoczyna się od 0, jak w 00135668 r.
# Wejście:
# Dane to sekwencja 8 cyfr (od 0 do 9).
# Wyjście:
# Różnica pomiędzy największą liczbą całkowitą a najmniejszą liczbą całkowitą.
print("Input an integer created by 8 numbers from 0 to 9.:")
num = list(input())
print("Difference between the largest and the smallest integer from the given integer:")
print(int("".join(sorted(num,reverse=True))) - int("".join(sorted(num))))
# Input an integer created by 8 numbers from 0 to 9.:
#  34568729
# Difference between the largest and the smallest integer from the given integer:
# 75308643


# Napisz program Python, aby obliczyć sumę pierwszych n podanych liczb głównych.
# Wejście:
# n ( n ≤ 10000). Wprowadzić 0, aby wyjść z programu.
# Wprowadź liczbę (n ≤10000), aby obliczyć sumę:(0, aby wyjść)
# 25
# Suma pierwszych 25 liczb pierwszych:
# 1060
MAX = 105000
print("Input a number (n≤10000) to compute the sum:(0 to exit)") 
is_prime = [True for _ in range(MAX)]
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX ** (1 / 2)) + 1):
  if is_prime[i]:
    for j in range(i ** 2, MAX, i):
      is_prime[j] = False 
primes = [i for i in range(MAX) if is_prime[i]] 
while True:
  n = int(input())
  if not n:
    break
  print("Sum of first",n,"prime numbers:")
  print(sum(primes[:n]))
# Input a number (n≤10000) to compute the sum:(0 to exit)
#  25
# Sum of first 25 prime numbers:
# 1060


# Napisz program Python, który zaakceptuje liczbę równą (>=4, liczbę Goldbach) od użytkownika i utwórz kombinacje, które wyrażają daną liczbę jako sumę dwóch liczb głównych. Wydrukuj liczbę kombinacji.
# Liczba Goldbach: Liczba Goldbach jest dodatnią nawet liczbą całkowitą, która może być wyrażona jako suma dwóch niedorywczych primów[4] ponieważ cztery jest jedyną liczbą jeszcze większą niż dwie, która wymaga nawet pierwszopi 2, aby być napisana jako suma dwóch primów, Inną formą wypowiedzi przymiotnika Goldbacha jest to, że wszyscy nawet liczni powyżej 4 to liczby Goldbacha.
# Wyrażenie danej liczby nawet jako sumy dwóch primów nazywa się partycją Goldbach tej liczby. Poniżej przedstawiono przykłady partycje Goldbach dla niektórych liczb równych:
# 6 = 3 + 3
# 8 = 3 + 5
# 10 = 3 + 7 = 5 + 5
# 12 = 7 + 5
# ...
# 100 = 3 + 97 = 11 + 89 = 17 + 83 = 29 + 71 = 41 + 59 = 47 + 53
import sys
from bisect import bisect_right
from itertools import chain, compress
print("Input an even number (0 to exit):") 
ub = 50000
is_prime = [0, 0, 1, 1] + [0]*(ub-3)
is_prime[5::6] = is_prime[7::6] = [1]*int(ub/6)
primes = [2, 3]
append = primes.append
 
for n in chain(range(5, ub, 6), range(7, ub, 6)):
    if is_prime[n]:
        append(n)
        is_prime[n*3::n*2] = [0]*((ub-n)//(n*2))
primes.sort()

for n in map(int, sys.stdin):
    if not n:
        break
    if n%2:
        print("Number of combinations:")  
        print(is_prime[n-2])
    else:
        print("Number of combinations:")  
        print(len([1 for p in primes[:bisect_right(primes, n/2)] if is_prime[n-p]]))
# Input an even number (0 to exit):
#  100
# Number of combinations:
# 6


# 54 w przypadku rysowania linii prostej na płaszczyźnie, płaszczyzna jest podzielona na dwa obszary. Na przykład, jeżeli wyciągniesz dwie linie proste równolegle, otrzymasz trzy obszary, a jeśli narysujesz pionowo jeden do drugiego, dostaniesz 4 obszarów.
# Napisz program Python, aby utworzyć maksymalną liczbę regionów uzyskanych przez rysowanie n podanych linii prostych.
while True:
    print("Input number of straight lines (o to exit): ")
    n=int(input())
    if n<=0:
        break
    print("Number of regions:") 
    print((n*n+n+2)//2)
# Input number of straight lines (o to exit): 
#  5
# Number of regions:
# 16