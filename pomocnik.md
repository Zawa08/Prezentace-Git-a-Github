# Pomocníček: Git a GitHub

Tahák k hodině. Najdeš tu přípravu, příkazy, slovníček a odkazy.

---

## 1. Příprava (instalace)

Udělej doma před hodinou:

1. **Účet na GitHubu:** zaregistruj se na [github.com](https://github.com). Bez něj nic neuložíš online.
2. **Nainstaluj Git:** stáhni instalátor z [git-scm.com](https://git-scm.com), proklikej ho a nech všechno na výchozím nastavení.
3. **Nastav svou identitu:** otevři Git Bash a napiš tyhle dva příkazy s e-mailem, který používáš na GitHubu. Bez nich ti Git později nedovolí ukládat práci.
   ```
   git config --global user.name "Tvoje Jméno"
   git config --global user.email "tvuj@email.cz"
   ```
4. **Nainstaluj Visual Studio Code:** stáhni z [code.visualstudio.com](https://code.visualstudio.com).
5. **Plugin Git Graph:** ve VS Code stiskni **Ctrl + Shift + X** (záložka Extensions), vyhledej „Git Graph" (autor mhutchie) a klikni na **Install**.
6. **Git Bash jako terminál ve VS Code:** stiskni **Ctrl + ~** (nebo v menu *Terminal → New Terminal*) a otevře se spodní panel. Klikni na šipku vedle ikony **+**, vyber **Select Default Profile** a zvol **Git Bash** místo toho nepohodlného PowerShellu.
7. **Nainstaluj GitHub Desktop:** stáhni z [desktop.github.com](https://desktop.github.com).
8. **Přihlas se:** v GitHub Desktopu jdi na **File → Options → Accounts** a přihlas se ke GitHubu. Přihlašování se pak řeší samo na pozadí a nikdy nemusíš psát heslo do terminálu.

> **Mac:** Git Bash nepotřebuješ, příkazy se píšou do běžného **Terminálu** (ve VS Code ho nech na výchozím nastavení, krok 6 přeskoč). V GitHub Desktopu je přihlášení v menu *GitHub Desktop → Settings → Accounts*.

---

## 2. Příkazy v terminálu

| Příkaz | Co dělá |
|--------|---------|
| `cd` | přejde do jiné složky |
| `ls` | vypíše obsah aktuální složky |
| `mkdir` | vytvoří novou složku |
| `mv` | přesune nebo přejmenuje soubor či složku |
| `rm` | smaže soubor, **nevratně, bez koše** |
| `touch` | vytvoří prázdný soubor |
| `cat` | vypíše obsah souboru do terminálu |
| `nano` | otevře textový editor přímo v terminálu |

---

## 3. Slovníček

| Pojem | Co to je |
|-------|----------|
| **Repository** | Složka tvého projektu. Obsahuje všechny soubory, kód i historii změn. |
| **README** | Úvodní dokument projektu. Vysvětlí nováčkovi, co projekt dělá, jak ho nainstalovat a spustit. |
| **.gitignore** | Skrytý soubor se seznamem věcí, které Git nikdy nemá nahrávat na server (např. hesla, API klíče). |
| **Commit** | „Uložení stavu". Není to jen Ctrl+S: commit dá tvým změnám razítko s popisem (*commit message*), co a proč jsi upravil. |
| **Branch** | Odbočka od hlavního kódu. Můžeš na ní pracovat na nové funkci nebo opravě chyby a nerozbiješ tím, co funguje ostatním. |
| **Main** | Název hlavní větve projektu. Měla by vždy obsahovat funkční a otestovaný kód. |
| **Clone** | Stažení kompletní kopie repozitáře z GitHubu k tobě do počítače, abys na něm mohl pracovat lokálně. |
| **Push** | Odeslání tvých lokálních uložení (commitů) z počítače nahoru na GitHub. |
| **Fetch** | Zjištění a stažení informací o tom, co se na GitHubu změnilo od tvé poslední návštěvy, ale bez automatického přepsání tvého kódu. |
| **Pull** | Stažení změn z GitHubu a jejich rovnou zapracování do tvého kódu. |
| **Pull Request** | Žádost o kontrolu a začlenění tvých změn. Říkáš tím majiteli projektu: *„Napsal jsem tuhle funkci ve své větvi, podívej se na ni, a pokud je dobrá, vlož ji do hlavního kódu."* |
| **Merge** | Sloučení změn z jedné větve (nebo schváleného Pull Requestu) do jiné větve. |

---

## 4. Jak napsat dobrý commit

Commit message má dvě části:

- **Hlavička:** krátký a výstižný popis toho, co se mění (maximálně 50 znaků).
- **Tělo (poznámka):** podrobné vysvětlení, proč se změna udála, jaký problém řeší a na co si dát případně pozor.

Tělo je od hlavičky oddělené **jedním prázdným řádkem**. Můžeš sem přidat i odkazy na úkoly (např. `Resolves #123`).

```
Přidej výpočet průměru známek

Funkce prumer() dosud vracela jen "???". Nově sečte
všechny známky a vydělí je jejich počtem.
```

V **GitHub Desktopu** je hlavička políčko *Summary* a tělo políčko *Description*.

---

## 5. Odkazy

- **[Pro Git](https://git-scm.com/book/en/v2)**: oficiální kniha o Gitu, zdarma (anglicky).
- **[Learn Git Branching](https://learngitbranching.js.org/)**: interaktivní hra, kde si větve procvičíš graficky.
- **[Oh Shit, Git!?!](https://ohshitgit.com/)**: co dělat, když se něco pokazí. Stejný obsah bez vulgarit najdeš na [dangitgit.com](https://dangitgit.com/).
