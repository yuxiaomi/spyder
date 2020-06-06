from wordcloud import WordCloud
import PIL .Image as image
import numpy as np
import jieba

def putong():
    from wordcloud import WordCloud
    with open("D:\spyder\spyder\word_cloud_dir\minister.txt",encoding="utf-8")as f:
        text=f.read()
        # print(text)
        WordCloud=WordCloud().generate(text)
        image_produce=WordCloud.to_image()
        image_produce.show()

def img():
    with open("D:\spyder\spyder\word_cloud_dir\minister.txt") as fp:
        text = fp.read()
        # print(text)
        mask = np.array(image.open("D:\spyder\spyder\word_cloud_dir\wordcloud_test.jpg"))
        wordcloud = WordCloud(
            mask=mask
        ).generate(text)
        image_produce = wordcloud.to_image()
        image_produce.show()

def parsegbk(text):
    word_list = jieba.cut(text)
    # 分词后在单独个体之间加上空格
    result = " ".join(word_list)
    return result

def cnimg():
    with open("D:\spyder\spyder\word_cloud_dir\cnword.txt",'r',encoding='utf-8') as fp:
        text = fp.read()
        text = parsegbk(text)
        # print(text)
        mask = np.array(image.open("D:\spyder\spyder\word_cloud_dir\jd.jpg"))
        wordcloud = WordCloud(
            mask=mask,
            contour_width=5,
            height=400,#当设置了背景的img时这是长宽将被忽略
            width=500,
            min_font_size=4,
            max_font_size=50,
            background_color="white",
            # mode='RGBA',
            colormap="viridis",#给每个字体随机分配颜色
            contour_color="White",
            font_path="C:\\Windows\\Fonts\\STXINGKA.TTF"
        ).generate(text)
        image_produce = wordcloud.to_image()
        wordcloud.to_file("D:\spyder\spyder\word_cloud_dir\gene.jpg")
        image_produce.show()

if __name__ == '__main__':
    # putong()
    # img()
    cnimg()
