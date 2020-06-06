from PIL import Image
import imagehash,os

def mach(original,dir):
    orhash=imagehash.average_hash(Image.open(original))
    print("原始的：",orhash)
    allfile=[]
    for root,dirs,files in os.walk(dir):
        # 输出所有的文件的名字
        for name in files:
            files=os.path.join(root,name)
            allfile.append(files)
    # print(allfile)
    match=[]
    for i in allfile:
        print(i)
        now=imagehash.average_hash(Image.open(i))
        if now==orhash:
            print("匹配到的图片为：",i)
            match.append(i)
            # break
    print("最后的结果：")
    for n in match:
        print(n)

if __name__ == '__main__':
    mach(r"C:\Users\yuxiaomi\Desktop\index.jpg","E:\outputss")
