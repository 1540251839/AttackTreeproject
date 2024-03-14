import os
import sys
rootFileName = 'code'
rootPath = __file__[:str(__file__).find(rootFileName) + len(rootFileName)]
utilPath = os.path.join(rootPath, 'utils')

print(f"项目根目录：{rootPath}")
print(f"utils目录：{utilPath}")

sys.path.append(utilPath)
sys.path.append(rootPath)