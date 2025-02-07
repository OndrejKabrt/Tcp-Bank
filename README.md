# Tcp-Bank

Aplikace přístupná přes internet, mnohdy na lokální síti nebo IP adrese, kterou jí nastavíte. Tato aplikace specificky spravuje účty v bance. Po zadání správných komandů program příkazy vykoná.

## Dostupné Příkazy

| Název commandu | Kód | Volání | Odpověď při úspěchu | Odpověď při chybě |
|----------------|-----|--------|---------------------|-------------------|
| Bank code | BC | BC | BC \<ip> | ER \<message> |
| Account create | AC | AC | AC \<account>/\<ip> | ER \<message> |
| Account deposit | AD | AD \<account>/\<ip> \<number> | AD | ER \<message> |
| Account withdrawal | AW | AW \<account>/\<ip> \<number> | AW | ER \<message> |
| Account balance | AB | AB \<account>/\<ip> | AB \<number> | ER \<message> |
| Account remove | AR | AR \<account>/\<ip> | AR | ER \<message> |
| Bank (total) amount | BA | BA | BA \<number> | ER \<message> |
| Bank number of clients | BN | BN | BN \<number> | ER \<message> |

## Vysvětlení Parametrů

- **\<ip>**: IP adresa aktuálního serveru, kde program běží (může být i localhost)
- **\<account>**: číslo účtu
- **\<number>**: výše obnosu
- **\<message>**: chybová zpráva

## Instalace a Nastavení

### Potřebné Knihovny

Pro spuštění programu v programovacím prostředí je nutné nainstalovat požadované knihovny. Postupujte následovně:

```bash
# Přejděte do adresáře s programem
cd jmeno_direktoře_kde_je_program_uložen 

# Vytvoření virtuálního prostředí (pouze jednou)
python -m venv venv

# Aktivace virtuálního prostředí
venv\Scripts\activate

# Instalace požadované knihovny
pip install mysql-connector-python
```

### Konfigurace

#### Nastavení ipConfig.json

Před spuštěním je nutné upravit soubor `ipConfig.json` s následujícími parametry:

```json
{
    "host": "10.147.18.60",
    "port": 65525,
    "server_timeout": 10,
    "logger_file": "./Logs.txt",
    "client_timeout": 15
}
```

**Důležité parametry:**
- **port**: číslo v rozsahu 65525 - 65535
- **server_timeout**: čas pro připojení k serveru
- **client_timeout**: čas na zadání příkazu (doporučeno více než 15 sekund)

#### Nastavení Databáze

1. Nejprve vytvořte databázi pomocí skriptu `Account.sql`
2. Upravte `databaseConfig.json` s přihlašovacími údaji:

```json
{
  "database": {
    "host": "115.114..112.132",
    "port": 3306,
    "user": "user_name",
    "password": "User_password",
    "database": "database_name"
  }
}
```

## Architektura Aplikace

### Hlavní Komponenty

#### Account
Reprezentační objekt pro data z databáze.

#### AccountDAO
Třída pro komunikaci s databází. Implementuje následující operace:
- **save**: ukládání dat
- **update_positive**: zvyšování hodnot v databázi
- **update_negative**: snižování hodnot v databázi
- **delete**: mazání záznamů
- **select_balance**: zjištění zůstatku
- **select_all**: výběr všech záznamů
- **client_count**: počet klientů

#### Application
Zpracovává uživatelské požadavky a předává je do AccountDAO. Metody odpovídají specifikovaným příkazům.

#### client_UserInterface
Kontroluje formát příkazů a předává je do Application třídy.

#### DatabaseSingleton
Zajišťuje připojení k databázi a čtení konfigurace.

#### Logger
Spravuje logování s následujícími funkcemi:
- **log_input**: logování uživatelských požadavků
- **log_output**: logování odpovědí serveru
- **log_user**: logování připojení uživatelů

#### Server
Řídí připojení klientů a jejich směrování do hlavního procesu.

## Zdroje a Konzultace

Projekt byl konzultován s:
- Adam Hlaváčik
- Martin Hornych

### Odkazy na zdroje
- Uvedl bych zde svoje základní kody, ale ty na githubu nemám. 
- https://github.com/Sharkpb8/Alfa_2_Database
- https://discord.com/channels/788370977007730688/1042124488394932284/1337488679333138432
- https://claude.ai/chat/d52529a4-72e3-4b88-9c2f-8652b25b8477
- https://claude.ai/chat/7e691720-46cf-44f8-af70-5374c3576442
- https://claude.ai/chat/dfa105ea-0bb5-4de3-8ccd-c6faadd082e4
- https://chatgpt.com/c/67a62367-e98c-8004-982a-d7e690d579c5
- https://claude.ai/chat/52c0b3c1-74b6-48d8-966e-d2b2857209d8

## Zdroje
Předchozí projekty, použity i kody z jiných jazyků které byly pouze přepsány do pythonu.

## Odkazy na chaty užité k zvýšení porozumnění
https://claude.ai/chat/267e32ae-a9e9-45d6-9778-9bc1b8625a42

___________________________________________________________________________________________________________________________________________________________________________________________________

# Tcp-Bank

This application is accessible via the internet, often on a local network or IP address that you configure. The application specifically manages bank accounts. After entering the correct commands, the program will execute them.

## Available Commands

| Command name | Code | Call | Success response | Error response |
|--------------|------|------|------------------|----------------|
| Bank code | BC | BC | BC \<ip> | ER \<message> |
| Account create | AC | AC | AC \<account>/\<ip> | ER \<message> |
| Account deposit | AD | AD \<account>/\<ip> \<number> | AD | ER \<message> |
| Account withdrawal | AW | AW \<account>/\<ip> \<number> | AW | ER \<message> |
| Account balance | AB | AB \<account>/\<ip> | AB \<number> | ER \<message> |
| Account remove | AR | AR \<account>/\<ip> | AR | ER \<message> |
| Bank (total) amount | BA | BA | BA \<number> | ER \<message> |
| Bank number of clients | BN | BN | BN \<number> | ER \<message> |

## Parameter Explanation

- **\<ip>**: IP address of the current server where the program is running (can be localhost)
- **\<account>**: account number
- **\<number>**: amount of money
- **\<message>**: error message

## Installation and Setup

### Required Libraries

To run the program in a programming environment, you need to install the required libraries. Follow these steps:

```bash
# Navigate to the program directory
cd name_of_directory_where_program_is_stored

# Create virtual environment (only once)
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install required library
pip install mysql-connector-python
```

### Configuration

#### Setting up ipConfig.json

Before running, you must modify the `ipConfig.json` file with the following parameters:

```json
{
    "host": "10.147.18.60",
    "port": 65525,
    "server_timeout": 10,
    "logger_file": "./Logs.txt",
    "client_timeout": 15
}
```

**Important parameters:**
- **port**: number in range 65525 - 65535
- **server_timeout**: time allowed for connecting to the server
- **client_timeout**: time allowed for command input (recommended more than 15 seconds)

#### Database Setup

1. First, create the database using the `Account.sql` script
2. Modify `databaseConfig.json` with your login credentials:

```json
{
  "database": {
    "host": "115.114..112.132",
    "port": 3306,
    "user": "user_name",
    "password": "User_password",
    "database": "database_name"
  }
}
```

## Application Architecture

### Main Components

#### Account
Representation object for database data.

#### AccountDAO
Class for database communication. Implements the following operations:
- **save**: saving data
- **update_positive**: increasing values in database
- **update_negative**: decreasing values in database
- **delete**: deleting records
- **select_balance**: checking balance
- **select_all**: selecting all records
- **client_count**: counting clients

#### Application
Processes user requests and forwards them to AccountDAO. Methods correspond to specified commands.

#### client_UserInterface
Checks command format and forwards them to the Application class.

#### DatabaseSingleton
Handles database connection and configuration reading.

#### Logger
Manages logging with the following functions:
- **log_input**: logging user requests
- **log_output**: logging server responses
- **log_user**: logging user connections

#### Server
Manages client connections and their routing to the main process.

## Sources and Consultation

Project was consulted with:
- Adam Hlaváčik
- Martin Hornych

### References
- Uvedl bych zde svoje základní kody, ale ty na githubu nemám. 
- https://github.com/Sharkpb8/Alfa_2_Database
- https://discord.com/channels/788370977007730688/1042124488394932284/1337488679333138432
- https://claude.ai/chat/d52529a4-72e3-4b88-9c2f-8652b25b8477
- https://claude.ai/chat/7e691720-46cf-44f8-af70-5374c3576442
- https://claude.ai/chat/dfa105ea-0bb5-4de3-8ccd-c6faadd082e4
- https://chatgpt.com/c/67a62367-e98c-8004-982a-d7e690d579c5
- https://claude.ai/chat/52c0b3c1-74b6-48d8-966e-d2b2857209d8