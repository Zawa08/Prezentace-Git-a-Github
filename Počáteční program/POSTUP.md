# Postup hodiny (do repa studentů NEDÁVAT)

## Příprava
1. Soubory (bez pro_ucitele/) nahrajte do repa, Settings → zaškrtnout Template repository.
2. Jeden ze čtveřice: Use this template → Settings → Collaborators → pozvat ostatní.
3. Ten samý vytvoří větve polovina-a a polovina-b (na webu v přepínači větví).
4. Všichni jednou: git config --global pull.rebase false

## Fáze 1 – stažení
    git clone <url>
    cd <repo>
    git switch polovina-a      (dvojice B: polovina-b)
    ls
    python main.py             -> vypisuje ???

## Fáze 2 – čtvrtiny → polovina
Každý přepíše řádek AUTORI svým jménem a napíše svou funkci.
Nikdo nedělá pull, dokud nemá hotovo!
    python kontrola.py
    git add .
    git commit -m "A1 prumer"
    git push
Druhý: push odmítnut → git pull → CONFLICT jen v řádku AUTORI
(funkce se spojily samy). Nechat AUTORI = "Jana, Petr", smazat <<<< ==== >>>>,
    git add .
    git commit -m "spojeni"
    git push
GitHub Desktop: Pull origin → okno konfliktu → Open in editor → Continue merge.

## Fáze 3 – poloviny → celek
Každá dvojice upraví v README řádek pod "Hotové části", commit, push.
Pull request polovina-a → main (projde), polovina-b → main (konflikt v README)
→ Resolve conflicts na webu. Pak všichni: git switch main, git pull, python main.py

## Nástavby (další kolečko)
A1: průměr zaokrouhlit na 2 místa – round()
A2: neprospěl ani tehdy, když je průměr horší než 4
B1: při bodech mimo 0–100 vrátit "chyba"
B2: u neznámé známky vrátit "neplatná známka"
