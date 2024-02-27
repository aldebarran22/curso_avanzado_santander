from singleton_idiomas import i18n


def prueba():
    print(i18n.getInstance()["twitter"])
    print(i18n.getInstance()["facebook"])
    print(i18n.getInstance("en")["instagram"])
    print(i18n.getInstance()["facebook"])


prueba()
