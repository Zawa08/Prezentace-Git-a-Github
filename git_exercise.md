**Copy & Paste in Terminal:** If you ever use a standalone Git Bash window, Ctrl+V will insert weird characters (like ^[[200~). Use Shift + Insert instead. However, because we are using the integrated terminal inside VS Code, normal Ctrl+V will work perfectly!

# Part 2: The Core Exercise

## The Scenario:

You are building an app. You decide to start building a risky, experimental new feature. Halfway through, you discover a massive, critical bug in the main app that needs fixing right now.\
You cannot fix the bug in your experimental branch, because you aren't ready to release the experiment yet. You need to travel back in time, fix the bug on the main timeline, and merge everything together later. Here is how you do it.

## Step 1: Set Up a Clean Slate

We need a fresh project. In the VS Code terminal, run these commands:

1. mkdir git-lesson
2. cd git-lesson
3. git init
4. code .

Note: The code . command reloads VS Code to focus entirely on this new folder. Open your terminal (Ctrl + ~) again once it reloads.\
**CRITICAL:** Look at the bottom blue/purple status bar in VS Code and click Git Graph. Keep this tab open next to your code.

## Step 2: Establish the Main Timeline

Let's create our first file and save it to the history.

1. echo "Version 1: The foundation" > app.txt
2. git add app.txt
3. git commit -m "First commit"

Look at Git Graph: You will see a single dot. This is your main timeline (usually called master or main).

## Step 3: Branch Off for a New Feature

Let's safely isolate your crazy new idea so it doesn't break the main app.

1. git checkout -b experimental-feature
2. echo "Adding a crazy new button" >> app.txt
3. git add app.txt
4. git commit -m "Started experimental feature"

**Look at Git Graph:** You now have two dots stacked vertically. The bold label shows you are currently working inside experimental-feature.

## Step 4: The Urgent Hotfix (Splitting the Timeline)

Emergency! The main app is crashing. You have to abandon your experiment for a minute and go fix the live code.
First, travel back in time to the main timeline:

- git checkout master

(If Git gives you an error, your default branch might be called main. Use git checkout main instead).
Now, create the fix and save it:

1. echo "URGENT FIX: Server was crashing" > fix.txt
2. git add fix.txt
3. git commit -m "Hotfix for server crash"

**Look at Git Graph:** The timeline has split into a "Y" shape. Your hotfix is on one path, and your experimental feature is safely quarantined on the other. You fixed the live app without touching the broken experiment.

## Step 5: Merge it Back Together

The crisis is over. Let's bring your experimental feature back into the main timeline using the visualizer instead of the terminal.

1. Ensure you are on the master (or main) branch. (The label should be bolded in Git Graph).
2. Find the dot on the other branch labeled "Started experimental feature".
3. Right-click that dot.
4. Select "Merge into current branch..."
5. Click "Yes, merge".

**Look at Git Graph:** The two separate paths have now reconnected into a single, unified timeline. You successfully managed parallel development without destroying your project.
