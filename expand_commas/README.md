`expand_commas.py`
==================
[expand_commas.py](expand_commas.py) reads CSV from standard input and writes
CSV to standard output.

The output is the result of taking the cartesian product implied by any values
that themselves are comma-separated lists.

For example, for the following one-row input
```csv
id,size,color,quantity
1,"small, medium","red, green, blue",8
```
the `id: 1` row would be expanded to `2 * 3 = 6` rows, corresponding to the
six possible combinations of `{small, medium} x {red, green, blue}` for the
`size` and `color` columns.

The output would be
```csv
id,size,color,quantity
1,small,red,8
1,small,green,8
1,small,blue,8
1,medium,red,8
1,medium,green,8
1,medium,blue,8
```

Example Usage
-------------
```console
$ cat example.in.csv
ID,Name,Size,Color,Price,Currency,Quantity
1,Domestic Cat,"small, medium","black, tabby, tuxedo",23.4,EGP,99
2,Domestic Dog,"small, medium, large","brown, black",0.01,USD,10000
3,Fibsh,"small, medium","gray, red",2.5,MXN,4
4,Stone of Jordan,small,gold,1,USD,0

$ ./expand_commas.py <example.in.csv
ID,Name,Size,Color,Price,Currency,Quantity
1,Domestic Cat,small,black,23.4,EGP,99
1,Domestic Cat,small,tabby,23.4,EGP,99
1,Domestic Cat,small,tuxedo,23.4,EGP,99
1,Domestic Cat,medium,black,23.4,EGP,99
1,Domestic Cat,medium,tabby,23.4,EGP,99
1,Domestic Cat,medium,tuxedo,23.4,EGP,99
2,Domestic Dog,small,brown,0.01,USD,10000
2,Domestic Dog,small,black,0.01,USD,10000
2,Domestic Dog,medium,brown,0.01,USD,10000
2,Domestic Dog,medium,black,0.01,USD,10000
2,Domestic Dog,large,brown,0.01,USD,10000
2,Domestic Dog,large,black,0.01,USD,10000
3,Fibsh,small,gray,2.5,MXN,4
3,Fibsh,small,red,2.5,MXN,4
3,Fibsh,medium,gray,2.5,MXN,4
3,Fibsh,medium,red,2.5,MXN,4
4,Stone of Jordan,small,gold,1,USD,0

$ ./expand_commas.py <example.in.csv >example.out.csv
```
