# Multilingual Advent of Code

[**_Advent of Code_**](https://adventofcode.com)
is a great opportunity to brush up on existing languages
and learn some new ones!

<p align="center">
<a href="#prerequisites">Prerequisites</a>
-
<a href="#usage">Usage</a>
-
<a href="#directory-structure">Directory Structure</a>
</p>

## Prerequisites

Docker!

## Usage

```bash
$ ./run.sh
usage: run.sh <language> <problem> <input_type>

arguments:
    language    the programming language
    problem     the day of the problem
    input_type  the type of input file
```

```bash
$ ./dev.sh
usage: dev.sh <language>

arguments:
    language    the programming language
```

## Directory structure

| File / Directory                       | Description                                   |
| -------------------------------------- | --------------------------------------------- |
| `data/<problem>/<input>.in`            | `<input>` for parts 1 and 2 of `<problem>`    |
| `data/<problem>/<input>-1.in`          | `<input>` for part 1 of `<problem>`           |
| `data/<problem>/<input>-2.in`          | `<input>` for part 2 of `<problem>`           |
| `data/<problem>/<expected>-1.expected` | `<expected>` output for part 1 of `<problem>` |
| `data/<problem>/<expected>-2.expected` | `<expected>` output for part 1 of `<problem>` |
| `langs/<language>`                     | Build context and solution for `<language>`   |
| `dev.sh`                               | Multilingual development container launcher   |
| `run.sh`                               | Multilingual solution dispatcher              |
