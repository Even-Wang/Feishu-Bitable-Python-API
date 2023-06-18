import argparse
import configparser
from GET_VIEW_ID import GET_VIEW_ID

# 这个函数用于将从GET_VIEW_ID获取的view_id写入到配置文件
def WRITE_VIEW_ID(view_name):
    config = configparser.ConfigParser()  # 创建一个ConfigParser对象
    config.read('feishu-config.ini')  # 读取名为'feishu-config.ini'的配置文件

    # 尝试从view_name获取view_id
    try:
        view_id = GET_VIEW_ID(view_name)
        # 如果提取的值不存在，将其置为空字符串
        if not view_id:
            view_id = ''
    except Exception:  # 如果在尝试过程中出现错误，返回None
        return None

    # 检查配置文件是否存在名为'ID'的section，如果不存在则添加
    if 'ID' not in config:
        config.add_section('ID')
    # 在'ID' section下添加view_id
    config['ID']['view_id'] = view_id

    # 尝试将新的配置写入到名为'feishu-config.ini'的文件中
    try:
        with open('feishu-config.ini', 'w') as configfile:
            config.write(configfile)
    except Exception:  # 如果在尝试过程中出现错误，返回None
        return None

    return view_id  # 如果一切正常，返回提取的值


# 这个函数用于解析命令行参数并调用WRITE_VIEW_ID函数
def WRITE_VIEW_ID_CMD():
    # 创建一个argparse对象，用于解析命令行参数
    parser = argparse.ArgumentParser()
    # 添加一个命名为'-v'或'--view'的参数，该参数是必需的，作用是提供一个视图的名称
    parser.add_argument('-v', '--view', required=True, help='视图的名称')
    # 解析命令行参数
    args = parser.parse_args()
    # 调用WRITE_VIEW_ID函数，将从视图名称获取的view_id写入到配置文件中
    result = WRITE_VIEW_ID(args.view)

    # 检查WRITE_VIEW_ID函数的返回结果
    if result is None:  # 如果返回None，打印错误信息
        print("发生错误，请检查您的输入视图名称并再试一次。")
    else:  # 如果返回的不是None，打印提取的值和成功信息
        print(f"view_id: {result}")
        print("成功写入 'feishu-config.ini' 文件")


# 主函数
if __name__ == "__main__":
    # 调用解析命令行参数的函数
    WRITE_VIEW_ID_CMD()