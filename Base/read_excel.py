import xlrd
class Execl_api:
    def __init__(self):
        self.workbook = xlrd.open_workbook("D:\\yundeng_apis\\Data\\api.xlsx")
        self.workSheet = self.workbook.sheet_by_name("接口文档")
    def case_data(self,a,b):#a指行，b指列
        case_value = self.workSheet.cell(a,b).value
        return case_value


# if __name__ == '__main__':
#     print(Execl_api().case_data(2,5))