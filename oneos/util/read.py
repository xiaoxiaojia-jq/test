import xlrd
class Read:
    def read(self):
        books=xlrd.open_workbook("../../oneos/data/testcase.xlsx")
        sheet=books.sheets()[0]
        test_datas=[]
        for i in range(1,sheet.nrows):
            test_data = []
            test_step = []
            test_mode=[]
            test_route=[]
            test_result=[]
            cells = sheet.row_values(i)
            test_data.append(cells[0])
            # 获取步骤
            steps=cells[1].split('\n')
            # print(test_steps,type(test_steps))
            for i in steps:
                step=i.split('.')
                test_step.append(step[1])
            test_data.append(test_step)
            # 获取步骤
            modes = cells[2].split('\n')
            for j in modes:
                mode = j.split('.')
                test_mode.append(mode[1])
            test_data.append(test_mode)
            #获取路径方式
            routes = cells[3].split('\n')
            for k in routes:
                route = k.split('.')
                test_route.append(route[1])
            test_data.append(test_route)
            #获取预期断言
            results = cells[4].split('\n')
            for m in results:
                result = m.split('.')
                test_result.append(result[1])
            test_data.append(test_result)
            test_datas.append(test_data)
        return test_datas



if __name__ == '__main__':
    a=Read()
    b=a.read()
    print(b)