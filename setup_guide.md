# Jak stáhnout projekt

## 1. Jeden z čtveřice:

1. Na GitHubu _Create a new repository_ **bez** .gitignore, README nebo licence.
2. _Settings → Collaborators_ a pozve ostatní tři.
3. Vytvoří větve `polovina-a` a `polovina-b` (přepínač větví → napsat název → Create branch).

## 2. Ostatní:

Přijmou pozvánku z e-mailu.

## 3. Jeden z čtveřice:

Naklonuje si repozitář [Prezentace Git a Github](https://github.com/Zawa08/Prezentace-Git-a-Github)

`git clone https://github.com/Zawa08/Prezentace-Git-a-Github.git`

`cd Prezentace-Git-a-Github`

Změní remote origin větve na svůj repozitář

`git remote remove origin`

`git remote add origin https://github.com/vase-jmeno/vase-nove-repo.git` dejte svoji URL, kterou najdete pod tlačítkem **CODE**.

Nakonec push, pokud máme master branch přejmenujeme pomocí git branch -M main.

`git push -u origin main`
