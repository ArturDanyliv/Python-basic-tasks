import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

# Current date and time : 
# 2014-07-05 14:34:14

from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

# Input the radius of the circle : 1.1                                                                          
# The area of the circle with radius 1.1 is: 3.8013271108436504 

fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)

# Input your First Name : Dany                                       
# Input your Last Name : Boon                                        
# Hello  Boon Dany  

values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)

# Input some comma seprated numbers : 3,5,7,23                       
# List :  ['3', '5', '7', '23']                                      
# Tuple :  ('3', '5', '7', '23')          


# Funkcja zwraca listę słów danego ciągu, używając separatora jako ciągu separatora.
# W przypadku wybrania maksplit lista będzie zawierać maksymalnie maksymalnie maksymalnie maksymalnie 1 elementów typu maxsplit+1.
# Jeśli nie określono maksymalnego podziału lub -1, nie ma limitu liczby podziałów.
# Jeśli podano SEP, kolejne separatory nie są pogrupowane razem i uważa się, że wytyczają granice pustych ciągów.
# Argument SEP może składać się z wielu znaków.
# Dzielenie pustego ciągu z określonym separatorem zwraca [''].
 
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))

# Input the Filename: abc.java                                                                                  
# The  extension of the file is : 'java'


# Zapisz program Python, aby wyświetlić pierwszy i ostatni kolor z poniższej listy.
# Color_list = [„czerwony”, „zielony”, „biały” ,„czarny”]

color_list = ["Red","Green","White" ,"Black"]
print( "%s %s"%(color_list[0],color_list[-1]))

# Red Black


# Zapisz program Python, aby wyświetlić harmonogram badania. (wyodrębnij datę z exam_st_date).
# exam_st_date = (11, 12, 2014)
# Próbka wyjściowa: Badanie rozpocznie się od: 11 / 12 / 2014

exam_st_date = (11,12,2014)
print( "The examination will start from : %i / %i / %i"%exam_st_date)

# The examination will start from : 11 / 12 / 2014


# Funkcja zwraca obiekt całkowity zbudowany z liczby lub ciągu x lub zwraca 0, jeśli nie podano żadnych argumentów. Jeśli x jest liczbą, zwróć x.__int__(). W przypadku liczb zmiennoprzecinkowych jest to skraca się do zera.

# 1. Jeśli x nie jest liczbą lub jeśli podana jest baza, x musi być ciągiem, bajtami lub przypadkiem porozdartym reprezentującym dosłowną liczbę całkowitą w bazie radixu
# 2. Dosłowny może być poprzedzony znakiem + lub - (bez spacji pomiędzy) i otoczony przez whitespace
# 3. Dosłowny „Base-n” składa się z cyfr od 0 do n-1, z A do z (lub A do z) o wartościach od 10 do 35. Domyślna baza to 10.
# 4. Dopuszczalne wartości to 0 i 2-36. Base-2, -8, i -16 literały mogą być opcjonalnie wstępnie ustalone z 0b/0B, 0o/0O lub 0x/0X, jak z liczbą całkowitą litrals w kodzie.

a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)

# 615 

# Napisz program Python, aby wydrukować dokumenty (składnia, opis itp.) z wbudowanych funkcji Pythona.
# Funkcja próbki: abs()
# Ciąg dokowania Pythona:
# Ciąg docstring to literał tekstowy, który występuje jako pierwsze stwierdzenie w definicji modułu, funkcji, klasy lub metody. Taki ciąg docstring staje się specjalnym atrybutem __doc__ tego obiektu.
# Wszystkie moduły powinny normalnie mieć docstrings, a wszystkie funkcje i klasy eksportowane przez moduł powinny również mieć docstrings. Metody publiczne (w tym konstruktor __init__) powinny również posiadać stacje dokujące.

print(abs.__doc__)

# Return the absolute value of the argument


# Napisz program Python, aby wydrukować kalendarz danego miesiąca i roku.
# Uwaga: Użyj modułu „Kalendarium”.

import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))

# # 


# # 
print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")

# #

# #
from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)

# 9


# Napisz program Python, aby uzyskać objętość kuli o promieniu 6.

pi = 3.1415926535897931
r= 6.0
V= 4.0/3.0*pi* r**3
print('The volume of the sphere is: ',V)

# The volume of the sphere is:  904.7786842338603


# Napisz program Python, aby sprawdzić, czy liczba mieści się w zakresie 100 z 1000 lub 2000.
# Funkcja zwraca wartość bezwzględną liczby. Argument może być liczbą całkowitą lub liczbą zmiennoprzecinkową. Jeżeli argument jest liczbą złożoną, jego wielkość jest zwracana.

def near_thousand(n):
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))   
print(near_thousand(2200))

# True                                                                                                          
# True                                                                                                          
# False                                                                                                         
# False 


# Napisz program Python, aby obliczyć sumę trzech podanych liczb, jeśli wartości są równe, a następnie zwróć trzykrotnie ich sumę.

def sum_thrice(x, y, z):

     sum = x + y + z
  
     if x == y == z:
      sum = sum * 3
     return sum

print(sum_thrice(1, 2, 3))
print(sum_thrice(3, 3, 3))

# 6
# 27


# Napisz program Python, aby pobrać nowy ciąg z danego ciągu, w którym „IS” został dodany do przodu. Jeśli dany ciąg zaczyna się już od „IS”, zwróć go bez zmian.
def new_string(str):
  if len(str) >= 2 and str[:2] == "Is":
    return str
  return "Is" + str

print(new_string("Array"))
print(new_string("IsEmpty"))

# IsArray                                                                                                       
# IsEmpty

# Napisz program Python, aby otrzymać ciąg, który jest n (nie-ujemną liczbą całkowitą) kopii danego ciągu.
def larger_string(str, n):
   result = ""
   for i in range(n):
      result = result + str
   return result

print(larger_string('abc', 2))
print(larger_string('.py', 3))

# abcabc                                                                                                        
# .py.py.py 

# Napisz program Python, aby sprawdzić, czy dany numer (zaakceptowanie przez użytkownika) jest równy czy nietypowy, wydrukuj odpowiedni komunikat dla użytkownika.

num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")

# Enter a number: 5                                                                                             
# This is an odd number


# Napisz program Python, aby policzyć liczbę 4 na danej liście.
def list_count_4(nums):
  count = 0  
  for num in nums:
    if num == 4:
      count = count + 1

  return count

print(list_count_4([1, 4, 6, 7, 4]))
print(list_count_4([1, 4, 6, 4, 7, 4]))

# 2 
# 3


# Napisz program Python, aby otrzymać n (nie-ujemną liczbę całkowitą) pierwszych 2 znaków danego ciągu. Zwróć n kopie całego ciągu, jeśli jego długość jest mniejsza niż 2.
def substring_copy(str, n):
  flen = 2
  if flen > len(str):
    flen = len(str)
  substr = str[:flen]
  
  result = ""
  for i in range(n):
    result = result + substr
  return result
print(substring_copy('abcdef', 2))
print(substring_copy('p', 3))

# abab                                                                                                          
# ppp


# Napisz program Python, aby sprawdzić, czy zaliczona litera jest samogłoską czy nie.
def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(is_vowel('c'))
print(is_vowel('e'))

# False                                                                                                         
# True 


# Napisz program Python, aby sprawdzić, czy określona wartość jest zawarta w grupie wartości.
# Test Data: 
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

def is_group_member(group_data, n):
   for value in group_data:
       if n == value:
           return True
   return False
print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([5, 8, 3], -1))

# True
# False


# Zapisz program Python, aby utworzyć histogram z danej listy liczb całkowitych.
def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)

histogram([2, 3, 6, 5])

# **                                                                                                            
# ***                                                                                                           
# ******                                                                                                        
# *****


# Napisz program Python, aby złączyć wszystkie elementy z listy w ciąg i zwrócić go.
def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result

print(concatenate_list_data([1, 5, 12, 2]))

# 15122

# Zapisz program Python, aby wydrukować wszystkie równe liczby z danej listy numerów w tej samej kolejności i zatrzymać drukowanie, jeśli w sekwencji pojawiają się liczby po 237.
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

for x in numbers:
    if x == 237:
        print(x)
        break;
    elif x % 2 == 0:
        print(x)
		

# 386                                                                                                           
# 462                                                                                                           
# 418                                                                                                           
# 344                                                                                                           
# 236                                                                                                           
# 566                                                                                                           
# 978                                                                                                           
# 328                                                                                                           
# 162                                                                                                           
# 758                                                                                                           
# 918  
# 237              


# Zapisz program Python, aby wydrukować zestaw zawierający wszystkie kolory z color_list_1, które nie występują w color_list_2.

# Dane testu:
# Color_list_1 = Set([„White”, „Black”, „Red”])
# Color_list_2 = Set([„Red”, „Green”])
# Spodziewany wynik:
# {'Black', 'White'}

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print("Original set elements:")
print(color_list_1)
print(color_list_2)
print("\nDifferenct of color_list_1 and color_list_2:")
print(color_list_1.difference(color_list_2))
print("\nDifferenct of color_list_2 and color_list_1:")
print(color_list_2.difference(color_list_1))

# Original set elements:
# {'White', 'Black', 'Red'}
# {'Green', 'Red'}

# Differenct of color_list_1 and color_list_2:
# {'White', 'Black'}

# Differenct of color_list_2 and color_list_1:
# {'Green'}

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print("Original set elements:")
print(color_list_1)
print(color_list_2)
print("\nDifferenct of color_list_1 and color_list_2:")
print(color_list_1 - color_list_2)
print("\nDifferenct of color_list_2 and color_list_1:")
print(color_list_2 - color_list_1)

# Original set elements:
# {'White', 'Black', 'Red'}
# {'Green', 'Red'}

# Differenct of color_list_1 and color_list_2:
# {'White', 'Black'}

# Differenct of color_list_2 and color_list_1:
# {'Green'}


# Napisz program Python, który zaakceptuje podstawę i wysokość trójkąta i obliczy obszar.
# Python: Obszar trójkąta
# Trójkąt jest wielobokiem z trzema krawędziami i trzema szczytami. It jest jednym z podstawowych kształtów w geometrii. Trójkąt z szczytami A, B i C jest oznaczony trójkątem ABC.
# Vertex trójkąta: Punkt, w którym spotykają się dwie strony trójkąta.
# Wysokość trójkąta: Prostopadły segment od szczytu trójkąta do linii zawierającej przeciwzdo.
# Podstawa trójkąta: Strona trójkąta, do której rysowana jest wysokość.
# Wysokość trójkąta: Długość wysokości.

b = int(input("Input the base : "))
h = int(input("Input the height : "))

area = b*h/2

print("area = ", area)

# Input the base : 20                                                                                           
# Input the height : 40                                                                                         
# area =  400.0


# Napisz program Python, aby obliczyć największe wspólne podziały (GCD) dwóch pozytywnych liczb całkowitych.
# Największy wspólny podziały (GCD) dwóch niezerowych liczb całkowitych a i b jest największą dodatnią liczbą całkowitą d taką, że d jest podziałem zarówno a, jak i b; oznacza to, że istnieją liczby całkowite e i f takie, że a = de i b = df, a d jest największą liczbą całkowitą. GCD w lit. a) i b jest ogólnie oznaczane jako gcd(a, b).

def gcd(x, y):
   gcd = 1   
   if x % y == 0:
       return y   
   for k in range(int(y / 2), 0, -1):
       if x % k == 0 and y % k == 0:
           gcd = k
           break 
   return gcd
print("GCD of 12 & 17 =",gcd(12, 17))
print("GCD of 4 & 6 =",gcd(4, 6))
print("GCD of 336 & 360 =",gcd(336, 360))

# GCD of 12 & 17 = 1
# GCD of 4 & 6 = 2
# GCD of 336 & 360 = 24

def gcd(x, y):
 z = x % y
 while z:
   x = y
   y = z
   z = x % y
 return y
print("GCD of 12 & 17 =",gcd(12, 17))
print("GCD of 4 & 6 =",gcd(4, 6))
print("GCD of 336 & 360 =",gcd(336, 360))

# GCD of 12 & 17 = 1
# GCD of 4 & 6 = 2
# GCD of 336 & 360 = 24


# Napisz program Python, aby zsumować trzy podane liczby całkowite. Jeśli jednak dwie wartości są równe sumie, wartość będzie równa zero.

def sum_three(x, y, z):
    if x == y or y == z or x==z:
        sum = 0
    else:
        sum = x + y + z
    return sum
print(sum_three(2, 1, 2))
print(sum_three(3, 2, 2))
print(sum_three(2, 2, 2))
print(sum_three(1, 2, 3))

# 0
# 0
# 0
# 6


# Napisz program Python, aby zsumować dwóch podanych liczb całkowitych. Jeśli jednak suma mieści się w przedziale od 15 do 20, to zwróci się 20.

def sum(x, y):
    sum = x + y
    if sum in range(15, 20):
        return 20
    else:
        return sum

print(sum(10, 6))
print(sum(10, 2))
print(sum(10, 12))

# 20                                                                                                            
# 12                                                                                                            
# 22 


# Zapisz program Python, który zwróci wartość True, jeśli dwie podane wartości całkowite są równe lub ich suma lub różnica wynosi 5.

def test_number5(x, y):
   if x == y or abs(x-y) == 5 or (x+y) == 5:
       return True
   else:
       return False
print(test_number5(7, 2))
print(test_number5(3, 2))
print(test_number5(2, 2))
print(test_number5(7, 3))
print(test_number5(27, 53))

# True
# True
# True
# False
# False

# Zapisz program Python, aby dodać dwa obiekty, jeśli oba obiekty są typu całkowitego.
def add_numbers(a, b):
   if not (isinstance(a, int) and isinstance(b, int)):
       return "Inputs must be integers!"
   return a + b
print(add_numbers(10, 20))
print(add_numbers(10, 20.23))
print(add_numbers('5', 6))
print(add_numbers('5', '6'))

# 30
# Inputs must be integers!
# Inputs must be integers!
# Inputs must be integers!


# Napisz program Python, aby wyświetlić swoje dane, takie jak imię i nazwisko, wiek, adres w trzech różnych wierszach.

def personal_details():
    name, age = "Simon", 19
    address = "Bangalore, Karnataka, India"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

personal_details()

# Name: Simon                                                                                                   
# Age: 19                                                                                                       
# Address: Bangalore, Karnataka, India


# Napisz program Python do rozwiązania (x + y) * (x + y).
# Dane testu: X = 4, y = 3
# Spodziewany wynik: (4 + 3) ^ 2) = 49

x, y = 4, 3
result = x * x + 2 * x * y + y * y
print("({} + {}) ^ 2) = {}".format(x, y, result))

# (4 + 3) ^ 2) = 49 


# Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.
# The formula for future value with compound interest is FV = P(1 + r/n)^nt.
# FV = the future value;
# P = the principal;
# r = the annual interest rate expressed as a decimal;
# n = the number of times interest is paid each year;
# t = time in years.
# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79

amt = 10000
int = 3.5
years = 7
future_value = amt*((1+(0.01*int)) ** years)
print(round(future_value,2))

# 12722.79


# Zapisz program Python, aby obliczyć odległość pomiędzy punktami (x1, y1) i (x2, y2).
import math
p1 = [4, 0]
p2 = [6, 6]
distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

print(distance)

# 6.324555320336759


# Napisz program Python, aby sprawdzić, czy plik istnieje.
import os.path
print(os.path.isfile('main.txt'))
print(os.path.isfile('main.py'))

# False
# True


# Napisz program Python, aby ustalić, czy powłoka Pythona jest uruchamiana w trybie 32-bitowym czy 64-bitowym w systemie operacyjnym.

# For 32 bit it will return 32 and for 64 bit it will return 64
import struct
print(struct.calcsize("P") * 8)

# 64 


# Napisz program Python, aby uzyskać nazwę systemu operacyjnego, platformę i informacje o wersji.
# os.name: Nazwa importowanego modułu zależnego od systemu operacyjnego. Obecnie zarejestrowano następujące nazwy: „posix”, „nt”, „java”.
# Platform.system(): Zwraca nazwę systemu operacyjnego, na którym działa.
# Platform.release(): Zwraca wersję systemu operacyjnego.

import platform
import os
print("Name of the operating system:",os.name)
print("\nName of the OS system:",platform.system())
print("\nVersion of the operating system:",platform.release())

# Name of the operating system: posix

# Name of the OS system: Linux

# Version of the operating system: 4.4.0-197-generic


# Napisz program Python, aby zlokalizować pakiety Python site-packages.
# Site.getsitepackages(): Zwraca listę zawierającą wszystkie globalne foldery pakietów site-packages.

import site; 
print(site.getsitepackages())

# ['/usr/local/lib/python3.5/dist-packages', '/usr/lib/python3/dist-packages', '/usr/lib/python3.5/dist-packages']


# Napisz program Python, aby wywołać polecenie zewnętrzne.
from subprocess import call
call(["ls", "-l"])

# drwxrwxr-x 2 students  students    4096 Sep 15  2016 c48d5200-7b43-11e6-b7e4-2516b8e1f7f8                     
# drwxrwxr-x 2 students  students    4096 Sep 21  2016 c4a96850-7fdf-11e6-a2b3-172481646809                     
# drwxrwxr-x 2 students  students    4096 Sep  7  2016 c4d98410-74de-11e6-ac36-65f2f75d0c7b                     
# drwxrwxr-x 2 students  students    4096 Sep  6  2016 c4fa6e10-7424-11e6-812c-5574d751e2d7                     
# drwxrwxr-x 2 prashanta prashanta   4096 Feb 20 18:24 c5216400-f76b-11e6-8ad1-9b7f6e755728   
# -------
# -rw-rw-r-- 1 students  students      27 Sep 28  2016 temp.txt                                                 
# -rw-rw-r-- 1 students  students      27 Sep 28  2016 test.txt 

import os
print(os.system('ls -l'))
# total 4
# -rw-rw-rw- 1 root root 36 Jun  9 10:47 main.py
# 0 


# Napisz program Python, aby uzyskać ścieżkę i nazwę aktualnie realizowanego pliku.
import os
print("Current File Name : ",os.path.realpath(__file__))
# Current File Name :  /home/students/fb6e28e0-2425-11e7-807b-bd9de91b1602.py


# Napisz program Python, aby dowiedzieć się, ile procesorów używa.
import multiprocessing
print(multiprocessing.cpu_count())
# 4


# Napisz program Python, aby przeanalizować ciąg znaków w pozycji Float lub Integer.
n = "246.2458"
print(float(n))
print(int(float(n)))

# 246.2458                                                                                                      
# 246


# Napisz program Python, aby drukować bez spacji i newline.
for i in range(0, 10):
    print('*', end="")
print("\n")
# **********

for i in range(0, 10):
    print('Artur jest zajbisty \n --> \t TAK \t', end="")
print("\n")
# Artur jest zajbisty 
#1. -->     TAK    Artur jest zajbisty 
#2. -->     TAK    Artur jest zajbisty 
#3. -->     TAK    Artur jest zajbisty 
#4. -->     TAK    Artur jest zajbisty 
#5. -->     TAK    Artur jest zajbisty 
#6. -->     TAK    Artur jest zajbisty 
#7. -->     TAK    Artur jest zajbisty 
#8. -->     TAK    Artur jest zajbisty 
#9. -->     TAK 

# Napisz program Python, aby określić profilowanie programów Pythona.
# Uwaga: Profil jest zestawem statystyk opisujących częstotliwość i czas wykonywania różnych części programu. Statystyki te można sformatować w raportach za pomocą modułu pstats.
import cProfile
def sum():
    print(1+2)
cProfile.run('sum()')

# 3                                                                                                             
#        5 function calls in 0.000 seconds                                                                    
                                                                                                              
#   Ordered by: standard name                                                                                  
                                                                                                              
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)                                       
#        1    0.000    0.000    0.000    0.000 7aa14930-2430-11e7-807b-bd9de91b1602.py:2(sum)                  
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)                                            
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}                                 
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}                                
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}  



# Napisz program Python, aby uzyskać dostęp do zmiennych środowiskowych.
import os
# Access all environment variables 
print('*----------------------------------*')
print(os.environ)
print('*----------------------------------*')
# Access a particular environment variable 
print(os.environ['HOME'])
print('*----------------------------------*')
print(os.environ['PATH'])
print('*----------------------------------*')

# *----------------------------------*                                                                          
#environ({'LESSOPEN': '| /usr/bin/lesspipe %s', '_': '/usr/bin/timeout', 'LIBVIRT_DEFAULT_URI': 'qemu:///system
#', 'HOME': '/home/students', 'TERM': 'xterm-256color', 'SHELL': '/bin/bash', 'SHLVL': '2', 'USER': 'students',
# 'MAIL': '/var/mail/students', 'COMP_WORDBREAKS': ' \t\n"\'><;|&(:', 'PATH': '/usr/local/bin:/usr/bin:/bin:/us
#r/local/games:/usr/games', 'LANG': 'en_US.UTF-8', 'LOGNAME': 'students', 'LS_COLORS': 'rs=0:di=01;34:ln=01;36:
#mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42
#:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;3
#1:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.d
#z=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;
#31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:
#*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.jpg=01;35:*.jpeg=01;35:*.gif=01;35:*.
#bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.p
#ng=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.m
#kv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wm
#v=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01
#;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36
#:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:
#*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:', 'JAVA_HOME': '/usr/lib/jvm/java-7-openjdk-amd
#64/jre/bin/java', 'LESSCLOSE': '/usr/bin/lesspipe %s %s', 'PWD': '/home/students'})                           
#*----------------------------------*                                                                          
#/home/students                                                                                                
#*----------------------------------*                                                                          
#/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games                                                      
#*----------------------------------*  


# Napisz program Python, aby uzyskać bieżącą nazwę użytkownika.
import getpass
print(getpass.getuser())
# trinket


# Napisz Pythona, aby znaleźć lokalne adresy IP przy użyciu stdlib Pythona.
import socket
print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] 
if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), 
s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, 
socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
# 192.168.0.200       bbnbnbnbnbbbbbbbbbbbbbbbbb
#   bbnbnbnbnbbbbbbbbbbbbbbbbb
#xbbnbnbnbnbbbbbbbbbbbbbbbbb

# Napisz program Python, aby uzyskać wysokość i szerokość okna konsoli.
def terminal_size():
    import fcntl, termios, struct
    th, tw, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    return tw, th

print('Number of columns and Rows: ',terminal_size())
# Number of columns and Rows:  (110, 21)


# Napisz program Python, aby uzyskać czas wykonania (w sekundach) dla metody Pythona.


# Napisz program Python, aby uzyskać czas wykonania (w sekundach) dla metody Pythona.
import time
def sum_of_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1,n+1):
        s = s + i
    end_time = time.time()
    return s,end_time-start_time

n = 5
print("\nTime to sum of 1 to ",n," and required time to calculate is :",sum_of_n_numbers(n))

# Time to sum of 1 to  5  and required time to calculate is : (15, 2.384185791015625e-06) 


# Napisz program Python, aby zsumować pierwszych n pozytywnych liczb całkowitych.
n = int(input("Input a number: "))
sum_num = (n * (n + 1)) / 2
print("Sum of the first", n ,"positive integers:", sum_num)

# Input a number:  2
# Sum of the first 2 positive integers: 3.0


# Napisz program Python, aby przeliczyć wysokość (w stopach i w centymetrach) na centymetry.
print("Input your height: ")
h_ft = int(input("Feet: "))
h_inch = int(input("Inches: "))

h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 1)

print("Your height is : %d cm." % h_cm)

# Input your height: 
# Feet:  5
# Inches:  3
# Your height is : 160 cm.


# Napisz program Python, aby przeliczyć odległość (w stopach) na cale, jardy i mile.
d_ft = int(input("Input distance in feet: "))
d_inches = d_ft * 12
d_yards = d_ft / 3.0
d_miles = d_ft / 5280.0

print("The distance in inches is %i inches." % d_inches)
print("The distance in yards is %.2f yards." % d_yards)
print("The distance in miles is %.2f miles." % d_miles)

# Input distance in feet: 100                                                                                   
# The distance in inches is 1200 inches.                                                                        
# The distance in yards is 33.33 yards.                                                                         
# The distance in miles is 0.02 miles.


# Napisz program Python, aby przekształcić wszystkie jednostki czasu w sekundy.
days = int(input("Input days: ")) * 3600 * 24
hours = int(input("Input hours: ")) * 3600
minutes = int(input("Input minutes: ")) * 60
seconds = int(input("Input seconds: "))

time = days + hours + minutes + seconds

print("The  amounts of seconds", time)

# Input days:  4
# Input hours:  5
# Input minutes:  20
# Input seconds:  10
# The  amounts of seconds 364810


# Napisz program Python, aby uzyskać bezwzględną ścieżkę pliku.
def absolute_file_path(path_fname):
        import os
        return os.path.abspath('path_fname')        
print("Absolute file path: ",absolute_file_path("test.txt"))

# Absolute file path:  /home/students/path_fname 

from pathlib import Path
p = Path("main.py").resolve()
print(p)

# /tmp/sessions/9f576d81597fd882/main.py


# Napisz program Python, aby uzyskać datę/godziny utworzenia pliku i modyfikacji.
import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime("test.txt")))
print("Created: %s" % time.ctime(os.path.getctime("test.txt")))

# Last modified: Wed Apr 19 11:36:23 2017                                                                       
# Created: Wed Apr 19 11:36:23 2017 


# Napisz program Python, aby zamienić sekundy na dzień, godzinę, minuty i sekundy.
time = float(input("Input time in seconds: "))
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))

# Input time in seconds: 1234565                                                                                
# d:h:m:s-> 14:6:56:5


# Napisz program Python, aby obliczyć indeks masy ciała.
height = float(input("Input your height in Feet: "))
weight = float(input("Input your weight in Kilogram: "))
print("Your body mass index is: ", round(weight / (height * height), 2))

# Input your height in Feet:  6
# Input your weight in Kilogram:  65
# Your body mass index is:  1.81


# Napisz program Pythona, aby przeliczyć ciśnienie w kilopaskali na funty na cal kwadratowy, milimetr rtęci (mmHg) i ciśnienie atmosferyczne.
kpa = float(input("Input pressure in in kilopascals> "))
psi = kpa / 6.89475729
mmhg = kpa * 760 / 101.325
atm = kpa / 101.325
print("The pressure in pounds per square inch: %.2f psi"  % (psi))
print("The pressure in millimeter of mercury: %.2f mmHg" % (mmhg))
print("Atmosphere pressure: %.2f atm." % (atm))

# Input pressure in in kilopascals> 12.35                                                                       
# The pressure in pounds per square inch: 1.79 psi                                                              
# The pressure in millimeter of mercury: 92.63 mmHg                                                             
# Atmosphere pressure: 0.12 atm.


# Napisz program Python, aby obliczyć sumę cyfr numeru.
num = int(input("Input a four digit numbers: "))
x  = num //1000
x1 = (num - x*1000)//100
x2 = (num - x*1000 - x1*100)//10
x3 = num - x*1000 - x1*100 - x2*10
print("The sum of digits in the number is", x+x1+x2+x3)

# Input a four digit numbers: 5245                                                                              
# The sum of digits in the number is 16


# Napisz program Python, aby posortować trzy liczby całkowite bez użycia warunkowych instrukcji i pętli.
x = int(input("Input first number: "))
y = int(input("Input second number: "))
z = int(input("Input third number: "))

a1 = min(x, y, z)
a3 = max(x, y, z)
a2 = (x + y + z) - a1 - a3
print("Numbers in sorted order: ", a1, a2, a3)

# Input first number: 2                                                                                         
# Input second number: 4                                                                                        
# Input third number: 5                                                                                         
# Numbers in sorted order:  2 4 5


# Napisz program Python, aby posortować pliki według daty.
import glob
import os

files = glob.glob("*.txt")
files.sort(key=os.path.getmtime)
print("\n".join(files))

# result.txt
# temp.txt
# myfile.txt
# mynewtest.txt
# mytest.txt
# abc.txt
# test.txt 


# Napisz program Python, aby uzyskać listę katalogów posortowanych według daty utworzenia.
from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time

#Relative or absolute path to the directory
dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'

#all entries in the directory w/ stats
data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
data = ((os.stat(path), path) for path in data)

# regular files, insert creation date
data = ((stat[ST_CTIME], path)
           for stat, path in data if S_ISREG(stat[ST_MODE]))

for cdate, path in sorted(data):
    print(time.ctime(cdate), os.path.basename(path))
	

# Mon Feb 22 16:11:49 2016 .bash_logout                                                                         
# Mon Feb 22 16:11:49 2016 .bashrc                                                                              
# Mon Feb 22 16:11:49 2016 .profile                                                                             
# Mon May 30 11:45:34 2016 .mysql_history                                                                       
# Sat Aug 13 11:37:48 2016 logging_example.out                                                                  
# Tue Sep 13 10:56:31 2016 result.txt                                                                           
# Tue Sep 20 18:00:14 2016 dddd.txt        
# -------
# Tue Apr 18 15:06:27 2017 abc.txt                                                                              
# Wed Apr 19 13:46:47 2017 .bash_history                                                                        
# Wed Apr 19 15:15:52 2017 test.txt                                                                             
# Wed Apr 19 16:58:20 2017 4ab8fe20-24f3-11e7-afe4-85767fd0ee52.py  

import os
import time
paths = ["%s %s" % (time.ctime(t),f) for t, f in
sorted([(os.path.getctime(x),x) for x in os.listdir(".")])]
print("Directory listing, sorted by creation date:")
for x in range(len(paths)):
    print(paths[x],)
	
# Directory listing, sorted by creation date:
# Mon May 31 13:29:45 2021 main.py


# Napisz program Python, aby uzyskać szczegółowe informacje o module matematycznym.
# Imports the math module
import math            
#Sets everything to a list of math module
math_ls = dir(math) # 
print(math_ls)

# ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'at
# an2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'fact
# orial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isn
# an', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh',
# 'sqrt', 'tan', 'tanh', 'trunc']  

import math
print("Details of math module:\n")
help(math)


# Napisz program Python, aby obliczyć punkty środkowe linii.
print('\nCalculate the midpoint of a line :')

x1 = float(input('The value of x (the first endpoint) '))
y1 = float(input('The value of y (the first endpoint) '))

x2 = float(input('The value of x (the first endpoint) '))
y2 = float(input('The value of y (the first endpoint) '))

x_m_point = (x1 + x2)/2
y_m_point = (y1 + y2)/2
print();
print("The midpoint of line is :")
print( "The midpoint's x value is: ",x_m_point)
print( "The midpoint's y value is: ",y_m_point)
print();

# Calculate the midpoint of a line :                                                                            
# The value of x (the first endpoint) 2                                                                         
# The value of y (the first endpoint) 2                                                                         
# The value of x (the first endpoint) 4                                                                         
# The value of y (the first endpoint) 4                                                                                                                                                       
# The midpoint of line is :                                                                                     
# The midpoint's x value is:  3.0                                                                               
# The midpoint's y value is:  3.0


# Napisz program Python, aby hash słowo.
soundex=[0,1,2,3,0,1,2,0,0,2,2,4,5,5,0,1,2,6,2,3,0,1,0,2,0,2]
 
word=input("Input the word be hashed: ")
 
word=word.upper()
 
coded=word[0]
 
for a in word[1:len(word)]:
    i=65-ord(a)
    coded=coded+str(soundex[i])
print() 
print("The coded word is: "+coded)
print()

# Input the word be hashed: w3r                                                                                 
# The coded word is: W02


# Napisz program Python, aby uzyskać informacje o prawach autorskich i napisać informacje o prawach autorskich w kodzie Pythona.
import sys
print("\nPython Copyright Information")
print(sys.copyright)
print()

# Python Copyright Information                                                                                  
# Copyright (c) 2001-2016 Python Software Foundation.                                                           
# All Rights Reserved.                                                                                          
                                                                                                              
# Copyright (c) 2000 BeOpen.com.                                                                                
# All Rights Reserved.                                                                                          
                                                                                                              
# Copyright (c) 1995-2001 Corporation for National Research Initiatives.                                        
# All Rights Reserved.                                                                                          
                                                                                                              
# Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.                                            
# All Rights Reserved. 

print("Python copyright information:\n")
print(copyright)

# To samo 

__author__ = "Software Authors Name"
__copyright__ = "Copyright (C) 2004 Author Name"
__license__ = "Public Domain"
__version__ = "1.0"
print("copyright information in Python code:\n")

# copyright information in Python code:


# Napisz program Python, aby uzyskać argumenty wiersza poleceń (nazwę skryptu, liczbę argumentów, argumenty) przekazane do skryptu.
import sys
print("This is the name/path of the script:"),sys.argv[0]
print("Number of arguments:",len(sys.argv))
print("Argument List:",str(sys.argv))

#  prashanta@server:~$ python test.py arg1 arg2 arg3

# This is the name/path of the script: test.py
# ('Number of arguments:', 4)
# ('Argument List:', "['test.py', 'arg1', 'arg2', 'arg3']")


# Napisz program Python, aby sprawdzić, czy system jest platformą big-endian czy małą platformą.
# sys.byteorder: Wskaźnik pierwotnej kolejności bajtów. Będzie to miało wartość „duży” na dużych platformach (najważniejszy bajt pierwszy) i „mały” na platformach o małym (najmniej znaczącym bajcie pierwszy).

import sys
print()
if sys.byteorder == "little":
    #intel, alpha
    print("Little-endian platform.")
else:
    #motorola, sparc
    print("Big-endian platform.")
print()

# Little-endian platform


# Napisz program Python, aby znaleźć dostępne wbudowane moduły.
import sys
import textwrap
module_name = ', '.join(sorted(sys.builtin_module_names))
print(textwrap.fill(module_name, width=70))

# _ast, _bisect, _codecs, _collections, _datetime, _elementtree,                                                
# _functools, _heapq, _imp, _io, _locale, _md5, _operator, _pickle,                                             
# _posixsubprocess, _random, _sha1, _sha256, _sha512, _signal, _socket,                                         
# _sre, _stat, _string, _struct, _symtable, _thread, _tracemalloc,                                              
# _warnings, _weakref, array, atexit, binascii, builtins, errno,                                                
# faulthandler, fcntl, gc, grp, itertools, marshal, math, posix, pwd,                                           
# pyexpat, select, spwd, sys, syslog, time, unicodedata, xxsubtype,                                             
# zipimport, zlib


# Zapisz program Python, aby uzyskać rozmiar obiektu w bajtach.
import sys
str1 = "one"
str2 = "four"
str3 = "three"
x = 0
y = 112
z = 122.56
print("Size of ",str1,"=",str(sys.getsizeof(str1))+ " bytes")
print("Size of ",str2,"=",str(sys.getsizeof(str2))+ " bytes")
print("Size of ",str3,"=",str(sys.getsizeof(str3))+ " bytes")
print("Size of",x,"=",str(sys.getsizeof(x))+ " bytes")
print("Size of" ,y,"="+str(sys.getsizeof(y))+ " bytes")
L = [1, 2, 3, 'Red', 'Black']
print("Size of",L,"=",sys.getsizeof(L)," bytes")
T = ("Red", [8, 4, 6], (1, 2, 3))
print("Size of",T,"=",sys.getsizeof(T)," bytes")
S = {'apple', 'orange', 'apple', 'pear'}
print("Size of",S,"=",sys.getsizeof(S)," bytes")
D = {'Name': 'David', 'Age': 6, 'Class': 'First'}
print("Size of",D,"=",sys.getsizeof(S)," bytes")

# Size of  one = 52 bytes
# Size of  four = 53 bytes
# Size of  three = 54 bytes
# Size of 0 = 24 bytes
# Size of 112 =28 bytes
# Size of [1, 2, 3, 'Red', 'Black'] = 104  bytes
# Size of ('Red', [8, 4, 6], (1, 2, 3)) = 72  bytes
# Size of {'orange', 'pear', 'apple'} = 224  bytes
# Size of {'Name': 'David', 'Age': 6, 'Class': 'First'} = 224  bytes


# Napisz program Python, aby uzyskać aktualną wartość limitu rekurencji.
# sys.getrecursionlimit(): Zwraca bieżącą wartość limitu rekursji, maksymalną głębokość stosu interpretera Pythona. Ten limit zapobiega nieograniczonej rekursji powodującej przepełnienie stosu C i awarii Pythona. It można ustawić przez setrecursionlimit().
import sys
print()
print("Current value of the recursion limit:")
print(sys.getrecursionlimit())
print()

# Current value of the recursion limit:                                                                         
# 1000

import sys
print("Call sys.getrecursionlimit() to get the current recursion limit:")
recursion_limit = sys.getrecursionlimit()
print(recursion_limit)
print("\nCall sys.setrecursionlimit(n) to change the recursion limit to n operations:")
sys.setrecursionlimit(1001)
new_recursion_limit = sys.getrecursionlimit()
print(new_recursion_limit)

# Call sys.getrecursionlimit() to get the current recursion limit:
# 1000
# Call sys.setrecursionlimit(n) to change the recursion limit to n operations:
# 1001


# Napisz program Python, aby złączyć N struny. 
list_of_colors = ['Red', 'White', 'Black']  
colors = '-'.join(list_of_colors)
print()
print("All Colors: "+colors)
print()

# All Colors: Red-White-Black


# Napisz program Python, aby obliczyć sumę wszystkich elementów kontenera (krotka, lista, zestaw, słownik).
# Niektóre obiekty zawierają odniesienia do innych obiektów; są one nazywane kontenerami. Ogólnie rzecz biorąc, kontenery umożliwiają dostęp do zawartych obiektów i ich iterację. Przykładami kontenerów są listy, zestawy, pule i słowniki.
s = sum([10,20,30])
print("\nSum of the container: ", s)
print()

# Sum of the container:  60


# Napisz program Python, aby sprawdzić, czy wszystkie numery listy są większe od określonej liczby.
num = [2, 3, 4, 5]
print()
print(all(x > 1 for x in num))
print(all(x > 4 for x in num))
print()
# True
# False


def test(nums, n):
   return(all(x > n for x in nums))      
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Original list numbers:")
print(nums)
n = 12
print("\nCheck whether all numbers of the said list greater than",n)
print(test(nums, n))
n = 5
print("\nCheck whether all numbers of the said list greater than",n)
print(test(nums, n))

# Original list numbers:
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Check whether all numbers of the said list greater than 12
# False
# Check whether all numbers of the said list greater than 5
# True


# Napisz program Python, aby policzyć liczbę wystąpień określonego znaku w ciągu.
s = "The quick brown fox jumps over the lazy dog."  
print("Original string:")
print(s)
print("Number of occurrence of 'o' in the said string:")
print(s.count("o"))

# Original string:
# The quick brown fox jumps over the lazy dog.
# Number of occurrence of 'o' in the said string:
# 4


s = "The quick brown fox jumps over the lazy dog."  
print("Original string:")
print(s)
print("Number of occurrence of 'o' in the said string:")
ctr = 0 
for c in s:
   if c == 'o':
       ctr = ctr + 1
print(ctr)

# Original string:
# The quick brown fox jumps over the lazy dog.
# Number of occurrence of 'o' in the said string:
# 4


# Napisz program Python, aby sprawdzić, czy ścieżka pliku jest plikiem, czy też katalogu.
import os  
path="abc.txt"  
if os.path.isdir(path):  
    print("\nIt is a directory")  
elif os.path.isfile(path):  
    print("\nIt is a normal file")  
else:  
    print("It is a special file (socket, FIFO, device file)" )
print()
# It is a normal file  


# Napisz program Python, aby uzyskać rozmiar pliku.
import os
file_size = os.path.getsize("abc.txt")
print("\nThe size of abc.txt is :",file_size,"Bytes")
print()
# The size of abc.txt is : 0 Bytes

import os
file_size = os.stat('main.py')
print("\nThe size of abc.txt is :",file_size.st_size,"Bytes")
# The size of abc.txt is : 104 Bytes

import os
file = open('main.py')
file.seek(0, os.SEEK_END)
print("The size of main.py is :", file.tell(), "bytes")
# The size of main.py is : 117 bytes


# Podane zmienne x=30 i y=20, zapisz program Pythona, aby wydrukować „30+20=50”.
x = 30
y = 20
print("\n%d+%d=%d" % (x, y, x+y))
print()
# 30+20=50

x = 30
y = 20
print("{0}+{1}={2}".format(x, y, x+y))
# 30+20=50

x = 30
y = 20
print("{}+{}={}".format(x, y, x + y))
# 30+20=50


# Napisz program Python, aby wykonać działanie, jeśli warunek jest prawdziwy.
# Jeśli podana jest nazwa zmiennej, jeśli wartość wynosi 1, należy wyświetlić ciąg „pierwszy dzień miesiąca!”. i nie rób nic, jeśli wartość nie jest równa.
n=1
if n == 1:
   print("\nFirst day of a Month!")
print()
# First day of a Month! 

n = float(input("Input a number: "))
if (n == 1):
   print("First day of a Month!")
else:
   print()
# Input a number:  1
# First day of a Month!


# Napisz program Python, aby utworzyć kopię własnego kodu źródłowego. 
def file_copy(src, dest):
    with open(src) as f, open(dest, 'w') as d:
        d.write(f.read())
        file_copy("untitled0.py", "z.py")
        with open('z.py', 'r') as filehandle:
            for line in filehandle:
                print(line, end = '')

# def file_copy(src, dest):
#    with open(src) as f, open(dest, 'w') as d:
#        d.write(f.read())
#        file_copy("untitled0.py", "z.py")
#        with open('z.py', 'r') as filehandle:
#            for line in filehandle:
#                print(line, end = '')


# Napisz program Python, aby zamienić dwie zmienne.
# Zamiana dwóch zmiennych odnosi się do wzajemnej wymiany wartości zmiennych. Zazwyczaj odbywa się to z danymi w pamięci.

# Najprostszą metodą wymiany dwóch zmiennych jest użycie trzeciej zmiennej tymczasowej :
# zdefiniuj swap(a, b)
# temp := a
# a := b
# b := temp
a = 30
b = 20
print("\nBefore swap a = %d and b = %d" %(a, b))
a, b = b, a
print("\nAfter swaping a = %d and b = %d" %(a, b))
print()
# Before swap a = 30 and b = 20
# After swaping a = 20 and b = 30


#Napisz program Python, aby uzyskać nazwę hosta, na którym uruchomiona jest procedura.
import socket
host_name = socket.gethostname()
print("Host name:", host_name)
# Host name: 0c299cb8f897

import platform
host_name = platform.uname()[1]
print("Host name:", host_name )
# Host name: 4735090b6baa

import os
host_name = os.uname().nodename
print("Host name:", host_name)
# Host name: 0c299cb8f897


# Napisz program Python, aby uzyskać wynik polecenia systemowego.
import subprocess
# file and directory listing
returned_text = subprocess.check_output("dir", shell=True, universal_newlines=True)
print("dir command to list file and directory")
print(returned_text)
# 6d2c5fa0-5ef2-11e6-8ff4-d5b1b3f27f4d  ead74d50-beb7-11e6-933b-47978
# 84c7124                                                            
# 6d33f7a0-242d-11e7-820d-03f0e944369f  eae8e560-767d-11e6-a3fc-0fb5e
# bee9d44                                                            
# 6d36f6e0-8616-11e6-affa-0dc8296ec630  eafedbe0-ed01-11e6-a189-7956f
# 7e10ca1                                                            
# 6d462c20-758e-11e6-a935-b7db6295ac51  eb190a30-bae6-11e6-a2d1-75a31
# a870ce2  
# ------
# 7feae620-bece-11e6-ad81-456cada677e8  sss.dat\n                    
# 7fef9710-7fc2-11e6-97c3-c153b6e0fe23  temp.txt                     
# 7ff17310-9c22-11e6-9e03-95cb39e2a59d  test.txt                     
# 801a70f0-4414-11e6-a0ac-5bb3315a1c3b                                                          


# Zapisz program Python, aby wyodrębnić nazwę pliku z danej ścieżki.
import os
print()
print(os.path.basename('/users/system1/student1/homework-1.py'))
print()
# homework-1.py 


# Napisz program Python, aby uzyskać efektywny identyfikator grupy, efektywny identyfikator użytkownika, rzeczywisty identyfikator grupy, listę dodatkowych identyfikatorów grup powiązanych z bieżącym procesem.
import os
print("\nEffective group id: ",os.getegid())
print("Effective user id: ",os.geteuid())
print("Real group id: ",os.getgid())
print("List of supplemental group ids: ",os.getgroups())
print()
# Effective group id:  1007                                          
# Effective user id:  1006                                           
# Real group id:  1007                                               
# List of supplemental group ids:  [1007]


# Napisz program Python, aby podzielić ścieżkę na separator rozszerzeń.
import os.path
for path in [ 'test.txt', 'filename', '/user/system/test.txt', '/', '' ]:
    print('"%s" :' % path, os.path.splitext(path))
# "test.txt" : ('test', '.txt')                                      
# "filename" : ('filename', '')                                      
# "/user/system/test.txt" : ('/user/system/test', '.txt')            
# "/" : ('/', '')                                                    
# "" : ('', '')


# Zapisz program Python, aby pobrać właściwości pliku.
import os.path
import time

print('File         :', __file__)
print('Access time  :', time.ctime(os.path.getatime(__file__)))
print('Modified time:', time.ctime(os.path.getmtime(__file__)))
print('Change time  :', time.ctime(os.path.getctime(__file__)))
print('Size         :', os.path.getsize(__file__))
# File         : 8dbacd90-266d-11e7-a9c1-cf681af3cdf1.py             
# Access time  : Fri Apr 21 14:06:03 2017                            
# Modified time: Fri Apr 21 14:06:02 2017                            
# Change time  : Fri Apr 21 14:06:02 2017                            
# Size         : 304


# Zapisz program Python, aby znaleźć ścieżkę, odnosi się do pliku lub katalogu, gdy pojawi się nazwa ścieżki.
import os.path

for file in [ __file__, os.path.dirname(__file__), '/', './broken_link']:
    print('File        :', file)
    print('Absolute    :', os.path.isabs(file))
    print('Is File?    :', os.path.isfile(file))
    print('Is Dir?     :', os.path.isdir(file))
    print('Is Link?    :', os.path.islink(file))
    print('Exists?     :', os.path.exists(file))
    print('Link Exists?:', os.path.lexists(file))
# File        : 26cb6a20-266f-11e7-a9c1-cf681af3cdf1.py              
# Absolute    : False                                                
# Is File?    : True                                                 
# Is Dir?     : False                                                
# Is Link?    : False                                                
# Exists?     : True                                                 
# Link Exists?: True  
# ------
# Is Dir?     : False                                                
# Is Link?    : False                                                
# Exists?     : False                                                
# Link Exists?: False 


# Zapisz program Python, aby sprawdzić, czy liczba jest dodatnia, ujemna lub zerowa.
# Liczby dodatnie: Każda liczba powyżej zera jest znana jako liczba dodatnia. Liczby dodatnie są zapisywane bez znaku lub znaku „+” przed nimi i są zliczane od zera, tj. 1, + 2, 3, +4 itd.
# Liczby ujemne: Dowolna liczba poniżej zera jest określana jako liczba ujemna. Liczby ujemne są zawsze zapisywane ze znakiem "-" przed nimi i są zliczane od zera, tj. od -1, -2, -3, -4 itd.
# Zawsze należy zwracać uwagę na znak przed cyfrą, aby sprawdzić, czy jest dodatni czy ujemny. Zero, 0, nie jest ani dodatnie, ani ujemne.
num = float(input("Input a number: "))
if num > 0:
   print("It is positive number")
elif num == 0:
   print("It is Zero")
else:
   print("It is a negative number")
# Input a number: 150                                                
# It is positive number   


# Napisz program Python, aby otrzymać liczby podzielne przez piętnastu z listy za pomocą funkcji anonimowej.
num_list = [45, 55, 60, 37, 100, 105, 220]
# use anonymous function to filter
result = list(filter(lambda x: (x % 15 == 0), num_list))
print("Numbers divisible by 15 are",result)
# Numbers divisible by 15 are [45, 60, 105]

num_list = [45, 55, 60, 37, 100, 105, 220]
print("Original list:",num_list)
# use anonymous function to filter
result = list(filter(lambda x: (x % 15 == 0), num_list))
print("Numbers of the said list divisible by 15 are:",result)
# Original list: [45, 55, 60, 37, 100, 105, 220]
# Numbers of the said list divisible by 15 are: [45, 60, 105]


# Zapisz program Python, aby utworzyć listy plików z bieżącego katalogu przy użyciu symbolu wieloznacznego.
import glob
file_list = glob.glob('*.*')
print(file_list)
#Specific files
print(glob.glob('*.py'))
print(glob.glob('./[0-9].*'))
# ['main.py']
# ['main.py']
# []


from pathlib import Path
for path in Path("/").glob("*.*"):
   print(path)
# /.dockerenv 


# Zapisz program Python, aby usunąć pierwszy element z określonej listy.
color = ["Red", "Black", "Green", "White", "Orange"]
print("Original list elements:")
print(color)
del color[0]
print("After removing the first color:")
print(color)
# Original list elements:
# ['Red', 'Black', 'Green', 'White', 'Orange']
# After removing the first color:
# ['Black', 'Green', 'White', 'Orange']


color = ["Red", "Black", "Green", "White", "Orange"]
print("Original list elements:")
print(color)
print("\nAfter removing the first element from the said list:")
new_color = color[1:]
print(new_color)
# Original list elements:
# ['Red', 'Black', 'Green', 'White', 'Orange']
# After removing the first element from the said list:
# ['Black', 'Green', 'White', 'Orange']


color = ["Red", "Black", "Green", "White", "Orange"]
print("Original list elements:")
print(color)
print("\nAfter removing the first element from the said list:")
color.remove("Red")
print(color)
# Original list elements:
# ['Red', 'Black', 'Green', 'White', 'Orange']
# After removing the first element from the said list:
# ['Black', 'Green', 'White', 'Orange']


def tail(lst):
  return lst[1:] if len(lst) > 1 else lst
print(tail([1, 2, 3, 4]))
print(tail([1]))
print(tail(["Red", "Black", "Green", "White", "Orange"]))
# [2, 3, 4]
# [1]
# ['Black', 'Green', 'White', 'Orange']

x = [10,1,1,20,3,50,45,5,6]
print(max(*x))
# 50

import itertools
def lister(*x):
    for i in x:
        print(i, end="|")

n = [10,1,1,20,35,75,40,5,6]
lister(*n)
# 10|1|1|20|35|75|40|5|6|


# Zapisz program Python, aby wprowadzić numer, jeśli nie jest to numer generuje komunikat o błędzie.
while True:
    try:
        a = int(input("Input a number: "))
        break
    except ValueError:
        print("\nThis is not a number. Try again...")
        print()
# Input a  number: abc                                                                                          
# This is not a number.  Try again...                                                                                                                                                                                 
# Input a  number: 150

x = 1.23
x_int = x.is_integer()
print("Check if x is an integer!")
print(x_int)
y= 1.0
y_int = y.is_integer()
print("Check if y is an integer!")
print(y_int)  
# Check if x is an integer!
# False
# Check if y is an integer!
# True

x = 1.0
x_int = isinstance(x, int)
print("Check if x is an integer!")
print(x_int)
y = 1
y_int = isinstance(y, int)
print("Check if y is an integer!")
print(y_int)
# Check if x is an integer!
# False
# Check if y is an integer!
# True


# Napisz program Python, aby filtrować liczby dodatnie z listy.
# Liczby dodatnie: Każda liczba powyżej zera jest znana jako liczba dodatnia. Liczby dodatnie są zapisywane bez znaku lub znaku „+” przed nimi i są zliczane od zera, tj. 1, + 2, 3, +4 itd.
nums = [34, 1, 0, -23, 12, -88]
print("Original numbers in the list: ",nums)
new_nums = list(filter(lambda x: x >0, nums))
print("Positive numbers in the said list: ",new_nums)
# riginal numbers in the list:  [34, 1, 0, -23, 12, -88]
# Positive numbers in the said list:  [34, 1, 12]

nums = [34, 1, 0, -23, 12, -88]
print("Original numbers in the list: ",nums)
print("Positive numbers in the said list: ")
for pos_nums in nums:
   if pos_nums > 0:
      print(pos_nums, end = " ")
# Original numbers in the list:  [34, 1, 0, -23, 12, -88]
# Positive numbers in the said list: 
# 34 1 12 

nums = [34, 1, 0, -23, 12, -88]
print("Original numbers in the list: ",nums)
pos_nums = [n for n in nums if n> 0]
print("Positive numbers in the said list: ",*pos_nums)
# Original numbers in the list:  [34, 1, 0, -23, 12, -88]
# Positive numbers in the said list:  34 1 12


# Napisz program Python, aby obliczyć produkt listy liczb całkowitych (bez użycia dla pętli).
from functools import reduce
nums = [10, 20, 30,]
print("Original list numbers:")
print(nums)
nums_product = reduce( (lambda x, y: x * y), nums)
print("\nProduct of the said numbers (without using for loop):",nums_product)
# Original list numbers:
# [10, 20, 30]
# Product of the numbers :  6000

import math
 # Python version 3.9.
nums = [10, 20, 30,]
print("Original list numbers:")
print(nums)
nums_product = math.prod(nums)
print("\nProduct of the said numbers (without using for loop):",nums_product)
# Original list numbers:
# [10, 20, 30]
# Product of the numbers :  6000


# Napisz program Python, aby wydrukować znaki Unicode.
str = u'\u0050\u0079\u0074\u0068\u006f\u006e \u0045\u0078\u0065\u0072\u0063\u0069\u0073\u0065\u0073 \u002d \u0077\u0033\u0072\u0065\u0073\u006f\u0075\u0072\u0063\u0065'
print()
print(str)
print()
# Python Exercises - w3resource


# Zapisz program Python, aby udowodnić, że dwie zmienne tekstowe o tej samej wartości wskazują tę samą lokalizację pamięci.
str1 = "Python"
str2 = "Python"
 
print("\nMemory location of str1 =", hex(id(str1)))
print("Memory location of str2 =", hex(id(str2)))
print()
# Memory location of str1 = 0x7f8af3e89f10                                                                      
# Memory location of str2 = 0x7f8af3e89f10


# Napisz program Python, aby utworzyć obejście z listy.
print()
nums = [10, 20, 56, 35, 17, 99]
# Create bytearray from list of integers.
values = bytearray(nums)
for x in values: print(x)
print()
# 10                                                                                                            
# 20                                                                                                            
# 56                                                                                                            
# 35                                                                                                            
# 17                                                                                                            
# 99


# Zapisz program Python, aby zaokrąglić liczbę zmiennoprzecinkową do określonej liczby miejsc po przecinku.
order_amt = 212.374
print('\nThe total order amount comes to %f' % order_amt)
print('The total order amount comes to %.2f' % order_amt)
print()
# The total order amount comes to 212.374000
# The total order amount comes to 212.37

order_amt = 212.374
print("\nThe total order amount comes to {:0.6f}".format(order_amt))
print("\nThe total order amount comes to {:0.2f}".format(order_amt))
# The total order amount comes to 212.374000
# The total order amount comes to 212.37


# Napisz program Python, aby sformatować określony ciąg ograniczający długość ciągu.
str_num = "1234567890"
print("Original string:",str_num)
print('%.6s' % str_num)
print('%.9s' % str_num)
print('%.10s' % str_num)
# Original string: 1234567890
# 123456
# 123456789
# 1234567890


# Napisz program Python, aby określić, czy zmienna jest zdefiniowana, czy nie.
try:
  x = 1
except NameError:
  print("Variable is not defined....!")
else:
  print("Variable is defined.")
try:
  y
except NameError:
  print("Variable is not defined....!")
else:
  print("Variable is defined.")
# Variable is defined.                                                                                          
# Variable is not defined....! 


# Napisz program Python, aby opróżnić zmienną bez jej niszczenia.
# type() zwraca typ obiektu, który wywołany tworzy nową wartość 'pustą'.
# Przykładowe dane: n=20
# d = {„x”:200}
# Spodziewany rezultat: 0
# {}
n = 20
d = {"x":200}
l = [1,3,5]
t= (5,7,8)
print(type(n)())
print(type(d)())
print(type(l)())
print(type(t)())
# 0
# {}
# []
# ()

def Empty_Var(lst):
   return [type(i)() for i in lst]
lst = ["python",{"x":12},[10,12,"sfsd"], (4,5), 200]
print("Original objects:")
print(lst)
print("\nEmpty the said variables without destroying it:")
print(Empty_Var(lst))
# Original objects:
# ['python', {'x': 12}, [10, 12, 'sfsd'], (4, 5), 200]
# Empty the said variables without destroying it:
# ['', {}, [], (), 0]


# Napisz program Python, aby określić największe i najmniejsze liczby całkowite, longi, pływaki.
import sys
print("Float value information: ",sys.float_info)
print("\nInteger value information: ",sys.int_info)
print("\nMaximum size of an integer: ",sys.maxsize) 
# Float value information: sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250
# 738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2
# , rounds=1)                                                                                                   
# Integer value information: sys.int_info(bits_per_digit=30, sizeof_digit=4)                                                                                                                                                 
# Maximum size of an integer: 9223372036854775807 


# Napisz program Python, aby sprawdzić, czy wiele zmiennych ma tę samą wartość.
x = 20
y = 20
z = 20
if x == y == z == 20:
    print("All variables have same value!")  
# All variables have same value! 

def multiple_variables_equality(*vars):
   for x in vars:
       if x != vars[0]:
           return "All variables have not same value."
   return "All variables have same value."
print(multiple_variables_equality(2,3,2,2,2,2))
print(multiple_variables_equality(10,10,10,10))
print(multiple_variables_equality(-3,-3,-3,-3))  
# All variables have not same value.
# All variables have same value.
# All variables have same value


# Napisz program Python, aby zsumować wszystkie liczniki w zbiorach.
import collections
num = [2,2,4,6,6,8,6,10,4]
print(sum(collections.Counter(num).values()))
# 9

nums = [2,2,4,6,6,8,6,10,4]
print(len(nums))
# 9


# Napisz program Python, aby uzyskać rzeczywisty obiekt modułu dla danego obiektu.
from inspect import getmodule
from math import sqrt
print(getmodule(sqrt))
# <module 'math' (built-in)>

import inspect
def add(x, y):
    return x + y
print(inspect.getmodule(add))
# <module '__main__' from '/tmp/sessions/5ced515afe46d808/main.py'>


# Napisz program Python, aby sprawdzić, czy liczba całkowita mieści się w 64 bitach.
int_val = 30
if int_val.bit_length() <= 63:
    print((-2 ** 63).bit_length())
    print((2 ** 63).bit_length())
# 64                                                                                                            
# 64


# Napisz program Python, aby sprawdzić, czy w ciągu występują małe litery.
str1 = 'A8238i823acdeOUEI'
print(any(c.islower() for c in str1))
# True 

def lower_case_str(text):
   ctr = 0
   for char in text:
       if(ord(char) >= 97 and ord(char) <= 122):
           ctr = ctr + 1
   if (ctr>0):
       return True
str1 = 'A8238i823acdeOUEI'
print("Original string:",str1)
print("Lowercase letters exist in the said string: ",lower_case_str(str1))
str1 = 'PYTHON'
print("\nOriginal string:",str1)
print("Lowercase letters exist in the said string: ",lower_case_str(str1))
str1 = 'javascript'
print("\nOriginal string:",str1)
print("Lowercase letters exist in the said string: ",lower_case_str(str1))
# Check if all input alphabets are small!

# Original string: A8238i823acdeOUEI
# Lowercase letters exist in the said string:  False
# Original string: PYTHON
# Lowercase letters exist in the said string:  False
# Original string: javascript
# Lowercase letters exist in the said string:  True


# Napisz program Python, aby dodać zera początkowe do ciągu.
str1='122.22'
print("Original String: ",str1)
print("\nAdded trailing zeros:")
str1 = str1.ljust(8, '0')
print(str1)
str1 = str1.ljust(10, '0')
print(str1)
print("\nAdded leading zeros:")
str1='122.22'
str1 = str1.rjust(8, '0')
print(str1)
str1 = str1.rjust(10, '0')
print(str1)
# Original String:  122.22
# Added trailing zeros:
# 122.2200
# 122.220000
# Added leading zeros:
# 00122.22
# 0000122.22

str1='122.22'
print("Original String: ",str1)
print("\nAdded trailing zeros:")
f_text = '{:<08}'
str1 = f_text.format(str1)
print(str1)
f_text = '{:<010}'
str1 = f_text.format(str1)
print(str1)
print("\nAdded leading zeros:")
str1='122.22'
f_text = '{:>08}'
str1 = f_text.format(str1)
print(str1)
f_text = '{:>010}'
str1 = f_text.format(str1)
print(str1)
# Original String:  122.22
# Added trailing zeros:
# 122.2200
# 122.220000
# Added leading zeros:
# 00122.22
# 0000122.22


# Napisz program Python, aby użyć podwójnych wycen do wyświetlania ciągów.
import json
print(json.dumps({'Alex': 1, 'Suresh': 2, 'Agnessa': 3}))
# {"Agnessa": 3, "Alex": 1, "Suresh": 2}


# Napisz program Python, aby podzielić ciąg o zmiennej długości na zmienne.
var_list = ['a', 'b', 'c']
x, y, z = (var_list + [None] * 3)[:3]
print(x, y, z)
var_list = [100, 20.25]
x, y = (var_list + [None] * 2)[:2]
print(x, y)
# a b c                                                                                                         
# 100 20.25 

var_list = ['a', 'b', 'c', 'd', 'e']
v, w, x, y, z = var_list
print(v, w, x, y, z)
# a b c d e


# Zapisz program Python, aby wyświetlić katalog domowy bez ścieżki bezwzględnej.
import os.path
print(os.path.expanduser('~'))
# /home/students


# Zapisz program Python, aby obliczyć czas trwania programu (różnicę między czasem rozpoczęcia a bieżącym).
from timeit import default_timer
def timer(n):
    start = default_timer()
    # some code here
    for row in range(0,n):
        print(row)
    print(default_timer() - start)

timer(5)
timer(15)
# 0                                                                                                             
# 1                                                                                                             
# 2                                                                                                             
# 3                                                                                                             
# 4                                                                                                             
# 2.6107000849151518e-05                                                                                        
# 0                                                                                                             
# 1                                                                                                             
# 2                                                                                                             
# 3                                                                                                             
# 4                                                                                                             
# 5                                                                                                             
# 6                                                                                                             
# 7                                                                                                             
# 8                                                                                                             
# 9                                                                                                             
# 10                                                                                                            
# 11                                                                                                            
# 12                                                                                                            
# 13                                                                                                            
# 14                                                                                                            
# 4.1371999941475224e-05


# Zapisz program Python, aby wprowadzić dwa liczby całkowite w jednej linii.
print("Input the value of x & y")
x, y = map(int, input().split())
print("The value of x & y are: ",x,y)
# Input the value of x & y
# 2 4
# The value of x & y are:  2 4

a, b = [int(a) for a in input("Input the value of a & b: ").split()]
print("The value of a & b are:",a,b)
# Input the value of a & b:  2 4
# The value of a & b are: 2 4


# Napisz program Python, aby wydrukować zmienną bez spacji pomiędzy wartościami.
x = 30
print('Value of x is "{}"'.format(x))
# Value of x is "30" 


# Napisz program Python, aby znaleźć pliki i pominąć katalog danego katalogu.
import os
print([f for f in os.listdir('/home/students') if os.path.isfile(os.path.join('/home/students', f))])
# ['test.txt', '.mysql_history', '.bash_logout', '.bash_history', '.profile', 'abc.py', '.viminfo', 'mynewtest.t
# xt', 'myfile.txt', 'logging_example.out', '.web-term.json', 'abc.txt', '64a57280-272f-11e7-9ce4-832a8e030fef.p
# y', 'exercise.cs', '.bashrc', 'Example.cs', 'myfig.png', 'file.out', 'line.gif', 'mmm.txt\n', 'temp.txt', 'ddd
# d.txt\n', 'sss.dat\n', 'result.txt', 'output.jpg', '26492-1274250701.png', 'mytest.txt'] 

import os
user_path = 'd:/'
for fname in os.listdir(user_path):
   path = os.path.join(user_path, fname)
   if os.path.isdir(path):
       # skip directories
       continue
   # print the file names
   print(fname)
# ....


# Zapisz program Python, aby wyodrębnić parę klucz-wartość słownika w zmiennych.
d = {'Red': 'Green'}
(c1, c2), = d.items()
print(c1)
print(c2)
# Red                                                                                                           
# Green   

dict = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'key4': 'val4'}
print("Extract specific key, value")
x, y = list(dict.items())[0]
print(x, y)
x, y = list(dict.items())[3]
print(x, y)
# Extract specific key, value
# key1 val1
# key4 val4

# Napisz program Python, aby przekonwertować True na 1 i false na 0.
x = 'true'
x = int(x == 'true')
print(x)
x = 'abcd'
x = int(x == 'true')
print(x)
# 1                                                                                                             
# 0


# Napisz program Python, aby przekonwertować liczbę całkowitą na binarną zera wiodące.
# Konwersja liczby całkowitej na liczbę binarną n-bitową powoduje, że jej reprezentacja binarna zawiera zera prowadzące do długości n. na przykład, aby przekształcić liczbę całkowitą 5 na 6-bitową liczbę binarną w 000101.
# format(num, name) funkcja z nazwą "0nb" do konwersji liczby całkowitej na ciąg binarny z zerami wiodącymi do długości n.
# Dane próbki: X=12
# Oczekiwana wydajność: 00001100
# 0000001100
x = 12
print(format(x, '08b'))
print(format(x, '010b'))
# 00001100
# 0000001100


# Zapisz program Python, aby przeliczyć liczbę miejsc po przecinku na liczbę szesnastkową.
x = 30
print(format(x, '02x'))
x = 4
print(format(x, '02x'))
# 1e                                                                                                            
# 04

def dechimal_to_Hex(n):   
   x = (n % 16)
   ch = ""
   if (x < 10):
       ch = x
   if (x == 10):
       ch = "A"
   if (x == 11):
       ch = "B"
   if (x == 12):
       ch = "ch"
   if (x == 13):
       ch = "D"
   if (x == 14):
       ch = "E"
   if (x == 15):
       ch = "F"
   if (n - x != 0):
       return dechimal_to_Hex(n // 16) + str(ch)
   else:
       return str(ch)
dechimal_nums = [0, 15, 30, 55, 355, 656, 896, 1125]
print("Dechimal numbers:")
print(dechimal_nums)
print("\nHexadechimal numbers of the said dechimal numbers:")
print([dechimal_to_Hex(x) for x in dechimal_nums])
# Dechimal numbers:
# [0, 15, 30, 55, 355, 656, 896, 1125]

# Hexadechimal numbers of the said dechimal numbers:
# ['0', 'F', '1E', '37', '163', '290', '380', '465']


# Napisz program Python, aby ustalić, czy powłoka Pythona jest uruchamiana w trybie 32-bitowym czy 64-bitowym w systemie operacyjnym.
import struct
print(struct.calcsize("P") * 8)
# 64 


# Napisz program Python, aby sprawdzić, czy zmienna jest liczbą całkowitą czy ciągiem.
print(isinstance(25,int) or isinstance(25,str))
print(isinstance([25],int) or isinstance([25],str))
print(isinstance("25",int) or isinstance("25",str))
# True                                                                    
# False                                                                   
# True


# Zapisz program Python, aby sprawdzić, czy zmienna jest listą, czy też jedną lub zestawem.
#x = ['a', 'b', 'c', 'd']
#x = {'a', 'b', 'c', 'd'}
x = ('tuple', False, 3.2, 1)
if type(x) is list:
    print('x is a list')
elif type(x) is set:
    print('x is a set')
elif type(x) is tuple:
    print('x is a tuple')    
else:
    print('Neither a list or a set or a tuple.')
# x is a tuple

def check_type(nums):
    if isinstance(x, tuple)==True:
        return 'The variablex is a tuple'
    elif isinstance(x, list)==True:
        return 'The variablex is a list'
    elif isinstance(x, set)==True:
        return 'The variablex is a set'
    else:
        return 'Neither a list or a set or a tuple.'
x = ['a', 'b', 'c', 'd']
print(check_type(x))
x = {'a', 'b', 'c', 'd'}
print(check_type(x))
x = ('tuple', False, 3.2, 1)
print(check_type(x))
x = 100
print(check_type(x))
# The variablex is a list
# The variablex is a set
# The variablex is a tuple
# Neither a list or a set or a tuple.


# Napisz program Python, aby znaleźć lokalizację źródeł modułu Python.
import imp
print("Location of Python os module sources:")
print(imp.find_module('os'))
print("\nLocation of Python sys module sources:")
print(imp.find_module('datetime'))
# Location of Python os module sources:
# (<_io.TextIOWrapper name='/usr/lib/python3.6/os.py' mode='r' encoding='utf-8'>, '/usr/lib/python3.6/os.py', ('.py', 'r', 1))
# Location of Python sys module sources:
# (<_io.TextIOWrapper name='/usr/lib/python3.6/datetime.py' mode='r' encoding='utf-8'>, '/usr/lib/python3.6/datetime.py', ('.py', 'r', 1))

import os
print("\nList of directories in os module:")
print(os.path)
print("\nList of directories in sys module:")
import sys
print(sys.path)
# List of directories in os module:
# <module 'posixpath' from '/usr/lib/python3.6/posixpath.py'>
# List of directories in sys module:
# ['/tmp/sessions/9ab477032ea1081a', '/trinket/python3', '/usr/lib/python36.zip', '/usr/lib/python3.6', '/usr/lib/python3.6/lib-dynload', '/usr/local/lib/python3.6/dist-packages', '/usr/lib/python3/dist-packages']


# Zapisz funkcję Pythona, aby sprawdzić, czy liczba jest podzielna przez inną liczbę. Użytkownik może zaakceptować dwie wartości liczby całkowite.
def multiple(m, n):
	return True if m % n == 0 else False

print(multiple(20, 5))
print(multiple(7, 2))
# True
# False


# Zapisz funkcję Python, aby znaleźć maksymalną i minimalną liczbę z sekwencji liczb.
# Uwaga: Nie używaj wbudowanych funkcji.
def max_min(data):
  l = data[0]
  s = data[0]
  for num in data:
    if num> l:
      l = num
    elif num< s:
        s = num
  return l, s

print(max_min([0, 10, 15, 40, -5, 42, 17, 28, 75]))
# (75, -5)


# Zapisz funkcję Python, która przyjmuje dodatnią liczbę całkowitą i zwraca sumę sześcianu wszystkich dodatnich liczb całkowitych mniejszą niż określona liczba.
# Przykład: 8 = 73+63+53+43+33+23+13 = 784
def sum_of_cubes(n):
 n -= 1
 total = 0
 while n > 0:
   total += n * n * n
   n -= 1
 return total
print("Sum of cubes smaller than the specified number: ",sum_of_cubes(3))
# Sum of cubes smaller than the specified number:  9


# Zapisz funkcję Python, aby sprawdzić, czy w sekwencji wartości całkowitych występuje różna para liczb, których produkt jest nietypowy.
def odd_product(nums):
  for i in range(len(nums)):
    for j in range(len(nums)):
      if  i != j:
        product = nums[i] * nums[j]
        if product & 1:
          return True
  return False          
dt1 = [2, 4, 6, 8]
dt2 = [1, 6, 4, 7, 8]
dt3 = [1, 3, 5, 7, 9]
print(dt1, odd_product(dt1));
print(dt2, odd_product(dt2));
print(dt3, odd_product(dt3));
# [2, 4, 6, 8] False
# [1, 6, 4, 7, 8] True
# [1, 3, 5, 7, 9] True

import itertools
def pair_nums_odd(nums):
    uniquelist = set(nums)
    result =[]
    for n in itertools.combinations(uniquelist, 2):
        if ((n[0] * n[1]) % 2 == 1):
            temp = str(n[0]) + " * " + str(n[1])
            result.append(temp)
    return result
          
dt1 = [2, 4, 6, 8]
print("Original sequence:")
print(dt1)
print("Distinct pair of numbers whose product is odd present in the said sequence:") 
print(pair_nums_odd(dt1));
dt2 = [1, 6, 4, 7, 8]
print("\nOriginal sequence:")
print(dt2)
print("Distinct pair of numbers whose product is odd present in the said sequence:") 
print(pair_nums_odd(dt2));
dt3 = [1, 3, 5, 7, 9]
print("\nOriginal sequence:")
print(dt3)
print("Distinct pair of numbers whose product is odd present in the said sequence:") 
print(pair_nums_odd(dt3));
# Original sequence:
# [2, 4, 6, 8]
# Distinct pair of numbers whose product is odd present in the said sequence:
# []

# Original sequence:
# [1, 6, 4, 7, 8]
# Distinct pair of numbers whose product is odd present in the said sequence:
# ['1 * 7']
# Original sequence:
# [1, 3, 5, 7, 9]
# Distinct pair of numbers whose product is odd present in the said sequence:
# ['1 * 3', '1 * 5', '1 * 7', '1 * 9', '3 * 5', '3 * 7', '3 * 9', '5 * 7', '5 * 9', '7 * 9']

