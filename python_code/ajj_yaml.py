import yaml


def test_yaml():
    with open("./data/load.yml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        #print(datas['add']['datas'])

test_yaml()
