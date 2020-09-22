# Hangman


[![Build Status](https://img.shields.io/travis/care1e55/hangman/master?style=plastic.png)](https://img.shields.io/travis/care1e55/hangman/master?style=plastic)
[![codecov](https://codecov.io/gh/care1e55/hangman/branch/master/graph/badge.svg)](https://codecov.io/gh/care1e55/hangman)

Консольная версия игры "[Висельница](http://www.robots.ox.ac.uk/~vgg/data/vgg_face2/)"

Протокол общения с пользователем:
```
> Guess a letter:
< a
> Missed, mistake 1 out of 5.
>
> The word: *****
> 
> Guess a letter:
< b
> Missed, mistake 2 out of 5.
> 
> The word: *****
> 
> Guess a letter:
< e
> Hit!
> 
> The word: *e***
> 
> Guess a letter:
< o
> Hit!
>
> The word: *e**o
> 
> Guess a letter:
< l
> Hit!
>
> The word: *ello
> 
> Guess a letter:
< h
> Hit!
>
> The word: hello
>
> You won!
```

Пример проигрыша:
```
> Guess a letter:
< x
> Missed, mistake 1 out of 5.
>
> The word: ******
>
> Guess a letter:
< y
> Missed, mistake 2 out of 5.
>
> The word: ******
>
> Guess a letter:
< z
> Missed, mistake 3 out of 5.
>
> The word: ******
> 
> Guess a letter:
< n
> Hit!
>
> The word: **n*n*
>
> Guess a letter:
< m
> Missed, mistake 4 out of 5.
>
> The word: **n*n*
>
> Guess a letter:
< o
> Missed, mistake 5 out of 5.
>
> The word: **n*n*
>
> You lost!
```

### TODO:
 - [x] README.md
 - [x] LICENSE
 - [x] Декларация сборки и зависимостей
 - [x] Статический анализ стиля кодирования
 - [x] Модульные тесты
 - [x] Настроена непрерывная интеграция
 - [x] Настроено измерение покрытия кода

