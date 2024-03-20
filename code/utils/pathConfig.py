import os
import sys
rootFileName = 'code'
rootPath = __file__[:str(__file__).find(rootFileName) + len(rootFileName)]
utilPath = os.path.join(rootPath, 'utils')
frontEndPath = os.path.join(rootPath, 'frontend')
cssPath = os.path.join(frontEndPath, 'css')
jsPath = os.path.join(frontEndPath, 'js')
plotPath = os.path.join(rootPath, 'generate_plot')
dataPoolPath = os.path.join(rootPath, 'dataPool')

print(f"项目根目录：{rootPath}")
print(f"utils目录：{utilPath}")
print(f"前端目录：{frontEndPath}")
print(f"css目录：{cssPath}")
print(f"js目录：{jsPath}")
print(f"plot目录：{plotPath}")
print(f"dataPool目录：{dataPoolPath}")

sys.path.append(utilPath)
sys.path.append(rootPath)
sys.path.append(frontEndPath)
sys.path.append(cssPath)
sys.path.append(jsPath)
sys.path.append(plotPath)
sys.path.append(dataPoolPath)