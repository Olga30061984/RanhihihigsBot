# RanhihihigsBot
Telgram bot for ranepa evening education

## Как работать с репозиторием

### Работа с git

`git` — система контроля версий для автоматизированного управления измененями в коде проекта

Основные команды

команда | описание
:-- | :--
git status | состояние изменений в репозитории
git add file1 file2 | добавление файлов в отслеживаемые
git commit -am "Описание задачи, которую решали" | оставить коммит (-a: для всех ранее отслеживаемых файлов ; -m: сообщение коммита) 
git push origin main | отправка изменений в репозиторий
git pull origin main | стягивание изменений с репозитория

### Про декораторы 

попробуйте запустить код

```Python
# Декоратор
import time

# функция обертка - декоратор
def time_check(func):
    def wrapper(*args, **qwargs):
        start = time.monotonic()
        res = func(*args, **qwargs)
        end = time.monotonic() - start
        print("время выполнения:", end)
        return res
    return wrapper


# функция-параметр
# вызов функции-декоратора через @
@time_check
def long_arifmetics(n):
    res = n ** 1000
    return res


if __name__ == "__main__":
    # time_check(long_arifmetics)(n=12)

    # w = time_check(long_arifmetics)
    # w(n=12)
    
    print(long_arifmetics(12))
```
