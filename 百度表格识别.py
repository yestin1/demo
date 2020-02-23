def printlist(result_list, n):
    for i in result_list:
        if isinstance(i, dict):
            printdic(i)
        else:
            n = n + 1
            print((n * "\t" + "[", i, "]"))


def printdic(result_dic):#结果输出函数
    for k, v in list(result_dic.items()):
        n = -1
        if isinstance(v, dict):
            n = n + 1
            print((n * "\t" + '{key}：'.format(key=k)))  # 逐个打印key
            printdic(v)
        elif isinstance(v, list):
            n = n + 1
            print((n * "\t" + '{key}：'.format(key=k)))  # 逐个打印key
            printlist(v, n)
        else:
            n = n + 1
            print((n * "\t" + '{key}：{value}'.format(key=k, value=v)))  # 逐个打印key:value


def imagepath():
    while True:
        path = eval(input('请输入图片地址：'))
        try:
            print('稍等……')
            return path
        except:
            path = eval(input('请重新输入地址：'))


def OCRtable(path):  # 表格识别
    import time
    """ 输入百度ai账号 OCR模式"""
    from aip import AipOcr
    APP_ID = '16352245'
    API_KEY = 'O6B42aucmnhNgvH7in01Uq6Q'
    SECRET_KEY = 'QOMQD7svEGzzZ9rxsfYrxrtd1dBGKAPN'

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    """ 读取图片 """
    import os
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    files = os.listdir(path)
    for f in files:
        image = get_file_content(path + '/' + f)
        """ 调用表格识别 """
        result_dic = client.tableRecognitionAsync(image);  # 返回的是字典dict
        requestId = result_dic.get('result')[0].get('request_id')
        print(requestId)
        time.sleep(20)
        url = client.getTableRecognitionResult(requestId)
        print(url)
    print('全部转换完成。')


path = imagepath()
OCRtable(path)
