# Kódová matrioška: Žákovská knížka

Program zatím **nic neumí**. Každý z vás dopíše jednu funkci a pak je spojíte dohromady.

## Kdo co dělá

Čtveřice = dvě dvojice. Hned se domluvte, kdo je kdo.

| Kdo | Soubor | Funkce | Co má dělat |
|-----|--------|--------|-------------|
| **A1** | `znamky.py` | `prumer` | Spočítá **průměr známek** ze seznamu. `[1, 2, 3]` → `2.0` |
| **A2** | `znamky.py` | `prospel` | Zjistí, jestli žák **prospěl** (nemá žádnou pětku). `[1, 5, 2]` → `False` |
| **B1** | `test.py` | `body_na_znamku` | Přepočítá **body z testu na známku** 1–5. `72` bodů → `3` |
| **B2** | `test.py` | `slovne` | Změní číslo známky na **slovo**. `3` → `"dobře"` |

Dvojice A je na větvi `polovina-a`, dvojice B na větvi `polovina-b`. 
Sahejte jen do svého souboru. `main.py` a `kontrola.py` neupravuje nikdo.

## Co jsou ty `???`

Ve své funkci najdete řádek `return "???"`. Je to jen **výplň**, aby šel program spustit. 
**Smažte ho a napište vlastní řešení.** Zadání a nápověda jsou v textu nad ním.

Spusťte `main.py` (tlačítko ▶ ve VS Code). Každá `???` čeká na jednoho z vás:

```
Průměr: ???           <- A1
Prospěl: ???          <- A2
Známka z testu: ???   <- B1
Slovně: ???           <- B2
```

`kontrola.py` ukáže u každé funkce OK nebo CHYBA. Cizí funkce budou zatím CHYBA, to je v pořádku.

---

## 1. Stáhnout projekt

1. **Jeden z čtveřice:** na GitHubu *Use this template → Create a new repository*. Pak *Settings → Collaborators* a pozve ostatní tři. Pak vytvoří větve `polovina-a` a `polovina-b` (přepínač větví → napsat název → Create branch).
2. **Ostatní:** přijmou pozvánku z e-mailu.
3. **Všichni:** GitHub Desktop → *File → Clone repository*. Nahoře *Current branch* → vyberte svou větev. Pak *Repository → Open in Visual Studio Code*.

## 2. Napsat svůj kousek

1. Ve svém souboru přepište na začátku `AUTORI = "..."` **svým jménem**.
2. Nahraďte `return "???"` svým řešením. Zkontrolujte přes `kontrola.py`.
3. GitHub Desktop: napište zprávu (např. `A1 prumer`) → **Commit** → **Push origin**.

Pokud vám Desktop místo Push origin nabídne **Pull origin**, klikněte na něj.

> Nejdřív dokončete a odešlete svůj kousek, teprve potom klikejte na Pull.

**Stane se něco, čemu nerozumíte? Nic nemažte a zvedněte ruku.**

---

## Hotové části

(zatím prázdné, vyplníte na konci hodiny)
