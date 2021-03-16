import  sys

import pytest
import yaml


sys.path.append('..')
print(sys.path)
# class Calculate:
#     def add(self,a,b):
#         return a+b
#
#     def div(self,a,b):
#         return  a/b
from python_orig.test_demo import Calculate

def yaml_parse():
    with open('./data/load.yml') as f:
        datas = yaml.safe_load(f)
        print(datas)
        data =datas[]
class Testcal:
    @pytest.mark.parametrize('a,b,result', [(1, 2, 3), (5, 15, 11)])
    #@pytest.mark.parametrize('[a,b,result]',yaml.safe_load(open('./data/load.yml'))
    def test_demo(self,a,b,result):
        #创建实例
        self.cal = Calculate()  # 实例变量
        assert  result == self.cal.add(a,b)


    def test_demo2(self,a,b,result):
        assert  result == self.cal.min(a,b)
#todo 知识点罗列
#todo yaml 结合数据验证
'''
fixture
pytest.mark.search
yaml 字典 列表，safe_load open ,改变对应parametrize-data ids
异常逻辑
yaml 用例分解 正常数据、异常数据、比如四则运算的整型 浮点型 try except mark.except
pytest 命令行学习
git 环境搭建 git push pull
'''





