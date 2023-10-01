from sample_madlibs import hp, code, zombie, hungergames
import random

if __name__ == "__main__":
    madlibs_modules = [hp, code, zombie, hungergames]
    selected_module = random.choice(madlibs_modules)
    selected_module.madlibs()
