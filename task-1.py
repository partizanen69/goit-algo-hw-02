# Потрібно розробити програму, яка імітує приймання й обробку заявок: програма має автоматично генерувати нові заявки (ідентифіковані унікальним 
# номером або іншими даними), додавати їх до черги, а потім послідовно видаляти з черги для "обробки", імітуючи таким чином роботу сервісного центру.
# Ось псевдокод для завдання з використанням черги (Queue з модуля queue в Python) для системи обробки заявок:

# У цьому псевдокоді використовуються дві основні функції: generate_request(), яка генерує нові заявки та додає їх до черги, та process_request(), яка обробляє 
# заявки, видаляючи їх із черги. Головний цикл програми виконує ці функції, імітуючи постійний потік нових заявок та їх обробку.

from queue import Queue
import time
import random

# Створити чергу заявок
queue = Queue()

# Функція generate_request():
#     Створити нову заявку
#     Додати заявку до черги
def generate_request():
  request = {
    "id": queue.qsize() + 1, 
    "timestamp": time.time()
  }
  queue.put(request)
  print(f"Створено заявку {request['id']}")


# Функція process_request():
#     Якщо черга не пуста:
#         Видалити заявку з черги
#         Обробити заявку
#     Інакше:
#         Вивести повідомлення, що черга пуста
def process_request():
  if not queue.empty():
    request = queue.get()
    print(f"Обробляється заявка: {request}")
    time.sleep(1)
    print(f"Заявку {request['id']} оброблено успішно")
  else:
    print("Черга пуста. Очікування нових заявок...")



# Головний цикл програми:
#     Поки користувач не вийде з програми:
#         Виконати generate_request() для створення нових заявок
#         Виконати process_request() для обробки заявок
if __name__ == "__main__":
  while True:
    random_number = random.randint(1, 10)
    print(f"Створюємо {random_number} заявок")
    print('')
    
    for i in range(random_number):
      generate_request()
      time.sleep(1)

    print("Черга заявок після створення: ", queue.qsize())
    print('')
    
    while not queue.empty():
      process_request()
    
    print("Черга заявок після обробки: ", queue.qsize())
    print('Чекаємо до наступної ітерації...')
    print('')
    time.sleep(5)
