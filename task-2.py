# Необхідно розробити функцію, яка приймає рядок як вхідний параметр, 
# додає всі його символи до двосторонньої черги (deque з модуля 
# collections в Python), а потім порівнює символи з обох кінців 
# черги, щоб визначити, чи є рядок паліндромом. Програма повинна 
# правильно враховувати як рядки з парною, так і з непарною кількістю 
# символів, а також бути нечутливою до регістру та пробілів.

from collections import deque

def is_palindrome(string: str) -> bool:
  deque_string = deque(string.lower().replace(" ", "").replace("'", ""))
  
  while len(deque_string) > 1:
    if deque_string.popleft() != deque_string.pop():
      return False
  
  return True

# Test examples
print("Tests:")
print("A man a plan a canal Panama", "--->", is_palindrome("A man a plan a canal Panama") == True)
print("Do geese see God", "--->", is_palindrome("Do geese see God") == True)
print("Madam", "--->", is_palindrome("Madam") == True)
print("radar", "--->", is_palindrome("radar") == True)
print("hello", "--->", is_palindrome("hello") == True)
print("", "--->", is_palindrome("") == True)
print("a", "--->", is_palindrome("a") == True)
print("Race a car", "--->", is_palindrome("Race a car") == True)
print("Was it a car or a cat I saw", "--->", is_palindrome("Was it a car or a cat I saw") == True)
print("лепсспел", "--->", is_palindrome("лепсспел") == True)
