#!/usr/bin/env python3
import sys

弦位 = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 6}
人话 = "没法读弦：请给出一段减字，里面正好有一个弦位\n"

def 读出(文本):
    找到 = [字 for 字 in 文本 if 字 in 弦位]
    if len(找到) != 1:
        return 2, "", 人话
    return 0, "第%d弦\n" % 弦位[找到[0]], ""

def 主程序(参数):
    if len(参数) != 1 or 参数[0] == "" or 参数[0] == "缺":
        sys.stderr.write(人话)
        return 2
    码, 出, 错 = 读出(参数[0])
    if 出:
        sys.stdout.write(出)
    if 错:
        sys.stderr.write(错)
    return 码

if __name__ == "__main__":
    raise SystemExit(主程序(sys.argv[1:]))
