# Úloha: Jak vypadají větve

V téhle úloze na vlastní oči uvidíš, co je **větev (branch)**: jak se historie projektu rozdělí na dvě cesty a pak zase spojí.

> **Než začneš:** musíš mít hotovou přípravu (Git, VS Code, plugin Git Graph, Git Bash v terminálu). Návod je v [Readme_Pomocnik.md](Readme_Pomocnik.md), část *Příprava*.

**Kopírování do terminálu:** v samostatném okně Git Bash vloží Ctrl+V divné znaky (třeba `^[[200~`). Tam použij **Shift + Insert**. V terminálu uvnitř VS Code funguje normální Ctrl+V.

---

## Scénář

Stavíš aplikaci a začneš dělat riskantní experimentální funkci. V půlce zjistíš, že v hlavní aplikaci je **kritická chyba**, která se musí opravit hned.

Opravit ji v experimentu nejde, protože ten ještě nechceš vydat. Potřebuješ se **vrátit v čase**, chybu opravit na hlavní časové ose a později všechno spojit. Takhle na to:

---

## Krok 1: Čistý začátek

Ve VS Code otevři terminál (**Ctrl + ~** nebo v menu *Terminal → New Terminal*) a napiš:

```
mkdir git-lesson
cd git-lesson
git init
code .
```

Složka se vytvoří tam, kde terminál právě je. Příkaz `code .` otevře VS Code na této nové složce (může se otevřít nové okno). Otevři v něm terminál znovu.

> **Důležité:** dole v modré/fialové stavové liště VS Code klikni na **Git Graph**. Nech tuhle záložku otevřenou vedle kódu, budeš se do ní dívat po každém kroku.

## Krok 2: Hlavní časová osa

Vytvoříme první soubor a uložíme ho do historie:

```
echo "Version 1: The foundation" > app.txt
git add app.txt
git commit -m "First commit"
```

> 👀 **V Git Graphu:** vidíš jednu tečku. To je hlavní časová osa (obvykle se jmenuje `master` nebo `main`).

## Krok 3: Odbočka pro novou funkci

Tvůj bláznivý nápad bezpečně oddělíme, aby nerozbil hlavní aplikaci:

```
git checkout -b experimental-feature
echo "Adding a crazy new button" >> app.txt
git add app.txt
git commit -m "Started experimental feature"
```

> 👀 **V Git Graphu:** máš dvě tečky nad sebou. Tučný popisek ukazuje, že právě pracuješ ve větvi `experimental-feature`.

## Krok 4: Naléhavá oprava (rozdělení časové osy)

Průšvih! Hlavní aplikace padá. Experiment musíš na chvíli opustit a jít opravit ostrý kód.

Nejdřív se vrať na hlavní časovou osu:

```
git checkout master
```

(Pokud Git ohlásí chybu, tvoje hlavní větev se asi jmenuje `main`. Napiš `git checkout main`.)

Teď vytvoř opravu a ulož ji:

```
echo "URGENT FIX: Server was crashing" > fix.txt
git add fix.txt
git commit -m "Hotfix for server crash"
```

> 👀 **V Git Graphu:** časová osa se rozdělila do tvaru písmene **Y**. Oprava je na jedné cestě a experiment je v bezpečí na druhé. Opravil jsi ostrou aplikaci a na rozbitý experiment ses ani nedotkl.

## Krok 5: Spojení zpátky

Krize skončila. Experimentální funkci vrátíme do hlavní časové osy, tentokrát přes Git Graph místo terminálu:

1. Ujisti se, že jsi na větvi `master` (nebo `main`). Její popisek musí být v Git Graphu **tučně**.
2. Najdi tečku na druhé větvi s popiskem **„Started experimental feature"**.
3. Klikni na ni **pravým tlačítkem**.
4. Vyber **„Merge into current branch…"**.
5. Klikni na **„Yes, merge"**.

> 👀 **V Git Graphu:** dvě oddělené cesty se zase spojily do jedné. Zvládl jsi souběžný vývoj, aniž bys cokoli zničil.

---

## Co sis vyzkoušel

- **Větev** je odbočka, na které můžeš dělat změny, aniž bys ovlivnil hlavní kód.
- Dvě větve se mohou vyvíjet **současně** a nepřekáží si.
- **Merge** je spojí zpátky do jedné historie.

Tohle samé budeš dělat v týmu, jen místo jednoho člověka budete dva.
