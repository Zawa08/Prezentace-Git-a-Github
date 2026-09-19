# VZOROVÉ ŘEŠENÍ – nedávat studentům

def prumer(znamky):
    return sum(znamky) / len(znamky)

def prospel(znamky):
    if 5 in znamky:
        return False
    return True

def body_na_znamku(body):
    if body >= 90:
        return 1
    elif body >= 75:
        return 2
    elif body >= 50:
        return 3
    elif body >= 30:
        return 4
    else:
        return 5

def slovne(znamka):
    if znamka == 1:
        return "výborně"
    elif znamka == 2:
        return "chvalitebně"
    elif znamka == 3:
        return "dobře"
    elif znamka == 4:
        return "dostatečně"
    else:
        return "nedostatečně"
