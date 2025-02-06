# Tcp-Bank
Je aplikace přístupná přes internet mnohdy na lokální síti a nebo ip adrese, kterou ji nastavíte.
Tato aplikace specificky spraveje účty v bance. Takže po zadání správných komandu program command vykonná.
Komandů tu máme kned několik.



| Název commandu         | Kód | Volání | Odpověď při úspěchu | Odpověď při chybě |
|------------------------|-----|--------|--------------------|---------------|
| Bank code              | BC | BC     | BC \<ip> | ER \<message> |
| Account create         | AC | AC     | AC \<account>/\<ip> | ER \<message> |
| Account deposit        | AD | AD \<account>/\<ip> \<number>| AD  | ER \<message> |
| Account withdrawal     | AW | AW \<account>/\<ip> \<number>| AW  | ER \<message> |
| Account balance        | AB | AB \<account>/\<ip>| AB \<number>| ER \<message> |
| Account remove         | AR | AR \<account>/\<ip>| AR  | ER \<message> |
| Bank (total) amount    | BA | BA     | BA \<number> | ER \<message> |
| Bank number of clients | BN | BN     | BN \<number> | ER \<message> |

## Zkratky

- \<ip> - IP adresa aktuálního serveru, kde program běží může být i local host
- \<account> - číslo účtu
- \<number> - výše obnosu
- \<message> - chybová zpráva


pip install mysql-connector-python

AB AD AW