# Část 2: Co se právě stalo

## Merge conflict

Dva z vás upravili **stejný řádek** (`AUTORI`). Git neví, čí verze má vyhrát, a tak se zastavil a nechal rozhodnutí na vás.
Nic jste nezkazili, tohle se v týmech děje pořád.

V souboru vidíte:

```
<<<<<<< HEAD
AUTORI = "Petr"
=======
AUTORI = "Jana"
>>>>>>> polovina-a
```

- mezi `<<<<<<<` a `=======` je **vaše** verze,
- mezi `=======` a `>>>>>>>` je verze **z GitHubu**.

## Jak to opravit

1. GitHub Desktop → _Open in Visual Studio Code_.
2. Smažte všechny tři řádky se značkami a nechte **jeden** řádek: `AUTORI = "Jana, Petr"`
   (nebo klikněte _Accept Both Changes_ a řádky sloučte ručně).
3. Uložte (Ctrl+S).
4. GitHub Desktop → **Continue merge** → **Push origin**.
5. Druhý ve dvojici klikne **Pull origin** a spustí `kontrola.py`. Obě funkce vaší poloviny mají být OK.

Všimněte si: samotné funkce se spojily **bez problému**, protože každý psal na jiné místo. Konflikt je jen tam, kde jste upravili stejný řádek.

---

## 3. Spojit poloviny

1. Otevřete `README.md`, dole najděte sekci **Hotové části**.
   Řádek `(zatím prázdné…)` **smažte** a napište jednu větu, co dělá vaše dvojice, např.:
   `Dvojice A (Jana, Petr): průměr známek a zjištění, jestli žák prospěl.`
   Commit → Push.
2. Na GitHubu: **Pull requests → New pull request**, _base:_ `main`, _compare:_ `polovina-a` → Create → **Merge pull request**.
3. Totéž s `polovina-b`.
4. Pokud GitHub ohlásí konflikt, už víte, co to je. Tady se řeší přímo na webu: **Resolve conflicts**, smažte značky, nechte **obě** věty, _Mark as resolved → Commit merge → Merge pull request_.
5. Všichni: GitHub Desktop → větev `main` → **Pull origin** → spusťte `main.py`.

Žádná `???` a osmkrát OK v `kontrola.py` = máte hotovo. 🎉

## Když se něco zasekne

- **Push se nepovedl:** klikněte Pull origin.
- **Nejde push / 403:** nepřijali jste pozvánku, nebo jste přihlášeni pod jiným účtem.
- **SyntaxError u `<<<<<<<`:** v souboru zůstaly značky konfliktu, smažte je.
- **IndentationError:** tělo funkce musí být odsazené o 4 mezery.
