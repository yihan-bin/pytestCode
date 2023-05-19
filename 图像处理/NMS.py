import cv2
import numpy as np
import matplotlib.pyplot as plt
###########非极大值抑制
#non_max_suppression
class NMS:
    '''
        3. 实现
            3.1 输入
            给定所有可能的预测边框 predictions = [ [x_max, x_min, y_max, y_min, score], [*], ..., [*]] 以及一个给定的IoU阈值 iou_threshold.（有多少个类别就执行多少次NMS算法）

            3.2 输出
            经过NMS算法过滤后的预测框 result = [x_max, x_min, y_max, y_min, score].

            3.3 算法
            （1）将所有可能的预测框按类别划分为num_class+1个集合，其中1为背景类，背景类无需NMS处理；

            （2）对于每一个集合（类别），按类别分数从高到低进行排序，得到num_class个降序列表 lst；

            （3）从 lst 中取得第一个元素（分数最高），逐个计算该元素与列表中剩余元素的IoU，若IoU大于给定阈值则将该元素从列表总剔除，同时将第一个元素保留；

            （4）对处理过后的降序列表 lst 重复执行步骤（3），直至 lst 为空；

            （5）对每一个类别都执行步骤（3）~（4），直接遍历完所有的类别；
            (1)从最大概率矩形框F开始，分别判断A~E与F的重叠度IOU是否大于某个设定的阈值;
        先假设有6个矩形框，根据分类器的类别分类概率做排序，假设从小到大属于车辆的概率 分别为A、B、C、D、E、F。

        (1)从最大概率矩形框F开始，分别判断A~E与F的重叠度IOU是否大于某个设定的阈值;


        著作权归作者所有。商业转载请联系作者获得授权,非商业转载请注明出处。
        原文: https://www.cnblogs.com/makefile/p/nms.html © 康行天下
        (2)假设B、D与F的重叠度超过阈值，那么就扔掉B、D；并标记第一个矩形框F，是我们保留下来的。

        (3)从剩下的矩形框A、C、E中，选择概率最大的E，然后判断E与A、C的重叠度，重叠度大于一定的阈值，那么就扔掉；并标记E是我们保留下来的第二个矩形框。


著作权归作者所有。商业转载请联系作者获得授权,非商业转载请注明出处。
原文: https://www.cnblogs.com/makefile/p/nms.html © 康行天下
    '''
    def __init__(self, center=False, scale=1.0):
        """
        :param center: the format of coordinate -> diagonal [x1, y1, x2, y2] or center [x, y, w, h]
        """
        self.center = center
        self.scale = scale

    def compute_iou(self, bbox1, bbox2, eps=1e-8):
        """
        compute the IoU of two bounding boxes.
        :param eps: avoid
        :param bbox1: bounding box No.1.
        :param bbox2: bounding box No.2.
        :return: IoU of bbox1 and bbox2.
        """
        if self.center:
            x1, y1, w1, h1 = bbox1
            xmin1, ymin1 = int(x1-w1/2.0), int(y1-h1/2.0)
            xmax1, ymax1 = int(x1+w1/2.0), int(y1+h1/2.0)
            x2, y2, w2, h2 = bbox2
            xmin2, ymin2 = int(x2-w2/2.0), int(y2-h2/2.0)
            xmax2, ymax2 = int(x2 + w2 / 2.0), int(y2 + h2 / 2.0)
        else:
            xmin1, ymin1, xmax1, ymax1 = bbox1
            xmin2, ymin2, xmax2, ymax2 = bbox2

        # 计算交集的对角坐标点
        xx1 = np.max([xmin1, xmin2])
        yy1 = np.max([ymin1, ymin2])
        xx2 = np.min([xmax1, xmax2])
        yy2 = np.min([ymax1, ymax2])

        # 计算交集面积
        w = np.max([0.0, xx2 - xx1 + 1])
        h = np.max([0.0, yy2 - yy1 + 1])
        area_intersection = w * h

        # 计算并集面积（这里要记得去掉重叠的面积，避免重复计算）
        area1 = (xmax1 - xmin1 + 1) * (ymax1 - ymin1 + 1)
        area2 = (xmax2 - xmax1 + 1) * (ymax2 - ymin2 + 1)
        area_union = area1 + area2 - area_intersection

        # 计算两个边框的交并比
        iou = area_intersection / (area_union + eps)

        return iou

    @classmethod
    def py_cpu_nms(cls, dets, iou_thresh=0.5, score_thresh=0.5):
        """
        Pure Python NMS baseline. -> take reference from the Fast R-CNN.
        :param iou_thresh: iou thresh -> default 0.5.
        :param score_thresh: cls score thresh -> default 0.5.
        :param dets: detection results -> [[xmin1, ymin1, xmax1, ymax1, score1], [xmin2, ymin2, xmax2, ymax2, score2], ...].
        :return: optimal bounding boxes.
        """
        dets = dets[np.where(dets[:, -1] >= score_thresh)[0]]  # 过滤掉低于分数阈值的预测框

        xmin = dets[:, 0]  # xmin -> [xmin1, xmin2, ...]
        ymin = dets[:, 1]  # ymin -> [ymin1, ymin2, ...]
        xmax = dets[:, 2]  # xmax -> [xmax1, xmax2, ...]
        ymax = dets[:, 3]  # ymax -> [ymax1, ymax2, ...]
        scores = dets[:, 4]  # predict bbox class score -> [score1, score2, score3]

        order = scores.argsort()[::-1]  # 按score降序排序，argsort返回降序后的索引
        areas = (xmax - xmin + 1) * (ymax - ymin + 1)  # 计算面积
        keep = []  # 保留最优的结果

        # 搜索最佳边框
        while order.size > 0:
            top1_idx = order[0]  # 选取得分最高的边框
            keep.append(top1_idx)  # 添加到候选列表

            # 将得分最高的边框与剩余边框进行比较
            xx1 = np.maximum(xmin[top1_idx], xmin[order[1:]])
            yy1 = np.maximum(ymin[top1_idx], ymin[order[1:]])
            xx2 = np.minimum(xmax[top1_idx], xmax[order[1:]])
            yy2 = np.minimum(ymax[top1_idx], ymax[order[1:]])

            # 计算交集
            w = np.maximum(0.0, xx2 - xx1 + 1)
            h = np.maximum(0.0, yy2 - yy1 + 1)
            intersection = w * h

            # 计算并集
            union = areas[top1_idx] + areas[order[1:]] - intersection

            # 计算交并比
            iou = intersection / union


            # 将重叠度大于给定阈值的边框剔除掉，仅保留剩下的边框，返回相应的下标
            inds = np.where(iou <= iou_thresh)[0]


            # 从剩余的候选框中继续筛选
            order = order[inds + 1]


        return keep


if __name__ == '__main__':
    img = cv2.imread("data/OIP-C.jpg")
    img_cp = np.copy(img)
    thickness = 2
    info = np.array([
        [30, 10, 200, 200, 0.95],
        [25, 15, 180, 220, 0.98],
        [35, 40, 190, 170, 0.96],
        [60, 60, 90, 90, 0.3],
        [20, 30, 40, 50, 0.1],
    ])
    colors = [[0, 0, 255], [0, 255, 0], [255, 0, 0], [255, 255, 0], [0, 255, 255]]

    plt.subplot(121)
    plt.axis('off')
    plt.title("Input image")
    for i in range(len(colors)):
        x1, y1, x2, y2, _, = info[i]
        cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), colors[i], thickness=thickness)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)

    plt.subplot(122)
    plt.axis('off')
    plt.title("After NMS")
    indx = NMS.py_cpu_nms(dets=info, iou_thresh=0.5, score_thresh=0.5)
    for i in indx:
        x1, y1, x2, y2, _ = info[i]
        cv2.rectangle(img_cp, (int(x1), int(y1)), (int(x2), int(y2)), colors[i], thickness=thickness)
    img_cp = cv2.cvtColor(img_cp, cv2.COLOR_BGR2RGB)
    plt.imshow(img_cp)


    # 保存并显示图片
    plt.savefig('results.png')
    plt.show()