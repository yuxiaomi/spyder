import cv2,os,time,datetime

def moviecut(url,outurl,formats):
    video_path=url
    times=0
    #提取视频的频率，每１帧提取一个
    frameFrequency=5
    #输出图片到当前目录vedio文件夹下
    outPutDirName=outurl
    if not os.path.exists(outPutDirName):
        #如果文件目录不存在则创建目录
        os.makedirs(outPutDirName)
    camera = cv2.VideoCapture(video_path)
    while True:
        times+=1
        res, image = camera.read()
        if not res:
            print('not res , not image')
            break
        if (times%frameFrequency==0):
            # 以每一帧的时间命名
            filename=str(datetime.timedelta(milliseconds=camera.get(0))).replace(":","-").replace(".","-")
            # print(filename)
            cv2.imwrite(outPutDirName + '/'+filename+formats, image)  # 存储为图像
            print(outPutDirName+"/"+filename+formats)
        cv2.waitKey(1)
    print('图片提取结束')
    camera.release()


def save_img(url,saveurl):
    vc = cv2.VideoCapture(url)  # 读入视频文件，命名cv
    n = 1  # 计数
    if vc.isOpened():  # 判断是否正常打开
        rval, frame = vc.read()
    else:
        rval = False
    timeF = 1  # 视频帧计数间隔频率
    i = 0
    while rval:  # 循环读取视频帧
        rval, frame = vc.read()
        if (n % timeF == 0):  # 每隔timeF帧进行存储操作
            i += 1
            cv2.imwrite(saveurl+'/{}.jpg'.format(i), frame)  # 存储为图像
            print(saveurl+'/{}.jpg'.format(i))
        n = n + 1
        cv2.waitKey(1)
    vc.release()


if __name__ == '__main__':
    # 需要cut的视频路径  保存路径（不能有中文） 保存格式
    moviecut(r"E:\电影\为了一张图，我让程序看了20小时的超炮.flv","E:/outputss",'.jpg')
    # save_img("E:/电影/为了一张图，我让程序看了20小时的超炮.flv","E:/output")