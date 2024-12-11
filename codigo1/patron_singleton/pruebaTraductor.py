from traductor  import SingletonIdioma

if __name__ == '__main__':
    try:
        d = SingletonIdioma.getInstance("en")['inicio']
        print(d)
        d = SingletonIdioma.getInstance("en")['twitter']
        print(d)
        d = SingletonIdioma.getInstance("es")['inicio']
        print(d)
    except  Exception as e:
        print(e)