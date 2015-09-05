from p12pos import app
import p12pos.config as config
import yaml
translations = yaml.load(open("lang/{}/translations.yml".format(config.locale)))

def _(s):
    if s in translations:
        return translations[s]
    return s

@app.context_processor
def inject_i18n_templates():
    return dict(_=_)
