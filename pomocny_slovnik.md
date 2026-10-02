• cd – přejde do jiné složky
• ls – vypíše obsah aktuální složky
• mkdir – vytvoří novou složku
• mv – přesune nebo přejmenuje soubor či složku
• rm – smaže soubor, nevratně, bez koše
• touch – vytvoří prázdný soubor
• cat – vypíše obsah souboru do terminálu
• nano (editor) – otevře soubor v textovém editoru přímo v terminálu

Hlavička: Krátký a výstižný popis toho, co se mění (max 50 znaků)
Tělo (Poznámka): Zde je detailní vysvětlení toho, proč se tato změna
udála, jaký problém řeší a případně na co dalšího si dát pozor.
Tělo je od hlavičky odděleno jedním prázdným řádkem. Můžeš sem přidat
i odkazy na úkoly (např. Resolves #123).

Repository - složka vašeho projektu, obsahuje všechny soubory, kód a historii změn.
README - Úvodní dokument projektu. Slouží jako návod, který nováčkovi vysvětlí, co projekt dělá, jak ho nainstalovat a jak ho spustit.
.gitignore - Skrytý soubor, do kterého zapisujete seznam věcí, které Git nikdy nemá nahrávat na server (např. hesla, API klíče
Commit - "Uložení stavu", Není to jen stisknutí Ctrl+S; commit vtiskne vašim změnám razítko s popisem (commit message), co a proč jste upravili.
Branch - Odbočka od hlavního kódu. Umožňuje pracovat na nové funkci nebo opravě chyby v izolaci, aniž byste rozbili to, co funguje ostatním.
Main - Název pro hlavní větev projektu. Měla by vždy obsahovat funkční a otestovaný kód.
Clone Stažení kompletní kopie repozitáře z GitHubu k vám do počítače, abyste na něm mohli začít pracovat lokálně.
Push - Odeslání vašich lokálních uložení (commitů) z počítače nahoru na server GitHubu.
Fetch - Zjištění a stažení informací o tom, co se na GitHubu změnilo od vaší poslední návštěvy — ale bez automatického přepisu vašeho kódu.
Pull Request - Žádost o kontrolu a začlenění vašich změn. Říkáte tím majiteli projektu: "Napsal jsem tuto funkci ve své větvi, podívej se na ni a pokud je dobrá, vlož ji do hlavního kódu."
Merge - sloučení změn z jedné větve (nebo schváleného Pull Requestu) do jiné větve.
Merge Conflict - Chybový stav. Nastane, když dva lidé upraví stejný řádek ve stejném souboru každý jinak a Git nedokáže sám rozhodnout, která verze má platit. Konflikt musíte vyřešit ručně.

• Create a GitHub account: Go to github.com and register. You need this to sync anything online.
• Install Git: Download the standalone installer from git-scm.com and click through, leaving all settings on default. (Since you already verified you have version 2.39.1, you can technically skip this, but updating ensures no weird bugs).
• Configure your local Git identity: Open Git Bash and run these exact two commands using your new GitHub email. If you skip this, Git will completely block you from saving any work later.
• git config --global user.name "Your Name"
• git config --global user.email "your@email.com"
• Install Visual Studio Code: Download from code.visualstudio.com and install.
• Install the Git Graph plugin: Open VS Code, press Ctrl + Shift + X to open the Extensions tab, search for "Git Graph" (by mhutchie), and hit Install.
• Set Git Bash as the VS Code terminal: Press Ctrl + ~ in VS Code to open the bottom terminal panel. Click the dropdown arrow next to the + icon on the right, click "Select Default Profile," and choose "Git Bash" to replace the clunky default PowerShell.
• Install GitHub Desktop: Download from desktop.github.com and install.
• Log in and link: Open GitHub Desktop, go to File > Options > Accounts, and sign in to your GitHub account. This handles the complex web authentication tokens in the background so you never have to manually type passwords in the terminal.

https://git-scm.com/book/en/v2
https://learngitbranching.js.org/
https://ohshitgit.com/
