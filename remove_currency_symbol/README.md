`remove_currency_symbol.py`
===========================
[remove_currency_symbol.py](remove_currency_symbol.py) reads CSV from standard
input and writes CSV to standard output.

The transformation removes leading "$" characters from fields that are otherwise
just numeric literals in the current locale.

The script is locale sensitive.  My computer uses an American locale, and so
the decimal point is a period character (".").  Elsewhere in the world, the
decimal point may be a comma character (",").  The convention used by the
script is whichever is the default on the current computer.

In an American locale, the following input:
```csv
ID,Name,Size,Color,Price,Currency,Quantity
4,Stone of Jordan,small,gold,1,USD,0
34,Griswald's Edge,large,silver,$456.33,MXN,1
420,$100 OG,small,green,$67.00,USD,0
```

is transformed into the following output:
```csv
ID,Name,Size,Color,Price,Currency,Quantity
4,Stone of Jordan,small,gold,1,USD,0
34,Griswald's Edge,large,silver,456.33,MXN,1
420,$100 OG,small,green,67.00,USD,0
```

Note how the "$" was removed from "$456.33" and from "$67.00", but _not_ from
"$100 OG".  Without the "$", "100 OG" is not a valid number, even though it
contains a number.

Example Usage
-------------
```console
$ cat example.in.csv
ID,Name,Size,Color,Price,Currency,Quantity
4,Stone of Jordan,small,gold,1,USD,0
34,Griswald's Edge,large,silver,$456.33,MXN,1
420,$100 OG,small,green,$67.00,USD,0

$ ./remove_currency_symbol.py <example.in.csv
ID,Name,Size,Color,Price,Currency,Quantity
4,Stone of Jordan,small,gold,1,USD,0
34,Griswald's Edge,large,silver,456.33,MXN,1
420,$100 OG,small,green,67.00,USD,0

$ ./remove_currency_symbol.py <example.in.csv >example.out.csv
```
