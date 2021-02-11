- Analyzujte dataset informací o vínech.
- Zjistěte co nejvíce informací o tomto datasetu.
- V notebooku by měl být zřejmý postup analýzy.  
- Využijte textové buňky, kam zjištené informace zapíšete. (Tak ať tomu rozumím a počtu si). 
- Připravte dataset pro další použití pro ML.

- ✓ správné typy
- ✓ stringy tokenizovat -> frekvenční analýza, z top četných udělám sloupce
- ✓ stejné jednotky
- ✓ odstranit outliery (3násobek směrodatné odchylky)
- ✓ nulové / nedefinované hodnoty
    - odstranit / doplnit    
- logaritmus / odmocnina
- k-nearest neighbours - pro dopočítání chybějících hodnot
- rozložení
    - odstranit / doplnit -> abych měl správné rozložení
- ✓ duplikáty (nechat / odstranit)
- ✓ vysvětlit sloupce
- obrázky převést na pole barev
- ✓ histogram / ✓ bar chart / ✓ stacked bar chart
- binning
- self organizing map

Run notebook:
`python -m notebook`

In statistics, **standardization** is the process of putting different variables on the same scale. This process allows you to compare scores between different types of variables. Typically, to standardize variables, you calculate the mean and standard deviation for a variable. Then, for each observed value of the variable, you **subtract the mean** and **divide by the standard deviation**.
    - Data will have mean 0 and standard deviation 1 now.
    - Can be done using standard scaler.

If you do not deal with outliers, standardization will make the data too small.